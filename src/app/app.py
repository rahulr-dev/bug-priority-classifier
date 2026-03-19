import streamlit as st
import pandas as pd
import datetime
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.models.BugData import BugData
from src.utils.inference import predict, predict_batch

# ── Page config ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Bug Priority Classifier",
    page_icon="🐛",
    layout="centered",
)

st.title("🐛 Bug Priority Classifier")
st.caption("Predicts whether a bug is High Priority (P1/P2) or Low Priority (P3–P5)")

tab1, tab2 = st.tabs(["Single Prediction", "Batch CSV"])

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1 — Single Prediction
# ─────────────────────────────────────────────────────────────────────────────

COMPONENTS = [
    "UI",
    "SWT",
    "Team",
    "Debug",
    "Resources",
    "User Assistance",
    "Ant",
    "Text",
    "Releng",
    "Update",
    "CVS",
    "Runtime",
    "Compare",
    "IDE",
    "Search",
    "Doc",
    "WebDAV",
    "Scripting",
    "Website",
    "PMC",
    "Incubator",
]

VERSIONS = [
    "3.0",
    "2.0",
    "3.1",
    "3.2",
    "2.1",
    "3.3",
    "3.4",
    "3.5",
    "3.6",
    "4.2",
    "3.7",
    "4.3",
    "3.0.1",
    "3.2.1",
    "3.1.1",
    "4.0",
    "1.0",
    "3.3.1",
    "2.0.2",
    "4.1",
    "3.4.1",
    "3.8",
    "2.1.1",
    "3.2.2",
    "3.4.2",
    "2.0.1",
    "3.1.2",
    "4.2.1",
    "2.1.2",
    "4.4",
    "3.0.2",
    "3.3.2",
    "3.5.1",
    "3.6.1",
    "3.6.2",
    "3.7.1",
    "3.5.2",
    "4.2.2",
    "2.1.3",
    "3.7.2",
    "4.3.1",
    "3.8.1",
    "3.8.2",
]


with tab1:
    with st.form("predict_form"):
        title = st.text_input(
            "Title", placeholder="e.g. NullPointerException on workspace load"
        )
        description = st.text_area(
            "Description", placeholder="Describe the bug in detail...", height=150
        )

        col1, col2 = st.columns(2)
        with col1:
            component = st.selectbox(
                "Component", COMPONENTS, index=COMPONENTS.index("Runtime")
            )
        with col2:
            version = st.selectbox("Version", VERSIONS, index=VERSIONS.index("3.0"))

        created_time = st.date_input("Created Date", value=datetime.date.today())
        submitted = st.form_submit_button("Predict", use_container_width=True)

    if submitted:
        if not title.strip() or not description.strip():
            st.warning("Title and Description are required.")
        else:
            bug = BugData(
                title=title,
                description=description,
                component=component,
                version=version,
                created_time=datetime.datetime.combine(
                    created_time, datetime.time()
                ).isoformat(),
            )

            with st.spinner("Predicting..."):
                result, elapsed_ms = predict(bug)

            if result.label == "High Priority":
                st.error(f"🔴 **{result.label}**")
            else:
                st.success(f"🟢 **{result.label}**")

            col1, col2, col3 = st.columns(3)
            col1.metric("Probability", f"{result.probability:.4f}")
            col2.metric("Threshold", f"{result.threshold}")
            col3.metric("Inference Time", f"{elapsed_ms} ms")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — Batch CSV
# ─────────────────────────────────────────────────────────────────────────────

with tab2:
    st.markdown(
        "#### Required columns: `title`, `description`, `component`, `version`, `created_time`"
    )
    st.markdown("Optional column: `expected_label` (used for accuracy comparison)")

    uploaded = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded:
        df_raw = pd.read_csv(uploaded)
        st.subheader("Preview")
        st.dataframe(df_raw.head(), use_container_width=True)

        # ── Validation ────────────────────────────────────────────────────────
        required_cols = {"title", "description", "component", "version", "created_time"}
        missing = required_cols - set(df_raw.columns.str.lower())

        if missing:
            st.error(f"Missing columns: {missing}")
        else:
            # ── Cleanup ───────────────────────────────────────────────────────
            df = df_raw.copy()
            df.columns = df.columns.str.lower().str.strip()

            df["title"] = df["title"].fillna("").str.strip()
            df["description"] = df["description"].fillna("").str.strip()
            df["component"] = df["component"].fillna("Team").str.strip()
            df["version"] = df["version"].fillna("3.0").astype(str).str.strip()
            df["created_time"] = pd.to_datetime(df["created_time"], errors="coerce")
            df["created_time"] = df["created_time"].fillna(pd.Timestamp.now())
            df["created_time"] = df["created_time"].dt.strftime("%Y-%m-%dT%H:%M:%S")

            # Drop rows where both title and description are empty
            df = df[(df["title"] != "") | (df["description"] != "")].reset_index(
                drop=True
            )

            st.caption(f"{len(df)} valid rows after cleanup")

            if st.button("Run Batch Prediction", use_container_width=True):
                # ── Build BugData list ────────────────────────────────────────
                bugs = []
                for _, row in df.iterrows():
                    bug = BugData(
                        title=row["title"],
                        description=row["description"],
                        component=row["component"],
                        version=row["version"],
                        created_time=row["created_time"],
                    )
                    bugs.append(bug)

                with st.spinner(f"Running predictions on {len(bugs)} bugs..."):
                    results, elapsed_ms = predict_batch(bugs)

                # ── Build results dataframe ───────────────────────────────────
                df["predicted_label"] = [r.label for r in results]
                df["probability"] = [r.probability for r in results]
                df["threshold"] = [r.threshold for r in results]

                st.success(f"Done in {elapsed_ms} ms")

                # ── Summary metrics ───────────────────────────────────────────
                total = len(results)
                n_high = sum(1 for r in results if r.label == "High Priority")
                n_low = total - n_high

                col1, col2, col3 = st.columns(3)
                col1.metric("Total Bugs", total)
                col2.metric("High Priority", n_high)
                col3.metric("Low Priority", n_low)

                # ── Accuracy vs expected (if column exists) ───────────────────
                if "expected_label" in df.columns:
                    df["expected_label"] = df["expected_label"].str.strip()
                    true_high = df[df["expected_label"] == "High Priority"]
                    correct_high = (
                        true_high["predicted_label"] == "High Priority"
                    ).sum()
                    recall = (
                        round(correct_high / len(true_high) * 100, 2)
                        if len(true_high) > 0
                        else 0.0
                    )
                    st.metric(
                        "Recall (High Priority)",
                        f"{recall}%",
                        help=f"{correct_high}/{len(true_high)} High Priority bugs correctly caught",
                    )

                # ── Results table ─────────────────────────────────────────────
                st.subheader("Results")
                display_cols = [
                    "title",
                    "component",
                    "version",
                    "predicted_label",
                    "probability",
                ]
                if "expected_label" in df.columns:
                    display_cols.insert(4, "expected_label")

                st.dataframe(
                    df[display_cols].style.apply(
                        lambda col: (
                            [
                                "background-color: #ffcccc"
                                if v == "High Priority"
                                else "background-color: #ccffcc"
                                for v in col
                            ]
                            if col.name == "predicted_label"
                            else [""] * len(col)
                        ),
                        axis=0,
                    ),
                    use_container_width=True,
                )

                # ── Download ──────────────────────────────────────────────────
                st.download_button(
                    label="Download Results CSV",
                    data=df.to_csv(index=False),
                    file_name="predictions.csv",
                    mime="text/csv",
                    use_container_width=True,
                )
