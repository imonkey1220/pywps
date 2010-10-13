"""Processes for testing purposes"""

from pywps.Process import WPSProcess
class NoInputsProcess(WPSProcess):
    """This process has no inputs and no outputs"""
    def __init__(self):
        WPSProcess.__init__(self, identifier = "noinputsprocess",title="No inputs")

class LiteralProcess(WPSProcess):
    """This process defines several types of literal type of in- and
    outputs"""

    def __init__(self):
        WPSProcess.__init__(self, identifier = "literalprocess",
                title="Literal process",
                metadata=[{"title":"Foobar","href":"http://foo/bar"},
                          {"title":"Barfoo","href":"http://bar/foo"},
                          {"title":"Literal process"},
                          {"href":"http://foobar/"}])

        self.intIn = self.addLiteralInput(identifier="int",
                                                 title="Integer data in")

        self.stringIn = self.addLiteralInput(identifier="string",
                                                 title="String data in",
                                                 type = type(""))

        self.floatIn = self.addLiteralInput(identifier="float",
                                                 title="Float data in",
                                                 type = type(0.0))

        self.zeroInDefault = self.addLiteralInput(identifier="zerodefault",
                                                 title="Zero data input",
                                                 default=0.0,
                                                 type = type(0.0))

        self.zeroInSet = self.addLiteralInput(identifier="zeroset",
                                                 title="Zero data input",
                                                 type = type(0.0))

        self.intOut = self.addLiteralOutput(identifier="int",
                                                 title="Integer data out")
        self.stringOut = self.addLiteralOutput(identifier="string",
                                                 title="String data out",
                                                 type = type(""))
        self.floatOut = self.addLiteralOutput(identifier="float",
                                                 title="Float data out",
                                                 type = type(0.0))
    def execute(self):
        self.intOut.setValue(self.intIn.getValue())
        self.stringOut.setValue(self.stringIn.getValue())
        self.floatOut.setValue(self.floatIn.getValue())

class ComplexProcess(WPSProcess):
    """This process defines raster and vector data in- and outputs"""

    def __init__(self):
        WPSProcess.__init__(self, identifier = "complexprocess",
            title="Complex process",
            storeSupported=True)

        self.vectorin = self.addComplexInput(identifier="vectorin",
                                                 title="Vector file")

        self.rasterin = self.addComplexInput(identifier="rasterin",
                                                 title="Raster file",
                                                 formats = [{"mimeType":"image/tiff"}])

        self.pausein = self.addLiteralInput(identifier="pause",
                                                 title="Pause the process",
                                                 abstract="Pause the process for several seconds, so that status=true can be tested",
                                                 default = False,
                                                 type = type(True))

        self.vectorout = self.addComplexOutput(identifier="vectorout",
                                                 title="Vector file")
        self.rasterout = self.addComplexOutput(identifier="rasterout",
                                                 title="Raster file",
                                                 formats = [{"mimeType":"image/tiff"}])
    def execute(self):
        self.vectorout.setValue(self.vectorin.getValue())
        self.rasterout.setValue(self.rasterin.getValue())

        if self.pausein.getValue():
            import time
            for i in range(5):
                self.status.set("Processing process",i*20)
                time.sleep(5)
        return

class BBoxProcess(WPSProcess):
    """This process defines bounding box in- and outputs"""

    def __init__(self):
        WPSProcess.__init__(self, identifier = "bboxprocess",title="BBox process")

        self.bboxin = self.addBBoxInput(identifier="bboxin",title="BBox in",crss=["EPSG:4326"])
        self.bboxout = self.addBBoxOutput(identifier="bboxout",title="BBox out")

    def execute(self):
        self.bboxout.setValue(self.bboxin.value.coords)

class AssyncProcess(WPSProcess):
    """This process runs in assynchronous way"""

    def __init__(self):
        WPSProcess.__init__(self, identifier =
                "assyncprocess",title="Assynchronous process",
                storeSupported=True, statusSupported=True)
    def execute(self):
        import time
        time.sleep(2)