---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:6000
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: extra separator in progress status item there is an extra separator
    between the drag handle and the progress region in the status bar this should
    be removed
  sentences:
  - cell editors comboboxcelleditor and dialogcelleditor need code changed in createcontrol
    comboboxcelleditor and dialogcelleditor needs the following piece of code changed
    in createcontrol combobox addselectionlistener new selectionadapter public void
    widgetdefaultselected selectionevent event must set the selection before getting
    value selection combobox getselectionindex object newvalue dogetvalue boolean
    newvalidstate iscorrect if dosetvalue else try to insert the current value into
    the error message seterrormessage messageformat format geterrormessage new object
    items selection fireapplyeditorvalue the fireapplyeditorvalue must be preceeded
    by valuechanged oldvalidstate newvalidstate as in textcelleditor if this isnt
    done then the validity flag is never properly set nor reset nor is the error message
    updated these are all done by the valuechanged method because of this if the value
    ever goes invalid due to a validator which can decide what is valid beyond the
    simple list used by the dropdown it can never be changed to valid and so the value
    will never be updated correctly by the user of the cell editor notes defect text
    from rich kulp rg the comment in icelleditorlistener editorvaluechanged indicates
    that this notification is normally sent only by text based editors in response
    to a keystroke i suppose the thinking was that combo box and dialog editors would
    constrain the choices to valid values however it may be worth considering this
    change since configuring the cell editor with a validator is a way of avoiding
    subclassing
  - errorhandling statushandling statusgenerator does not test editor with init exceptions
    correctly build i20071211 0010 please see bug 204106 comment 5
  - offer last scope also forjava search 3 2 m5 either remove last scope again or
    allign ctrl shift g from java search i e also search in last scope instead of
    workspace see also bug 128505
- source_sentence: aioobe when changing install location version 3 3 0 build id i20070323
    1616 sun jre 1 6 0 02 ea scenario installing europa on top 3 3 m6 help software
    updates find and install search for new features select europa discovery site
    and click the finish button select an update site click ok the search result dialog
    opens select europa discovery site in the check box tree root item due to bugs
    182548 182549 and 182550 the dialog is in error and the next button is diabled
    deselect the corona soa and buckminster in error features click next accept the
    license agreements and click next on the displayed installation page select all
    features and click the change location button add a new location and click ok
    though no error msg displayed and new location is taken into account an aioobe
    occured and is visible both in the ms dos console and the error log view to be
    attached files
  sentences:
  - preferences losing preferences in workbench build id 200410050800 with this build
    i keep losing preference settings when restarting eclipse example preferences
    which are lost the welcome page is shown every time workbench keys modify active
    configuration my emacs bindings are always reset to default workbench appearence
    show text on perspective bar always reset to true nothing in the log
  - invoking all integrated external tool builder since my last update of eclipse
    with the eclipse internal refresh update when i run a project it takes much longer
    to start because a dialog appears that runs all tool builders of all open projects
    in former times it only invoked the tool builder of the project that i started
    this can take about 10 seconds if you have several projects oben and as you work
    on several projects you dont want to open close each project if you have to adjust
    something
  - changetoperspectivemenu leaks the changetoperspectivemenu is not being disposed
    to recreate take the f1 build in the shortcut bar bring up the changetoperspectivemenu
    from a memory profiler new instances of this menu are being created every time
    and not being released nick this problem has been here for a while recall our
    discussion about disposing popup menus and the different swt behavior between
    win and motif when ie one platform returns immediately while the other call waits
    until the menu has been processed
- source_sentence: key bindings emacs alt accelerators display in menu with esc build
    gm6 for any action that is bound to an accelerator with an alt key we also provide
    a binding using the esc key when the action is displayed in the menu both of the
    accelerators are shown see file print only the alt accelerator needs to be shown
    since the esc accelerator should be implied
  sentences:
  - help help contents does not use workbench preferences when you open the help perspective
    from the menu bar help help contents it does not use the preferences set up for
    the workbench open a new perspective the workbench preferences allows me to say
    that all new perspectives should be opened in a new window this is used so that
    i can view multiple things at ths same time however since the help menu item doesnt
    use this i cant have help up and also see what im working on at the same time
    there is a workaround and that is to open the help perspective in a different
    way that is to click on the open perspective icon or do perspective open other
    help anytime a perspective is opened it should use the preferences
  - api issue breadth vs depth resource accessing the vcm api supports the query and
    retrieval of resources in a breadth first style that is to find a member of a
    project directory we must retrieve all members furthermore loading of resources
    must start at a root and include all children of that root there is no api to
    directly support query and retrieval given a resource path unless the parent resources
    already exist in the eclipse workspace this type of api would be helpfull in supporting
    the partial loads required for our initial method of loading cvs modules without
    such an api we need to make assumptions about how vcm would create the parent
    project and folders when loading child resources which is dangerous notes
  - members view is broken in m3 the members view in eclipse 3 0 m3 is broken when
    you click a method in members view pane it shows the method body correctly in
    the editor however the rest of the class desappears and the only way to view it
    again is to re open the class i dont know if it is really a bug or a new feature
    in m3 but i think at least the plataform should give an option to the user to
    have this functionality enabled or not
- source_sentence: file ascii binary type guessing eclipse should provide an algorithm
    similar to the one provided by wincvs that examining files contents tries to guess
    the ascii or binary file type when sharing a project or adding new resources to
    repository this should work for those files whose extensions are not mapped in
    the well known ones
  sentences:
  - toggle mark occurrence short key is invalid sometime toggle mark occurrence short
    key alt shift o is invalid in one editor window the shout key is ok but when i
    switch another editor windonw it broke windows 2000 professional 1 7g 512m jdk1
    5
  - workingsets working set selection wizard page has faulty layout the layout for
    the working set type label of the new edit workingsettypepage wizard page is not
    correct if you select a type then go back you will see the labels layout is grabbing
    excess vertical space when it shouldnt be i have a patch to fix this
  - javax net is not recognized my code is using the javax net ssl httpsurlconnection
    class but unfortunately it is not recognized the editor marks it with red underline
    and the program refuses to run saying could not find the main class programm will
    exit if i change the code to be exactly the same but use java net httpurlconnection
    instead non ssl all works fine the javax net was introduced in 1 4 but the problem
    appears when eclipse is using either jdk1 4 2 and 1 5 in eclipse 3 0 and 3 0 1
    i did make sure the jdk compliance is set to 1 4 window prefs java compiler compliance
    if i compile the code manually outside the eclipse there is no problem at all
    compiles successfuly and runs javac exe g target 1 4 source 1 4 deprecation d
    bin sourcepath src src java calling to javap javax net ssl httpsurlconnection
    is successful so it seem that there is no problem with the jdk itself the severity
    is major since the ide cannot be used meanwhile i use netbeans ide and no problems
    there
- source_sentence: workingsets deadlock on each startup caused by abstractworkingsetmanager
    i20051129 0800 i always get a deadlock caused by abstractworkingsetmanager when
    starting an existing workspace full thread dump java hotspot client vm 1 5 0 05
    b03 mixed mode java indexing daemon prio 4 tid 0x02e3f338 nid 0x28c in object
    wait 0x0492f000 0x0492fb68 at java lang object wait native method waiting on 0x12dd1b00
    a org eclipse jdt internal core search indexing indexmanager at java lang object
    wait object java 474 at org eclipse jdt internal core search processing jobmanager
    run jobmanager java 349 locked 0x12dd1b00 a org eclipse jdt internal core search
    indexing indexmanager at java lang thread run thread java 595 worker 3 daemon
    prio 5 tid 0x03907ca0 nid 0x948 in object wait 0x03d8f000 0x03d8fbe8 at java lang
    object wait native method waiting on 0x11b4ff60 a org eclipse core internal jobs
    workerpool at org eclipse core internal jobs workerpool sleep workerpool java
    173 locked 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse
    core internal jobs workerpool startjob workerpool java 205 at org eclipse core
    internal jobs worker run worker java 51 worker 2 daemon prio 5 tid 0x0377d0a8
    nid 0x11e0 in object wait 0x03d4f000 0x03d4fc68 at java lang object wait native
    method waiting on 0x11b4ff60 a org eclipse core internal jobs workerpool at org
    eclipse core internal jobs workerpool sleep workerpool java 173 locked 0x11b4ff60
    a org eclipse core internal jobs workerpool at org eclipse core internal jobs
    workerpool startjob workerpool java 205 at org eclipse core internal jobs worker
    run worker java 51 worker 1 daemon prio 5 tid 0x0371f570 nid 0x988 in object wait
    0x0350f000 0x0350fce8 at java lang object wait native method waiting on 0x11b4ff60
    a org eclipse core internal jobs workerpool at org eclipse core internal jobs
    workerpool sleep workerpool java 173 locked 0x11b4ff60 a org eclipse core internal
    jobs workerpool at org eclipse core internal jobs workerpool startjob workerpool
    java 205 at org eclipse core internal jobs worker run worker java 51 worker 0
    daemon prio 5 tid 0x036d4408 nid 0x1430 in object wait 0x034cf000 0x034cfd68 at
    java lang object wait native method waiting on 0x11b4ff60 a org eclipse core internal
    jobs workerpool at org eclipse core internal jobs workerpool sleep workerpool
    java 173 locked 0x11b4ff60 a org eclipse core internal jobs workerpool at org
    eclipse core internal jobs workerpool startjob workerpool java 205 at org eclipse
    core internal jobs worker run worker java 51 start level event dispatcher daemon
    prio 5 tid 0x02dc7870 nid 0x1428 in object wait 0x0344f000 0x0344fae8 at java
    lang object wait native method waiting on 0x11b364a8 a org eclipse osgi framework
    eventmgr eventmanager eventthread at java lang object wait object java 474 at
    org eclipse osgi framework eventmgr eventmanager eventthread getnextevent eventmanager
    java 349 locked 0x11b364a8 a org eclipse osgi framework eventmgr eventmanager
    eventthread at org eclipse osgi framework eventmgr eventmanager eventthread run
    eventmanager java 287 state saver prio 5 tid 0x02dc57b0 nid 0xea4 in object wait
    0x0340f000 0x0340fb68 at java lang object wait native method waiting on 0x11b365f8
    a org eclipse osgi internal resolver systemstate at org eclipse core runtime adaptor
    eclipseadaptor statesaver run eclipseadaptor java 929 locked 0x11b365f8 a org
    eclipse osgi internal resolver systemstate at java lang thread run thread java
    595 framework event dispatcher daemon prio 5 tid 0x02dd8560 nid 0xa80 in object
    wait 0x033cf000 0x033cfbe8 at java lang object wait native method waiting on 0x13113e28
    a org eclipse swt widgets runnablelock at java lang object wait object java 474
    at org eclipse swt widgets synchronizer syncexec synchronizer java 169 locked
    0x13113e28 a org eclipse swt widgets runnablelock at org eclipse ui internal uisynchronizer
    syncexec uisynchronizer java 28 at org eclipse swt widgets display syncexec display
    java 3656 at org eclipse ui internal abstractworkingsetmanager firepropertychange
    abstractworkingsetmanager java 301 at org eclipse ui internal abstractworkingsetmanager
    getupdater abstractworkingsetmanager java 585 at org eclipse ui internal abstractworkingsetmanager
    bundlechanged abstractworkingsetmanager java 546 locked 0x12d83968 a org eclipse
    ui internal workingsetmanager at org eclipse osgi framework internal core bundlecontextimpl
    dispatchevent bundlecontextimpl java 1205 at org eclipse osgi framework eventmgr
    eventmanager dispatchevent eventmanager java 189 at org eclipse osgi framework
    eventmgr eventmanager eventthread run eventmanager java 291 low memory detector
    daemon prio 5 tid 0x00a92fd0 nid 0x1768 runnable 0x00000000 0x00000000 compilerthread0
    daemon prio 10 tid 0x00a91ba8 nid 0xe6c waiting on condition 0x00000000 0x02d0f6cc
    signal dispatcher daemon prio 10 tid 0x00a90f98 nid 0xe1c waiting on condition
    0x00000000 0x00000000 finalizer daemon prio 9 tid 0x00a48850 nid 0x1774 in object
    wait 0x02c8f000 0x02c8fa68 at java lang object wait native method waiting on 0x11af0310
    a java lang ref referencequeue lock at java lang ref referencequeue remove referencequeue
    java 116 locked 0x11af0310 a java lang ref referencequeue lock at java lang ref
    referencequeue remove referencequeue java 132 at java lang ref finalizer finalizerthread
    run finalizer java 159 reference handler daemon prio 10 tid 0x00a87b58 nid 0x15c0
    in object wait 0x02c4f000 0x02c4fae8 at java lang object wait native method waiting
    on 0x11af0070 a java lang ref reference lock at java lang object wait object java
    474 at java lang ref reference referencehandler run reference java 116 locked
    0x11af0070 a java lang ref reference lock main prio 7 tid 0x00036d78 nid 0xd50
    waiting for monitor entry 0x0007e000 0x0007fc3c at org eclipse core commands common
    eventmanager addlistenerobject eventmanager java 56 waiting to lock 0x12d83968
    a org eclipse ui internal workingsetmanager at org eclipse ui internal abstractworkingsetmanager
    addpropertychangelistener abstractworkingsetmanager java 272 at org eclipse jdt
    internal ui workingsets workingsetfilteractiongroup init workingsetfilteractiongroup
    java 89 at org eclipse jdt internal ui browsing javabrowsingpart createactions
    javabrowsingpart java 578 at org eclipse jdt internal ui browsing packagesview
    createactions packagesview java 426 at org eclipse jdt internal ui browsing javabrowsingpart
    createpartcontrol javabrowsingpart java 352 at org eclipse ui internal viewreference
    createparthelper viewreference java 305 at org eclipse ui internal viewreference
    createpart viewreference java 180 at org eclipse ui internal workbenchpartreference
    getpart workbenchpartreference java 552 at org eclipse ui internal partpane setvisible
    partpane java 285 at org eclipse ui internal viewpane setvisible viewpane java
    503 at org eclipse ui internal presentations presentablepart setvisible presentablepart
    java 140 at org eclipse ui internal presentations util presentablepartfolder select
    presentablepartfolder java 263 at org eclipse ui internal presentations util lefttorighttaborder
    select lefttorighttaborder java 65 at org eclipse ui internal presentations util
    tabbedstackpresentation selectpart tabbedstackpresentation java 394 at org eclipse
    ui internal partstack refreshpresentationselection partstack java 1140 at org
    eclipse ui internal partstack createcontrol partstack java 621 at org eclipse
    ui internal partstack createcontrol partstack java 530 at org eclipse ui internal
    partsashcontainer createcontrol partsashcontainer java 557 at org eclipse ui internal
    perspectivehelper activate perspectivehelper java 227 at org eclipse ui internal
    perspective onactivate perspective java 813 at org eclipse ui internal workbenchpage
    onactivate workbenchpage java 2217 at org eclipse ui internal workbenchwindow
    6 run workbenchwindow java 2461 at org eclipse swt custom busyindicator showwhile
    busyindicator java 69 at org eclipse ui internal workbenchwindow setactivepage
    workbenchwindow java 2443 at org eclipse ui internal workbenchwindow restorestate
    workbenchwindow java 1893 at org eclipse ui internal workbench dorestorestate
    workbench java 2644 at org eclipse ui internal workbench access 14 workbench java
    2593 at org eclipse ui internal workbench 17 run workbench java 1542 at org eclipse
    ui internal workbench runstartupwithprogress workbench java 1287 at org eclipse
    ui internal workbench restorestate workbench java 1540 at org eclipse ui internal
    workbench access 12 workbench java 1519 at org eclipse ui internal workbench 15
    run workbench java 1402 at org eclipse core runtime saferunner run saferunner
    java 37 at org eclipse core runtime platform run platform java 785 at org eclipse
    ui internal workbench restorestate workbench java 1346 at org eclipse ui internal
    workbenchconfigurer restorestate workbenchconfigurer java 183 at org eclipse ui
    application workbenchadvisor openwindows workbenchadvisor java 700 at org eclipse
    ui internal workbench init workbench java 1074 at org eclipse ui internal workbench
    runui workbench java 1696 at org eclipse ui internal workbench createandrunworkbench
    workbench java 396 at org eclipse ui platformui createandrunworkbench platformui
    java 143 at org eclipse ui internal ide ideapplication run ideapplication java
    106 at org eclipse core internal runtime platformactivator 1 run platformactivator
    java 109 at org eclipse core runtime internal adaptor eclipseapplauncher runapplication
    eclipseapplauncher java 92 at org eclipse core runtime internal adaptor eclipseapplauncher
    start eclipseapplauncher java 68 at org eclipse core runtime adaptor eclipsestarter
    run eclipsestarter java 369 at org eclipse core runtime adaptor eclipsestarter
    run eclipsestarter java 167 at sun reflect nativemethodaccessorimpl invoke0 native
    method at sun reflect nativemethodaccessorimpl invoke nativemethodaccessorimpl
    java 39 at sun reflect delegatingmethodaccessorimpl invoke delegatingmethodaccessorimpl
    java 25 at java lang reflect method invoke method java 585 at org eclipse core
    launcher main invokeframework main java 338 at org eclipse core launcher main
    basicrun main java 282 at org eclipse core launcher main run main java 977 at
    org eclipse core launcher main main main java 952 vm thread prio 10 tid 0x0003f2a0
    nid 0x9dc runnable vm periodic task thread prio 10 tid 0x00a8f3d0 nid 0xeec waiting
    on condition
  sentences:
  - feature request mapping files in the build process like working sets but not only
    providing a view on files it could be helpful if it would be possible to specify
    files which should be processed copied or not during the build process the proper
    way to do so would be in the properties dialog of a project tree node java build
    path maybe a new tab build properties this would also be a good place for a relocated
    build output folder attribute and its browse button instead of the actual location
    below every tab on this dialog regards mark evertz
  - viewers adding many adjacent children to a treeviewer is slow this is on 3 1m5a
    gtk2 build if you add several thousand children to a tree it can take several
    minutes to complete a concrete example is browsing a cvs repository containing
    thousands of directories e g cvs fedora redhat com cvs dist if you browse through
    that repo the ui becomes unresponsive for several minutes while the tree is updated
    this is unacceptable adding n children to a tree node is currently an o n 2 operation
    at least on gtk2 i havent checked other platforms this is because for every child
    an o read of all the children on that node and an o linear search to check for
    duplicates is performed the attached patch reduces the add n children cost to
    o n log n which in practice means that for my cvs repo test case the ui only takes
    a few seconds to update instead of several minutes but only in the case of sorted
    trees by doing two things 1 abstracttreeviewer indexforelement now requests only
    the children that are actually needed in its binary search rather than requesting
    all the children of the current node 2 this optimisation is only performed for
    sorted trees in abstracttreeviewer createaddedelement given that we now know the
    index where we need to insert the new item and given the reasonable assumption
    which needs to be explicitly required in the javadoc that the sorter is consistent
    with equals we dont have to search through all the children to find possible duplicates
    we need only look at the item prior to that index if the index is positive if
    the index is 0 we know it is not a duplicate because of the algorithm used in
    indexforelement no new fields have been added but some new public methods have
    been added unfortunately because it straddles the platform specific interface
    if this patch were accepted it would need to be implemented for every platform
    and my patch only implements the gtk2 part of it because i dont develop on windows
  - dialogs open type dialog type filtering is not working i20040317 open the open
    type dialog ctrl shift t type throwa the displayed matching types are throwable
    undeclaredthrowableexception compilationuniteditor compilationuniteditoractioncontributor
    x xbitmap x xpixmap
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'workingsets deadlock on each startup caused by abstractworkingsetmanager i20051129 0800 i always get a deadlock caused by abstractworkingsetmanager when starting an existing workspace full thread dump java hotspot client vm 1 5 0 05 b03 mixed mode java indexing daemon prio 4 tid 0x02e3f338 nid 0x28c in object wait 0x0492f000 0x0492fb68 at java lang object wait native method waiting on 0x12dd1b00 a org eclipse jdt internal core search indexing indexmanager at java lang object wait object java 474 at org eclipse jdt internal core search processing jobmanager run jobmanager java 349 locked 0x12dd1b00 a org eclipse jdt internal core search indexing indexmanager at java lang thread run thread java 595 worker 3 daemon prio 5 tid 0x03907ca0 nid 0x948 in object wait 0x03d8f000 0x03d8fbe8 at java lang object wait native method waiting on 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse core internal jobs workerpool sleep workerpool java 173 locked 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse core internal jobs workerpool startjob workerpool java 205 at org eclipse core internal jobs worker run worker java 51 worker 2 daemon prio 5 tid 0x0377d0a8 nid 0x11e0 in object wait 0x03d4f000 0x03d4fc68 at java lang object wait native method waiting on 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse core internal jobs workerpool sleep workerpool java 173 locked 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse core internal jobs workerpool startjob workerpool java 205 at org eclipse core internal jobs worker run worker java 51 worker 1 daemon prio 5 tid 0x0371f570 nid 0x988 in object wait 0x0350f000 0x0350fce8 at java lang object wait native method waiting on 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse core internal jobs workerpool sleep workerpool java 173 locked 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse core internal jobs workerpool startjob workerpool java 205 at org eclipse core internal jobs worker run worker java 51 worker 0 daemon prio 5 tid 0x036d4408 nid 0x1430 in object wait 0x034cf000 0x034cfd68 at java lang object wait native method waiting on 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse core internal jobs workerpool sleep workerpool java 173 locked 0x11b4ff60 a org eclipse core internal jobs workerpool at org eclipse core internal jobs workerpool startjob workerpool java 205 at org eclipse core internal jobs worker run worker java 51 start level event dispatcher daemon prio 5 tid 0x02dc7870 nid 0x1428 in object wait 0x0344f000 0x0344fae8 at java lang object wait native method waiting on 0x11b364a8 a org eclipse osgi framework eventmgr eventmanager eventthread at java lang object wait object java 474 at org eclipse osgi framework eventmgr eventmanager eventthread getnextevent eventmanager java 349 locked 0x11b364a8 a org eclipse osgi framework eventmgr eventmanager eventthread at org eclipse osgi framework eventmgr eventmanager eventthread run eventmanager java 287 state saver prio 5 tid 0x02dc57b0 nid 0xea4 in object wait 0x0340f000 0x0340fb68 at java lang object wait native method waiting on 0x11b365f8 a org eclipse osgi internal resolver systemstate at org eclipse core runtime adaptor eclipseadaptor statesaver run eclipseadaptor java 929 locked 0x11b365f8 a org eclipse osgi internal resolver systemstate at java lang thread run thread java 595 framework event dispatcher daemon prio 5 tid 0x02dd8560 nid 0xa80 in object wait 0x033cf000 0x033cfbe8 at java lang object wait native method waiting on 0x13113e28 a org eclipse swt widgets runnablelock at java lang object wait object java 474 at org eclipse swt widgets synchronizer syncexec synchronizer java 169 locked 0x13113e28 a org eclipse swt widgets runnablelock at org eclipse ui internal uisynchronizer syncexec uisynchronizer java 28 at org eclipse swt widgets display syncexec display java 3656 at org eclipse ui internal abstractworkingsetmanager firepropertychange abstractworkingsetmanager java 301 at org eclipse ui internal abstractworkingsetmanager getupdater abstractworkingsetmanager java 585 at org eclipse ui internal abstractworkingsetmanager bundlechanged abstractworkingsetmanager java 546 locked 0x12d83968 a org eclipse ui internal workingsetmanager at org eclipse osgi framework internal core bundlecontextimpl dispatchevent bundlecontextimpl java 1205 at org eclipse osgi framework eventmgr eventmanager dispatchevent eventmanager java 189 at org eclipse osgi framework eventmgr eventmanager eventthread run eventmanager java 291 low memory detector daemon prio 5 tid 0x00a92fd0 nid 0x1768 runnable 0x00000000 0x00000000 compilerthread0 daemon prio 10 tid 0x00a91ba8 nid 0xe6c waiting on condition 0x00000000 0x02d0f6cc signal dispatcher daemon prio 10 tid 0x00a90f98 nid 0xe1c waiting on condition 0x00000000 0x00000000 finalizer daemon prio 9 tid 0x00a48850 nid 0x1774 in object wait 0x02c8f000 0x02c8fa68 at java lang object wait native method waiting on 0x11af0310 a java lang ref referencequeue lock at java lang ref referencequeue remove referencequeue java 116 locked 0x11af0310 a java lang ref referencequeue lock at java lang ref referencequeue remove referencequeue java 132 at java lang ref finalizer finalizerthread run finalizer java 159 reference handler daemon prio 10 tid 0x00a87b58 nid 0x15c0 in object wait 0x02c4f000 0x02c4fae8 at java lang object wait native method waiting on 0x11af0070 a java lang ref reference lock at java lang object wait object java 474 at java lang ref reference referencehandler run reference java 116 locked 0x11af0070 a java lang ref reference lock main prio 7 tid 0x00036d78 nid 0xd50 waiting for monitor entry 0x0007e000 0x0007fc3c at org eclipse core commands common eventmanager addlistenerobject eventmanager java 56 waiting to lock 0x12d83968 a org eclipse ui internal workingsetmanager at org eclipse ui internal abstractworkingsetmanager addpropertychangelistener abstractworkingsetmanager java 272 at org eclipse jdt internal ui workingsets workingsetfilteractiongroup init workingsetfilteractiongroup java 89 at org eclipse jdt internal ui browsing javabrowsingpart createactions javabrowsingpart java 578 at org eclipse jdt internal ui browsing packagesview createactions packagesview java 426 at org eclipse jdt internal ui browsing javabrowsingpart createpartcontrol javabrowsingpart java 352 at org eclipse ui internal viewreference createparthelper viewreference java 305 at org eclipse ui internal viewreference createpart viewreference java 180 at org eclipse ui internal workbenchpartreference getpart workbenchpartreference java 552 at org eclipse ui internal partpane setvisible partpane java 285 at org eclipse ui internal viewpane setvisible viewpane java 503 at org eclipse ui internal presentations presentablepart setvisible presentablepart java 140 at org eclipse ui internal presentations util presentablepartfolder select presentablepartfolder java 263 at org eclipse ui internal presentations util lefttorighttaborder select lefttorighttaborder java 65 at org eclipse ui internal presentations util tabbedstackpresentation selectpart tabbedstackpresentation java 394 at org eclipse ui internal partstack refreshpresentationselection partstack java 1140 at org eclipse ui internal partstack createcontrol partstack java 621 at org eclipse ui internal partstack createcontrol partstack java 530 at org eclipse ui internal partsashcontainer createcontrol partsashcontainer java 557 at org eclipse ui internal perspectivehelper activate perspectivehelper java 227 at org eclipse ui internal perspective onactivate perspective java 813 at org eclipse ui internal workbenchpage onactivate workbenchpage java 2217 at org eclipse ui internal workbenchwindow 6 run workbenchwindow java 2461 at org eclipse swt custom busyindicator showwhile busyindicator java 69 at org eclipse ui internal workbenchwindow setactivepage workbenchwindow java 2443 at org eclipse ui internal workbenchwindow restorestate workbenchwindow java 1893 at org eclipse ui internal workbench dorestorestate workbench java 2644 at org eclipse ui internal workbench access 14 workbench java 2593 at org eclipse ui internal workbench 17 run workbench java 1542 at org eclipse ui internal workbench runstartupwithprogress workbench java 1287 at org eclipse ui internal workbench restorestate workbench java 1540 at org eclipse ui internal workbench access 12 workbench java 1519 at org eclipse ui internal workbench 15 run workbench java 1402 at org eclipse core runtime saferunner run saferunner java 37 at org eclipse core runtime platform run platform java 785 at org eclipse ui internal workbench restorestate workbench java 1346 at org eclipse ui internal workbenchconfigurer restorestate workbenchconfigurer java 183 at org eclipse ui application workbenchadvisor openwindows workbenchadvisor java 700 at org eclipse ui internal workbench init workbench java 1074 at org eclipse ui internal workbench runui workbench java 1696 at org eclipse ui internal workbench createandrunworkbench workbench java 396 at org eclipse ui platformui createandrunworkbench platformui java 143 at org eclipse ui internal ide ideapplication run ideapplication java 106 at org eclipse core internal runtime platformactivator 1 run platformactivator java 109 at org eclipse core runtime internal adaptor eclipseapplauncher runapplication eclipseapplauncher java 92 at org eclipse core runtime internal adaptor eclipseapplauncher start eclipseapplauncher java 68 at org eclipse core runtime adaptor eclipsestarter run eclipsestarter java 369 at org eclipse core runtime adaptor eclipsestarter run eclipsestarter java 167 at sun reflect nativemethodaccessorimpl invoke0 native method at sun reflect nativemethodaccessorimpl invoke nativemethodaccessorimpl java 39 at sun reflect delegatingmethodaccessorimpl invoke delegatingmethodaccessorimpl java 25 at java lang reflect method invoke method java 585 at org eclipse core launcher main invokeframework main java 338 at org eclipse core launcher main basicrun main java 282 at org eclipse core launcher main run main java 977 at org eclipse core launcher main main main java 952 vm thread prio 10 tid 0x0003f2a0 nid 0x9dc runnable vm periodic task thread prio 10 tid 0x00a8f3d0 nid 0xeec waiting on condition',
    'viewers adding many adjacent children to a treeviewer is slow this is on 3 1m5a gtk2 build if you add several thousand children to a tree it can take several minutes to complete a concrete example is browsing a cvs repository containing thousands of directories e g cvs fedora redhat com cvs dist if you browse through that repo the ui becomes unresponsive for several minutes while the tree is updated this is unacceptable adding n children to a tree node is currently an o n 2 operation at least on gtk2 i havent checked other platforms this is because for every child an o read of all the children on that node and an o linear search to check for duplicates is performed the attached patch reduces the add n children cost to o n log n which in practice means that for my cvs repo test case the ui only takes a few seconds to update instead of several minutes but only in the case of sorted trees by doing two things 1 abstracttreeviewer indexforelement now requests only the children that are actually needed in its binary search rather than requesting all the children of the current node 2 this optimisation is only performed for sorted trees in abstracttreeviewer createaddedelement given that we now know the index where we need to insert the new item and given the reasonable assumption which needs to be explicitly required in the javadoc that the sorter is consistent with equals we dont have to search through all the children to find possible duplicates we need only look at the item prior to that index if the index is positive if the index is 0 we know it is not a duplicate because of the algorithm used in indexforelement no new fields have been added but some new public methods have been added unfortunately because it straddles the platform specific interface if this patch were accepted it would need to be implemented for every platform and my patch only implements the gtk2 part of it because i dont develop on windows',
    'feature request mapping files in the build process like working sets but not only providing a view on files it could be helpful if it would be possible to specify files which should be processed copied or not during the build process the proper way to do so would be in the properties dialog of a project tree node java build path maybe a new tab build properties this would also be a good place for a relocated build output folder attribute and its browse button instead of the actual location below every tab on this dialog regards mark evertz',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6945, 0.7193],
#         [0.6945, 1.0000, 0.6934],
#         [0.7193, 0.6934, 1.0000]])
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 6,000 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                          | label                                                          |
  |:--------|:-----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                             | string                                                                              | float                                                          |
  | details | <ul><li>min: 8 tokens</li><li>mean: 125.4 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 120.59 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.67</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | label            |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>deadlock when importing a project this deadlock happens when you import a java project that has classpath problems it is hard to reproduce since it apparently depends on timimg of different events the threads participating in the deadlock thread worker 7 object wait line not available native method semaphore acquire line 38 orderedlock doacquire semaphore long line 166 orderedlock acquire line 102 orderedlock acquire line 79 workmanager checkin ischedulingrule iprogressmonitor line 96 workspace prepareoperation ischedulingrule iprogressmonitor line 1628 project createmarker line 626 javaproject createclasspathproblemmarker line 707 javaproject getresolvedclasspath iclasspathentry ipath boolean boolean map line 1862 deltaprocessingstate projectupdateinfo updateprojectreferencesifnecessar y line 98 deltaprocessor resourcechanged line 1866 deltaprocessingstate resourcechanged line 414 notificationmanager 2 run line 283 internalplatform run line 616 platform run line 747 notificationmanage...</code> | <code>laying down features and fragments cause fragments to activate immediately steps 1 take a wswb win32 drop im betting this works for vanilla eclipse too from the ftp server at ott4f inet eams wswb anon out 2 0 2 stream wswb m20021025 200210251102 2 unzip and start exit immediately 3 take a language pack 1 feature from ott4f inet eams wswb anon out nlfeature 4 unzip the file over your wswb install contains a features and a plugins directory 5 make sure you are in a different locale 6 start wswb notice that the wswb starts up translated in your local and asks you in the locale language if you want to install the feature however the fact that everything is translated proves the feature is already active quiting the feature install leaves the language pack active</code>                                                                                                                                                                                                                                            | <code>1.0</code> |
  | <code>coolbar workbench toolbar flash selecting stack frames i20040324 debug to a breakpoint close all of the open editors reselect the top stack frame opens java editor select another stack frame that will open a different editor classfile editor but the reuse editor when displaying source code preference is enabled so the java editor is replaced move back and forth between these two stack frames all of the eclipse toolbar icons flash for each stack frame selection outside of debugging if i close the last editor you can see a brief flash of the toolbar icons michael has this been seen in any other context</code>                                                                                                                                                                                                                                                                                                                                                                                                             | <code>cant restart eclipse after upgrading to build 20021216 build id 200212160800 had not get a new version of eclipse for a couple of weeks got new build run on top on my workspace an got the following in the log file delete the config directory and it restarted going to attach the config dir i have my 100mg bytes workspace zipped if you need log file session dec 16 2002 10 24 57 312 java version 1 3 1 03 java vendor sun microsystems inc bootloader constants os win32 arch x86 ws win32 nl en us command line arguments os win32 ws win32 arch x86 data d eduardo desktop workbenchs ws dev21 plugins dev bin update debug consolelog install file d eduardo desktop workbenchs eclipse dev21 entry org eclipse core resources 1 1 dec 16 2002 10 24 57 312 message could not load library core 2 0 5 dll this library provides platform specific optimizations for certain file system operations this library is not present on all platforms so this may not be an error the resources plugin will safely fall back to ...</code> | <code>1.0</code> |
  | <code>cvs timeout v 20020604 when i try to access a cvs repository in eclipse the repository appears in the exploring perspective with branches head and versions however when i try to expand head a eclipse hangs for a while a minute it looks like its blocking on the cvs connection b after the wait it returns with interrupted timeout while closing output stream the cvs server logs connection made at the beginning and then cvs root this does not happen on the windows box ive also got running the same release</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | <code>platform new and noteworthy glitches i20070608 1718 org eclipse platform doc user whatsnew platform whatsnew html hiding the window toolbar you can now hide the window toolbar by clicking window hide toolbar not true in i20070608 1718 i can only hide from the context menu and only restore from the window menu see also bug 182113 history view search should explain that search field must be enabled in the view menu screenshot should better show the view menu as well with show search field checked and selected</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | <code>1.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 32
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 5e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: trackio
- `eval_strategy`: no
- `per_device_eval_batch_size`: 32
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `warmup_ratio`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 2.6596 | 500  | 0.2359        |


### Framework Versions
- Python: 3.13.11
- Sentence Transformers: 5.3.0
- Transformers: 5.3.0
- PyTorch: 2.10.0+cu130
- Accelerate: 1.13.0
- Datasets: 4.7.0
- Tokenizers: 0.22.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->