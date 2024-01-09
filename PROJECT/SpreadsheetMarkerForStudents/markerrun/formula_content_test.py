import traceback
from markerrun.ClasesCorrector import SuperClassForTests
from usecasesmarker.spread_sheet_factory_for_checker import SpreadSheetFactoryForChecker


class FormulaContentTest(SuperClassForTests):

    numErrorsBefore = 0;

    numInstances = 0;

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        FormulaContentTest.numInstances = FormulaContentTest.numInstances + 1
        self.instance=SpreadSheetFactoryForChecker.create_spreadsheet_controller()
        self.instance.set_cell_content("A1","1")
        self.instance.set_cell_content("A2","2")
        self.instance.set_cell_content("A3","3")
        self.instance.set_cell_content("A4","4")
        self.instance.set_cell_content("A5","5")
        self.instance.set_cell_content("A6","6")
        self.instance.set_cell_content("A7","7")
        self.instance.set_cell_content("A8","8")
        self.instance.set_cell_content("A9","9")
        self.instance.set_cell_content("A10","10")
        self.instance.set_cell_content("A11","11")
        self.instance.set_cell_content("A12","12")
        self.instance.set_cell_content("A13","13")
        self.instance.set_cell_content("A14","14")
        self.instance.set_cell_content("A15","15")
        self.instance.set_cell_content("A16","16")
        self.instance.set_cell_content("A17","17")
        self.instance.set_cell_content("A18","18")
        self.instance.set_cell_content("A19","19")
        self.instance.set_cell_content("A20","20")
        self.instance.set_cell_content("A21","21")
        self.instance.set_cell_content("A22","22")
        self.instance.set_cell_content("A23","23")
        self.instance.set_cell_content("A24","24")
        self.instance.set_cell_content("A25","This is a string")
        if FormulaContentTest.numInstances == 1:
            FormulaContentTest.numErrorsBefore = len(SuperClassForTests.indErrors)

    def setUpClass():
        # SuperClassForTests.nota = {}
        FormulaContentTest.nota = 0.0
        print("\nMarking editing a cell with a formula content (FormulaContentTest)")
        print("***********************")


    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "FormulaContent")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        FormulaContentTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_set_cell_content_formula_only_numbers(self):
        valor_total = 0.465116279069767
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with only numbers. Value: " + str(valor_total))
        try:
            print("\n\tCase 1: a sum of two numbers. Value: " + str(valor_total * 0.25))
            self.instance.set_cell_content("B1", "=1+2")
            content = self.instance.get_cell_content_as_float("B1")
            error=self.sAssertEquals(3.0,content,valor_total*0.25,"The cell should contain the value 3.0 -result of " \
                                     +"the formula =1+2- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        try:
            print("\n\tCase 2: a substraction of two numbers. Value: " + str(valor_total * 0.25))
            self.instance.set_cell_content("B2", "=1-3")
            content = self.instance.get_cell_content_as_float("B2")
            error=self.sAssertEquals(-2.0,content,valor_total*0.25,"The cell should contain the value -2.0 -result of " \
                                     +"the formula =1-3- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
            to_throw=self.toThrow(error,to_throw)
        try:
            print("\n\tCase 3: a multiplication of two numbers. Value: " + str(valor_total * 0.25))
            self.instance.set_cell_content("B3", "=2*3")
            content = self.instance.get_cell_content_as_float("B3")
            error=self.sAssertEquals(6.0,content,valor_total*0.25,"The cell should contain the value 6.0 -result of " \
                                     +"the formula =2*3- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        try:
            print("\n\tCase 4: a division of two numbers. Value: " + str(valor_total * 0.25))
            self.instance.set_cell_content("B4", "=8/4")
            content = self.instance.get_cell_content_as_float("B4")
            error=self.sAssertEquals(2.0,content,valor_total*0.25,"The cell should contain the value 2.0 -result of " \
                                     +"the formula =8/4- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test_02_set_cell_content_formula_numbers_one_level_parenthesis(self):
        valor_total = 0.62015503875969
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers and one level of parenthesis. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("C1", "=10/(2+3)")
            content = self.instance.get_cell_content_as_float("C1")
            error=self.sAssertEquals(2.0,content,valor_total,"The cell should contain the value 2.0 -result of " \
                                     +"the formula =10/(2+3)- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()

        self.puntosAntesDespues(puntos_antes)

    def test_03_set_cell_content_formula_numbers_two_levels_parenthesis(self):
        valor_total = 0.775193798449612
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers and two levels of parenthesis. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("C2", "=100/(5+(25/5))")
            content = self.instance.get_cell_content_as_float("C2")
            error=self.sAssertEquals(10.0,content,valor_total,"The cell should contain the value 10.0 -result of " \
                                     +"the formula =100/(5+(25/5))- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test_04_set_cell_content_formula_numbers_cells(self):
        valor_total = 0.775193798449612
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers and cells. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("D1", "=A1*10-5")
            content = self.instance.get_cell_content_as_float("D1")
            error=self.sAssertEquals(5.0,content,valor_total,"The cell should contain the value 5.0 -result of " \
                                     +"the formula =A1*10-5- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test_05_set_cell_content_formula_numbers_cells_one_level_parenthesis(self):
        valor_total = 0.852713178294574
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers, cells, and one level of parenthesis. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("E1", "=(A5*4)/(A2+A2)")
            content = self.instance.get_cell_content_as_float("E1")
            error=self.sAssertEquals(5.0,content,valor_total,"The cell should contain the value 5.0 -result of " \
                                     +"the formula =(A5*4)/(A2+A2)- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test_06_set_cell_content_formula_numbers_cells_two_levels_parenthesis(self):
        valor_total = 1.0077519379845
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers, cells, and two levels of parenthesis. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("F1", "=100/(A5+(A5*A5/5))")
            content = self.instance.get_cell_content_as_float("F1")
            error=self.sAssertEquals(10.0,content,valor_total,"The cell should contain the value 10.0 -result of " \
                                     +"the formula =100/(A5+(A5*A5/5))- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test_07_set_cell_content_formula_numbers_cells_functions_num_args(self):
        valor_total = 1.16279069767442
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers, cells, and functions with numbers as args. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("G1", "=(A5*4)/(A2+A2)+SUMA(1;2;3;4;5)")
            content = self.instance.get_cell_content_as_float("G1")
            error=self.sAssertEquals(20.0,content,valor_total,"The cell should contain the value 20.0 -result of " \
                                     +"the formula =(A5*4)/(A2+A2)+SUMA(1;2;3;4;5)- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test_08_set_cell_content_formula_numbers_cells_functions_num_cells_args(self):
        valor_total = 1.31782945736434
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers, cells, and functions with numbers and cells as args. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("H1", "=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5)")
            content = self.instance.get_cell_content_as_float("H1")
            error=self.sAssertEquals(20.0,content,valor_total,"The cell should contain the value 20.0 -result of " \
                                     +"the formula =(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5)- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test_09_set_cell_content_formula_numbers_cells_functions_num_cells_ranges_args(self):
        valor_total = 1.47286821705426
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers, cells, and functions with numbers, cells, and ranges as args. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("I1", "=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5;A6:A12)")
            content = self.instance.get_cell_content_as_float("I1")
            error=self.sAssertEquals(83.0,content,valor_total,"The cell should contain the value 83.0 -result of " \
                                     +"the formula =(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5;A6:A12)- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test_10_set_cell_content_formula_numbers_cells_functions_num_cells_ranges_functions_args(self):
        valor_total = 1.55038759689922
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nSpreadsheetControllerForChecker::testSetCellContent() with formula content with numbers, cells, and functions with numbers, cells, ranges, and other functions as args. Value: " + str(valor_total))
        try:
            self.instance.set_cell_content("J1", "=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5;A6:A12;MIN(A13:A20))")
            content = self.instance.get_cell_content_as_float("J1")
            error=self.sAssertEquals(96.0,content,valor_total,"The cell should contain the value 96.0 -result of " \
                                     +"the formula =(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5;A6:A12;MIN(A13:A20))- Instead it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)
