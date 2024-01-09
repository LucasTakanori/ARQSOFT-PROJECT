import traceback
from markerrun.ClasesCorrector import SuperClassForTests
from usecasesmarker.spread_sheet_factory_for_checker import SpreadSheetFactoryForChecker

class TextContentTest(SuperClassForTests):

    numErrorsBefore = 0;

    numInstances = 0;

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        TextContentTest.numInstances = TextContentTest.numInstances + 1
        self.instance=SpreadSheetFactoryForChecker.create_spreadsheet_controller()
        if TextContentTest.numInstances == 1:
            TextContentTest.numErrorsBefore = len(SuperClassForTests.indErrors)

    def setUpClass():
        # SuperClassForTests.nota = {}
        TextContentTest.nota = 0.0
        print("\nMarking editing a cell with a text content (TextContentTest)")
        print("***********************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "TextContent")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        TextContentTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01_set_cell_content_text_content(self):
        valor_total = 10
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with text content. Value: " + str(valor_total))
        try:
            str_val="This is a string"
            self.instance.set_cell_content("C1",str_val)
            content = self.instance.get_cell_content_as_string("C1")
            error = self.sAssertEquals(str_val,content,valor_total,"The cell " \
                    + "should contain the string: \'This is a string\'. Instead, it contains \'" \
                    + content + "\'")
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)
