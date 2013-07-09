import os
from __main__ import vtk, qt, ctk, slicer
import EditorLib
from EditorLib.EditOptions import HelpButton
from EditorLib.EditOptions import EditOptions
from EditorLib import EditUtil
from EditorLib import LabelEffect


class InteractiveConnectedComponentsUsingParzenPDFsOptions(EditorLib.LabelEffectOptions):
  """ Editor Effect gui
  """

  def __init__(self, parent=0):
    super(InteractiveConnectedComponentsUsingParzenPDFsOptions,self).__init__(parent)

    self.attributes = ('PaintTool')
    self.displayName = 'Interactive Connected Components using Parzen PDFs'
    self.undoRedo = EditorLib.EditUtil.UndoRedo()

    # Create the normal PDF segmenter node cli if it doesn't exists yet.
    # This is because we want the normal module's cli to be selected
    # when opening the cli module.
    module = slicer.modules.segmentconnectedcomponentsusingparzenpdfs
    self.getCLINode(module, module.title)

  def __del__(self):
    super(InteractiveConnectedComponentsUsingParzenPDFsOptions,self).__del__()

  def create(self):
    super(InteractiveConnectedComponentsUsingParzenPDFsOptions,self).create()

    ioCollapsibleButton = ctk.ctkCollapsibleButton()
    ioCollapsibleButton.text = "IO"
    ioCollapsibleButton.collapsed = 1
    self.frame.layout().addWidget(ioCollapsibleButton)

    # Layout within the io collapsible button
    ioFormLayout = qt.QFormLayout(ioCollapsibleButton)
    secondaryIoCollapsibleGroupBox = ctk.ctkCollapsibleGroupBox()
    secondaryIoCollapsibleGroupBox.title = "Additional Input"
    secondaryIoCollapsibleGroupBox.collapsed = 1
    secondaryIoFormLayout = qt.QFormLayout(secondaryIoCollapsibleGroupBox)
    self.inputNodeSelectors = []
    self.inputNodeSelectors.append(self.addInputNodeSelector(0, ioFormLayout))
    self.inputNodeSelectors[0].noneEnabled = False
    for i in range(1,3):
      self.inputNodeSelectors.append(self.addInputNodeSelector(i, secondaryIoFormLayout))
    self.inputNodeSelectors[0].toolTip = "Select the 1st input volume to be segmented"
    self.inputNodeSelectors[1].toolTip = "Select the 2nd input volume to be segmented"
    self.inputNodeSelectors[2].toolTip = "Select the 3rd input volume to be segmented"
    ioFormLayout.addWidget(secondaryIoCollapsibleGroupBox)

    # Objects
    objectCollapsibleGroupBox = ctk.ctkCollapsibleGroupBox()
    objectCollapsibleGroupBox.title = "Objects"
    self.frame.layout().addWidget(objectCollapsibleGroupBox)

    # Layout within the io collapsible button
    objectFormLayout = qt.QFormLayout(objectCollapsibleGroupBox)
    foregroundLayout = qt.QHBoxLayout()
    foregroundLabel = slicer.qMRMLLabelComboBox()
    foregroundLabel.objectName = 'Foreground label'
    foregroundLabel.setMRMLScene(slicer.mrmlScene)
    foregroundLabel.setMRMLColorNode(self.editUtil.getColorNode())
    foregroundLabel.labelValueVisible = True
    foregroundLabel.currentColor = 1
    foregroundWeightSpinBox = qt.QDoubleSpinBox(foregroundLabel)
    self.foregroundWeightSpinBox = foregroundWeightSpinBox
    foregroundWeightSpinBox.setRange(0.0, 1.0)
    foregroundWeightSpinBox.setSingleStep(0.1)
    foregroundWeightSpinBox.value = 1.0
    foregroundPopup = ctk.ctkPopupWidget( foregroundWeightSpinBox )
    foregroundPopupLayout = qt.QHBoxLayout( foregroundPopup )
    foregroundPopupSlider = ctk.ctkDoubleSlider( foregroundPopup )
    self.foregroundPopupSlider = foregroundPopupSlider
    foregroundPopupSlider.maximum = 1.0
    foregroundPopupSlider.minimum = 0.0
    foregroundPopupSlider.singleStep = 0.1
    foregroundPopupSlider.connect('valueChanged(double)', self.foregroundWeightSpinBox.setValue)
    foregroundWeightSpinBox.connect('valueChanged(double)', self.foregroundPopupSlider.setValue)
    foregroundLayout.addWidget( foregroundLabel )
    foregroundLayout.addWidget( foregroundWeightSpinBox )
    foregroundPopupLayout.addWidget( foregroundPopupSlider )
    objectFormLayout.addRow("Foreground Label:", foregroundLayout )
    self.objectLabel = foregroundLabel
    # http://qt-project.org/doc/qt-4.7/qt.html
    foregroundPopup.alignment = 0x0082 # Qt::AlignVCenter | Qt::AlignRight
    foregroundPopup.horizontalDirection = 0 # Qt::LeftToRight
    foregroundPopup.verticalDirection = 0 # Qt::TopToBottom
    foregroundPopup.animationEffect = 1 # Qt::ScrollEffect

    backgroundLayout = qt.QHBoxLayout()
    backgroundLabel = slicer.qMRMLLabelComboBox()
    backgroundLabel.objectName = 'Background label'
    backgroundLabel.setMRMLScene(slicer.mrmlScene)
    backgroundLabel.setMRMLColorNode(self.editUtil.getColorNode())
    backgroundLabel.labelValueVisible = True
    backgroundLabel.currentColor = 2
    backgroundWeightSpinBox = qt.QDoubleSpinBox(backgroundLabel)
    self.backgroundWeightSpinBox = backgroundWeightSpinBox
    backgroundWeightSpinBox.setRange(0.0, 1.0)
    backgroundWeightSpinBox.setSingleStep(0.1)
    backgroundWeightSpinBox.value = 1.0
    backgroundPopup = ctk.ctkPopupWidget( backgroundWeightSpinBox )
    backgroundPopupLayout = qt.QHBoxLayout( backgroundPopup )
    backgroundPopupSlider = ctk.ctkDoubleSlider( backgroundPopup )
    self.backgroundPopupSlider = backgroundPopupSlider
    backgroundPopupSlider.maximum = 1.0
    backgroundPopupSlider.minimum = 0.0
    backgroundPopupSlider.singleStep = 0.1
    backgroundPopupSlider.connect('valueChanged(double)', self.backgroundWeightSpinBox.setValue)
    backgroundWeightSpinBox.connect('valueChanged(double)', self.backgroundPopupSlider.setValue)
    backgroundLayout.addWidget( backgroundLabel )
    backgroundLayout.addWidget( backgroundWeightSpinBox )
    backgroundPopupLayout.addWidget( backgroundPopupSlider )
    objectFormLayout.addRow("Background Label:", backgroundLayout)
    self.backgroundLabel = backgroundLabel
    # http://qt-project.org/doc/qt-4.7/qt.html
    backgroundPopup.alignment = 0x0082 # Qt::AlignVCenter | Qt::AlignRight
    backgroundPopup.horizontalDirection = 0 # Qt::LeftToRight
    backgroundPopup.verticalDirection = 0 # Qt::TopToBottom
    backgroundPopup.animationEffect = 1 # Qt::ScrollEffect

    barrierLabel = slicer.qMRMLLabelComboBox()
    barrierLabel.objectName = 'Barrier label selector'
    barrierLabel.setMRMLScene(slicer.mrmlScene)
    barrierLabel.setMRMLColorNode(self.editUtil.getColorNode())
    barrierLabel.labelValueVisible = True
    barrierLabel.currentColor = 3
    objectFormLayout.addRow("Barrier Label:", barrierLabel)
    self.barrierLabel = barrierLabel

    voidLabel = slicer.qMRMLLabelComboBox()
    voidLabel.objectName = 'Void label selector'
    voidLabel.setMRMLScene(slicer.mrmlScene)
    voidLabel.setMRMLColorNode(self.editUtil.getColorNode())
    voidLabel.labelValueVisible = True
    # HACK: Set this to 1 first to get around a bug in the labelComboBox MRML interaction
    voidLabel.setCurrentColor(1)
    voidLabel.setCurrentColor(0)
    objectFormLayout.addRow("Void Label:", voidLabel)
    self.voidLabel = voidLabel

    # Presets
    # Placeholder
    presetsCollapsibleGroupBox = ctk.ctkCollapsibleGroupBox()
    presetsCollapsibleGroupBox.title = "Preset"
    self.frame.layout().addWidget(presetsCollapsibleGroupBox)
    presetComboBox = slicer.qSlicerPresetComboBox()

    # Advanced Parameters
    paramsCollapsibleGroupBox = ctk.ctkCollapsibleGroupBox()
    paramsCollapsibleGroupBox.title = "Advanced Parameters"
    paramsCollapsibleGroupBox.collapsed = 1
    self.frame.layout().addWidget(paramsCollapsibleGroupBox)

    # Layout within the io collapsible button
    paramsFormLayout = qt.QFormLayout(paramsCollapsibleGroupBox)

    erosionSpinBox = qt.QSpinBox()
    erosionSpinBox.objectName = 'erosionSpinBox'
    erosionSpinBox.toolTip = "Set the erosion radius."
    erosionSpinBox.setMinimum(0)
    paramsFormLayout.addRow("Erosion Radius:", erosionSpinBox)
    self.erosionSpinBox = erosionSpinBox

    holeFillSpinBox = qt.QSpinBox()
    holeFillSpinBox.objectName = 'holeFillSpinBox'
    holeFillSpinBox.toolTip = "Set the hole fill iterations."
    holeFillSpinBox.setMinimum(0)
    paramsFormLayout.addRow("Hole Fill Iterations:", holeFillSpinBox)
    self.holeFillSpinBox = holeFillSpinBox

    # probabilitySmoothingStandardDeviation spin box
    probabilitySmoothingStdDevSpinBox = qt.QDoubleSpinBox()
    probabilitySmoothingStdDevSpinBox.objectName = 'probabilitySmoothingStdDevSpinBox'
    probabilitySmoothingStdDevSpinBox.toolTip = "Standard deviation of blur applied to probability images prior to computing maximum likelihood of each class at each pixel."
    probabilitySmoothingStdDevSpinBox.setMinimum(0.0)
    probabilitySmoothingStdDevSpinBox.setValue(3.0) # Default
    probabilitySmoothingStdDevSpinBox.setSingleStep(0.1)
    paramsFormLayout.addRow("Probability Smoothing Standard Deviation:", probabilitySmoothingStdDevSpinBox)
    self.probabilitySmoothingStdDevSpinBox = probabilitySmoothingStdDevSpinBox

    # draft check box
    draftCheckBox = qt.QCheckBox()
    draftCheckBox.objectName = 'draftCheckBox'
    draftCheckBox.toolTip = "Downsamples results by a factor of 4."
    paramsFormLayout.addRow("Draft Mode:", draftCheckBox)
    self.draftCheckBox = draftCheckBox

    # reclassifyObjectMask check box
    reclassifyObjectMaskCheckBox = qt.QCheckBox()
    reclassifyObjectMaskCheckBox.objectName = 'reclassifyObjectMaskCheckBox'
    reclassifyObjectMaskCheckBox.toolTip = "Perform classification on voxels within the foreground mask?"
    paramsFormLayout.addRow("Reclassify Foreground Mask:", reclassifyObjectMaskCheckBox)
    self.reclassifyObjectMaskCheckBox = reclassifyObjectMaskCheckBox

    # reclassifyNotObjectMask check box
    reclassifyNotObjectMaskCheckBox = qt.QCheckBox()
    reclassifyNotObjectMaskCheckBox.objectName = 'reclassifyNotObjectMaskCheckBox'
    reclassifyNotObjectMaskCheckBox.toolTip = "Perform classification on voxels within the barrier mask?"
    paramsFormLayout.addRow("Reclassify Barrier Mask:", reclassifyNotObjectMaskCheckBox)
    self.reclassifyNotObjectMaskCheckBox = reclassifyNotObjectMaskCheckBox

    # force classification check box
    forceClassificationCheckBox = qt.QCheckBox()
    forceClassificationCheckBox.objectName = 'forceClassificationCheckBox'
    forceClassificationCheckBox.toolTip = "Perform the classification of all voxels?"
    forceClassificationCheckBox.setChecked(False)
    paramsFormLayout.addRow("Force Classification: ", forceClassificationCheckBox)
    self.forceClassificationCheckBox = forceClassificationCheckBox

    self.helpLabel = qt.QLabel("Run the PDF Segmentation on the current label map.", self.frame)
    self.frame.layout().addWidget(self.helpLabel)

    self.apply = qt.QPushButton("Apply", self.frame)
    self.apply.setToolTip("Apply to run segmentation.\nCreates a new label volume using the current volume as input")
    self.frame.layout().addWidget(self.apply)
    self.widgets.append(self.apply)

    EditorLib.HelpButton(self.frame, "Use this tool to apply segmentation using Parzen windowed PDFs.\n\n Select different label colors and paint on the foreground, background, or barrier voxels using the paint effect.\nTo run segmentation correctly, you need to supply a minimum or two class labels.")

    self.connections.append( (self.apply, 'clicked()', self.onApply) )

  def destroy(self):
    super(InteractiveConnectedComponentsUsingParzenPDFsOptions,self).destroy()

  # note: this method needs to be implemented exactly as-is
  # in each leaf subclass so that "self" in the observer
  # is of the correct type
  def updateParameterNode(self, caller, event):
    node = EditUtil.EditUtil().getParameterNode()
    if node != self.parameterNode:
      if self.parameterNode:
        node.RemoveObserver(self.parameterNodeTag)
      self.parameterNode = node
      self.parameterNodeTag = node.AddObserver(vtk.vtkCommand.ModifiedEvent, self.updateGUIFromMRML)

  def setMRMLDefaults(self):
    super(InteractiveConnectedComponentsUsingParzenPDFsOptions,self).setMRMLDefaults()

  def updateGUIFromMRML(self,caller,event):
    self.disconnectWidgets()
    super(InteractiveConnectedComponentsUsingParzenPDFsOptions,self).updateGUIFromMRML(caller,event)
    self.connectWidgets()

  def onApply(self):

    self.undoRedo.saveState()
    objectIds = []
    objectIds.append(self.objectLabel.currentColor)
    objectIds.append(self.backgroundLabel.currentColor)
    objectPDFWeights = []
    objectPDFWeights.append(self.foregroundWeightSpinBox.value)
    objectPDFWeights.append(self.backgroundWeightSpinBox.value)
    parameters = {}
    for i in range(0,3):
      parameters['inputVolume'+str(i+1)] = self.inputNodeSelectors[i].currentNode()
    parameters['voidId'] = self.voidLabel.currentColor
    parameters['objectId'] = objectIds
    parameters['labelmap'] = self.editUtil.getLabelVolume()
    parameters['outputVolume'] = self.editUtil.getLabelVolume()
    parameters['erodeRadius'] = self.erosionSpinBox.value
    parameters['holeFillIterations'] = self.holeFillSpinBox.value
    parameters['objectPDFWeight'] = objectPDFWeights
    parameters['probSmoothingStdDev'] = self.probabilitySmoothingStdDevSpinBox.value
    parameters['draft'] = self.draftCheckBox.checked
    parameters['reclassifyObjectMask'] = self.reclassifyObjectMaskCheckBox.checked
    parameters['reclassifyNotObjectMask'] = self.reclassifyNotObjectMaskCheckBox.checked
    parameters['forceClassification'] = self.forceClassificationCheckBox.checked

    module = slicer.modules.segmentconnectedcomponentsusingparzenpdfs
    cliNode = self.getCLINode(module, 'PDFSegmenterEditorEffect')
    slicer.cli.run(module, cliNode, parameters)

  def getCLINode(self, module, nodeName):
    cliNode = slicer.mrmlScene.GetFirstNodeByName(nodeName)
    # Also check path to make sure the CLI isn't a scripted module
    if (cliNode == None) and ('qt-scripted-modules' not in module.path):
      cliNode = slicer.cli.createNode(module)
      cliNode.SetName(nodeName)
    return cliNode

  def updateMRMLFromGUI(self):
    if self.updatingGUI:
      return
    disableState = self.parameterNode.GetDisableModifiedEvent()
    self.parameterNode.SetDisableModifiedEvent(1)
    super(InteractiveConnectedComponentsUsingParzenPDFsOptions,self).updateMRMLFromGUI()
    self.parameterNode.SetDisableModifiedEvent(disableState)
    if not disableState:
      self.parameterNode.InvokePendingModifiedEvent()

  def setInputNode1(self):
    backgroundLogic = self.sliceLogic.GetBackgroundLayer()
    backgroundNode = backgroundLogic.GetVolumeNode()

  def addInputNodeSelector(self, index, layout):
    inputNodeSelector =  slicer.qMRMLNodeComboBox()
    inputNodeSelector.objectName = 'inputNodeSelector'+str(index+1)
    inputNodeSelector.nodeTypes = ['vtkMRMLScalarVolumeNode']
    inputNodeSelector.noneEnabled = True
    inputNodeSelector.addEnabled = False
    inputNodeSelector.removeEnabled = False
    inputNodeSelector.editEnabled = True
    inputNodeSelector.enabled = 1
    inputNodeSelector.setMRMLScene(slicer.mrmlScene)
    layout.addRow("Input Volume "+str(index+1)+":", inputNodeSelector)
    return inputNodeSelector

#
# EditorEffectTemplateTool
#

class InteractiveConnectedComponentsUsingParzenPDFsTool(LabelEffect.LabelEffectTool):
  """
  One instance of this will be created per-view when the effect
  is selected.  It is responsible for implementing feedback and
  label map changes in response to user input.
  This class observes the editor parameter node to configure itself
  and queries the current view for background and label volume
  nodes to operate on.
  """

  def __init__(self, sliceWidget):
    super(InteractiveConnectedComponentsUsingParzenPDFsTool,self).__init__(sliceWidget)
    # create a logic instance to do the non-gui work
    self.logic = InteractiveConnectedComponentsUsingParzenPDFsLogic(self.sliceWidget.sliceLogic())

  def cleanup(self):
    super(InteractiveConnectedComponentsUsingParzenPDFsTool,self).cleanup()

  def processEvent(self, caller=None, event=None):
    """
    handle events from the render window interactor
    """

    # let the superclass deal with the event if it wants to
    if super(InteractiveConnectedComponentsUsingParzenPDFsTool,self).processEvent(caller,event):
      return

    if event == "LeftButtonPressEvent":
      xy = self.interactor.GetEventPosition()
      sliceLogic = self.sliceWidget.sliceLogic()
      logic = InteractiveConnectedComponentsUsingParzenPDFsLogic(sliceLogic)
      logic.apply(xy)
      print("Got a %s at %s in %s", (event,str(xy),self.sliceWidget.sliceLogic().GetSliceNode().GetName()))
      self.abortEvent(event)
    else:
      pass
    #if event == "LeftButtonPressEvent"
    #  self.actionState = "painting"
    #  if not self.pixelMode:
    #    self.cursorOff()
    #  xy = self.interactor.GetEventPosition()
    #elif event == "LeftButtonReleaseEvent":
    #  self.paintApply

    # events from the slice node
    #if caller and caller.IsA('vtkMRMLSliceNode'):
      # here you can respond to pan/zoom or other changes
      # to the view
    #  pass


#
# EditorEffectTemplateLogic
#

class InteractiveConnectedComponentsUsingParzenPDFsLogic(LabelEffect.LabelEffectLogic):
  """
  This class contains helper methods for a given effect
  type.  It can be instanced as needed by an EditorEffectTemplateTool
  or EditorEffectTemplateOptions instance in order to compute intermediate
  results (say, for user feedback) or to implement the final
  segmentation editing operation.  This class is split
  from the EditorEffectTemplateTool so that the operations can be used
  by other code without the need for a view context.
  """

  def __init__(self,sliceLogic):
    self.sliceLogic = sliceLogic

  def apply(self,xy):
    pass


#
# The InteractiveConnectedComponentsUsingParzenPDFs Template class definition
#

class InteractiveConnectedComponentsUsingParzenPDFsExtension(LabelEffect.LabelEffect):
  """Organizes the Options, Tool, and Logic classes into a single instance
  that can be managed by the EditBox
  """

  def __init__(self):
    # name is used to define the name of the icon image resource (e.g. EditorEffectTemplate.png)
    self.name = "InteractiveConnectedComponentsUsingParzenPDFs"
    self.title = "InteractiveConnectedComponentsUsingParzenPDFs"
    # tool tip is displayed on mouse hover
    self.toolTip = "Perform PDF Segmentation"

    self.options = InteractiveConnectedComponentsUsingParzenPDFsOptions
    self.tool = InteractiveConnectedComponentsUsingParzenPDFsTool
    self.logic = InteractiveConnectedComponentsUsingParzenPDFsLogic


#
# EditorEffectTemplate
#

class InteractiveConnectedComponentsUsingParzenPDFs:
  """
  This class is the 'hook' for slicer to detect and recognize the extension
  as a loadable scripted module
  """
  def __init__(self, parent):
    parent.title = "Editor InteractiveConnectedComponentsUsingParzenPDFs Effect"
    parent.categories = ["Developer Tools.Editor Extensions"]
    parent.contributors = ["Danielle Pace (Kitware)",
                           "Christopher Mullins (Kitware)",
                           "Stephen Aylward (Kitware)"]
    parent.helpText = """
    The PDF Segmenter is a framework for using connected components alonside intensity
    histograms for classifying images in pixel space.
    """
    parent.acknowledgementText = """
    This work is part of the TubeTK project at Kitware.
    Module implemented by Danielle Pace.  PDF Segmenter implemented by
    Stephen Aylward.
    """

    # TODO:
    # don't show this module - it only appears in the Editor module
    #parent.hidden = True

    # Add this extension to the editor's list for discovery when the module
    # is created.  Since this module may be discovered before the Editor itself,
    # create the list if it doesn't already exist.
    try:
      slicer.modules.editorExtensions
    except AttributeError:
      slicer.modules.editorExtensions = {}
    slicer.modules.editorExtensions['InteractiveConnectedComponentsUsingParzenPDFs'] = InteractiveConnectedComponentsUsingParzenPDFsExtension

#
# EditorEffectTemplateWidget
#

class InteractiveConnectedComponentsUsingParzenPDFsWidget:
  def __init__(self, parent = None):
    self.parent = parent

  def setup(self):
    # don't display anything for this widget - it will be hidden anyway
    pass

  def enter(self):
    pass

  def exit(self):
    pass
