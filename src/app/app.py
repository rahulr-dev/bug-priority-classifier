import streamlit as st
import pandas as pd
import datetime
import sys
import os
import shap
from streamlit_shap import st_shap

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.models.BugData import BugData
from src.utils.inference import predict, predict_batch

# ── Configuration ────────────────────────────────────────────────────────────
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ARTIFACT_DIR = os.path.join(PROJECT_ROOT, "artifacts")

st.set_page_config(page_title="Bug Priority AI", page_icon="🛡️", layout="wide")

# ── Header ───────────────────────────────────────────────────────────────────
st.title("🛡️ Dynamic Bug Prioritization System")
st.caption("Cost-Sensitive Classification for Eclipse Bug Reports")

tab2, tab3 = st.tabs(["📊 Batch", "🔬 Research"])

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

# with tab1:
#     col_in, col_out = st.columns([1, 1], gap="medium")

#     with col_in:
#         with st.form("predict_form"):
#             title = st.text_input("Title")
#             description = st.text_area("Description", height=150)
#             c1, c2 = st.columns(2)
#             comp = c1.selectbox(
#                 "Component", COMPONENTS, index=COMPONENTS.index("Runtime")
#             )
#             ver = c2.selectbox("Version", VERSIONS, index=VERSIONS.index("3.0"))
#             submitted = st.form_submit_button(
#                 "Classify", use_container_width=True, type="primary"
#             )

#     with col_out:
#         if submitted and title and description:
#             bug = BugData(
#                 title=title,
#                 description=description,
#                 component=comp,
#                 version=ver,
#                 created_time=datetime.datetime.now().isoformat(),
#             )
#             res, _, explanation = predict(bug)

#             if res.label == "High Priority":
#                 st.error(f"### {res.label}")
#             else:
#                 st.success(f"### {res.label}")

#             st.metric("Probability", f"{res.probability:.1%}")
#             st.caption(f"Decision Threshold: {res.threshold}")

#             # Explainable AI section
#             with st.expander("🔬 Explainable AI (SHAP)", expanded=True):
#                 st.write(
#                     "This chart shows how each feature influenced the AI's decision."
#                 )
#                 exp = shap.Explanation(
#                     values=explanation["shap_values"],
#                     base_values=explanation["base_value"],
#                     data=explanation["input_features"],
#                     feature_names=explanation["feature_names"],
#                 )
#                 st_shap(shap.plots.waterfall(exp, max_display=10))
#         else:
#             st.info("Awaiting input...")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2 — Batch Analysis
# ─────────────────────────────────────────────────────────────────────────────

with tab2:
    uploaded = st.file_uploader("Upload Bug CSV", type=["csv"])

    if uploaded:
        df = pd.read_csv(uploaded)
        df.columns = df.columns.str.lower().str.strip()

        if st.button("Process Batch", use_container_width=True, type="primary"):
            bugs = [
                BugData(
                    title=row.get("title", ""),
                    description=row.get("description", ""),
                    component=row.get("component", "Runtime"),
                    version=row.get("version", "3.0"),
                    created_time=row.get(
                        "created_time", datetime.datetime.now().isoformat()
                    ),
                )
                for _, row in df.iterrows()
            ]
            results, _ = predict_batch(bugs)

            df["predicted"] = [r.label for r in results]
            df["prob"] = [r.probability for r in results]

            c1, c2, c3 = st.columns(3)
            c1.metric("Total", len(df))
            c2.metric("High", sum(df["predicted"] == "High Priority"))
            c3.metric("Low", sum(df["predicted"] == "Low Priority"))

            # Business Impact
            with st.expander("ROI Analysis", expanded=True):
                ic1, ic2 = st.columns(2)
                c_fn = ic1.number_input("Cost of Missed High (hrs)", 10)
                c_fp = ic2.number_input("Cost of False Alarm (hrs)", 1)

                if "expected_label" in df.columns:
                    df["expected_label"] = df["expected_label"].str.strip()
                    fn = (
                        (df["expected_label"] == "High Priority")
                        & (df["predicted"] == "Low Priority")
                    ).sum()
                    fp = (
                        (df["expected_label"] == "Low Priority")
                        & (df["predicted"] == "High Priority")
                    ).sum()
                    tp = (
                        (df["expected_label"] == "High Priority")
                        & (df["predicted"] == "High Priority")
                    ).sum()

                    savings = (tp * c_fn) - (fp * c_fp)
                    st.metric("Net Productivity Gain", f"{round(savings, 1)} hrs")

            st.dataframe(
                df[["title", "predicted", "prob"]].style.apply(
                    lambda x: [
                        "background-color: #ffcccc" if v == "High Priority" else ""
                        for v in x
                    ],
                    subset=["predicted"],
                    axis=0,
                ),
                use_container_width=True,
            )

# ─────────────────────────────────────────────────────────────────────────────
# TAB 3 — Research
# ─────────────────────────────────────────────────────────────────────────────

with tab3:
    st.subheader("Mathematical Optimization")
    st.markdown(
        "We optimize the decision threshold to minimize total business cost ($Cost = 10 \cdot FN + 1 \cdot FP$)."
    )

    path = os.path.join(ARTIFACT_DIR, "cost_curve.png")
    if os.path.exists(path):
        st.image(path, use_container_width=True)

    st.divider()
    st.write(
        "**Stack:** XGBoost + Sentence Embeddings (SOTA mpnet) + FastAPI + Docker + SHAP Explainable AI"
    )
