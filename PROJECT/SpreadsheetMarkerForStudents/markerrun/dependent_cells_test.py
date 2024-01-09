import traceback
from markerrun.ClasesCorrector import SuperClassForTests
from usecasesmarker.spread_sheet_factory_for_checker import SpreadSheetFactoryForChecker


class DependentCellsTest(SuperClassForTests):

    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        DependentCellsTest.numInstances = DependentCellsTest.numInstances + 1
        self.instance=SpreadSheetFactoryForChecker.create_spreadsheet_controller()
        if DependentCellsTest.numInstances == 1:
            DependentCellsTest.numErrorsBefore = len(SuperClassForTests.indErrors)
        try:
            self.instance.set_cell_content("A1", "1")
            self.instance.set_cell_content("A2", "2")
            self.instance.set_cell_content("A3", "3")
            self.instance.set_cell_content("A4", "4")
            self.instance.set_cell_content("A5", "5")
            self.instance.set_cell_content("A6", "6")
            self.instance.set_cell_content("A7", "7")
            self.instance.set_cell_content("A8", "8")
            self.instance.set_cell_content("A9", "9")
            self.instance.set_cell_content("A10", "10")
            self.instance.set_cell_content("A11", "11")
            self.instance.set_cell_content("A12", "12")
            self.instance.set_cell_content("A13", "13")
            self.instance.set_cell_content("A14", "14")
            self.instance.set_cell_content("A15", "15")
            self.instance.set_cell_content("A16", "16")
            self.instance.set_cell_content("A17", "17")
            self.instance.set_cell_content("A18", "18")
            self.instance.set_cell_content("A19", "19")
            self.instance.set_cell_content("A20", "20")
            self.instance.set_cell_content("A21", "21")
            self.instance.set_cell_content("A22", "22")
            self.instance.set_cell_content("A23", "23")
            #
            #Now set formulas that depend on some of the cells above
            #
            self.instance.set_cell_content("B1", "=A1+2-A2")
            self.instance.set_cell_content("B2", "=1+SUMA(A3;A4;A5)")
            self.instance.set_cell_content("C1", "=2+SUMA(A6:A10)")
        except Exception as err:
            print("An error has occurred while trying to set either "
                           + "a numerical or a formula content in one cell. You should "
                           + "review your code as this should not happen. Details "
                           + "of the exception follow: " + str(err));
            traceback.print_exc()


    def setUpClass():
        # SuperClassForTests.nota = {}
        DependentCellsTest.nota = 0.0
        print("\nMarking updating of dependent cells (DependentCellsTest)")
        print("***********************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "DependentCells")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        DependentCellsTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01_dependent_cells_direct_dependency(self):
        valor_total = 2.5
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nChecking the proper update of cells that contain formulas that contain an operand that is a reference to the cell whose content is modified. Value: " + str(valor_total))
        cell_str="B1"
        try:
            print("\n\tCase 1: modifying one cell that is directly referenced as an operand in the formula: "+ str(valor_total*0.5))
            content = self.instance.get_cell_content_as_float("B1")
            error = self.sAssertEquals(1.0,content,0,"The cell " + cell_str \
                + " should contain the value: 1 -result of formula =A1+2-A2, when A1=1 and A2=2- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
            self.instance.set_cell_content("A1","2")
            content = self.instance.get_cell_content_as_float("B1")
            error = self.sAssertEquals(2.0,content,valor_total*0.5,"The cell " + cell_str \
                                       + " should contain the value: 2 -result of formula =A1+2-A2, when A1=2 and A2=2- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        try:
            print("\n\tCase 2: modifying a second cell that is directly referenced as an operand in the formula: "+ str(valor_total*0.5))
            self.instance.set_cell_content("A2","4")
            content = self.instance.get_cell_content_as_float("B1")
            error = self.sAssertEquals(0.0,content,valor_total*0.5,"The cell " + cell_str \
                                       + "should contain the value: 0.0 -result of formula =A1+2-A2, when A1=2 and A2=4- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test02_dependent_cells_referenced_as_function_argument(self):
        valor_total = 3.5
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nChecking the proper update of cells that contain formulas that contain a function with an argument that is a reference to the cell whose content is modified. Value: " + str(valor_total))
        cell_str="B2"
        try:
            print("\n\tCase 1: modifying one cell that is directly referenced as an operand in the formula: "+ str(valor_total*0.5))
            content = self.instance.get_cell_content_as_float("B2")
            error = self.sAssertEquals(13.0,content,valor_total*0.25,"The cell " +  cell_str \
                                       + " should contain the value: 13 -result of formula =1+SUMA(A3;A4;A5), when A3=4, A4=4 , and A5=5- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
            self.instance.set_cell_content("A3","4")
            content = self.instance.get_cell_content_as_float("B2")
            error = self.sAssertEquals(14.0,content,valor_total*0.25,"The cell " +  cell_str \
                                       + " should contain the value: 14 -result of formula =1+SUMA(A3;A4;A5), when A3=4, A4=4 , and A5=5- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        try:
            print("\n\tCase 2: modifying a second cell whose reference is one of the arguments of a function in another cell: "+ str(valor_total*0.5))
            self.instance.set_cell_content("A4","5")
            content = self.instance.get_cell_content_as_float("B2")
            error = self.sAssertEquals(15.0,content,valor_total*0.5,"The cell " +  cell_str \
                                       + " should contain the value: 15.0 -result of formula =1+SUMA(A3;A4;A5), when A3=4, A4=5 , and A5=5- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test03_dependent_cells_referenced_as_function_range_argument(self):
        valor_total = 4
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nChecking the proper update of cells that contain formulas that contain a function with an argument that is a range that contains the cell whose content is modified. Value: " + str(valor_total))
        cell_str="C1"
        try:
            print("\n\tCase 1: modifying one cell that is within the range that is one of the arguments of a function in the formula: "+ str(valor_total*0.5))
            content = self.instance.get_cell_content_as_float("C1")
            error = self.sAssertEquals(42.0,content,0,"The cell " + cell_str \
                                       + " should contain the value: 13 -result of formula =1+SUMA(A3;A4;A5), when A3=4, A4=4 , and A5=5- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
            self.instance.set_cell_content("A6","7")
            content = self.instance.get_cell_content_as_float("C1")
            error = self.sAssertEquals(43.0,content,valor_total*0.5,"The cell " +  cell_str \
                                       + " should contain the value: 43 -result of formula =2+SUMA(A6:A10), when A6=7, A7=7, A8=8, A9=9, and A10=10- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        try:
            print("\n\tCase 1: modifying a second cell that is within the range that is one of the arguments of a function in another cell: "+ str(valor_total*0.5))
            self.instance.set_cell_content("A7","8")
            content = self.instance.get_cell_content_as_float("C1")
            error = self.sAssertEquals(44.0,content,valor_total*0.5,"The cell " +  cell_str \
                                       + " should contain the value: 44 -result of formula =2+SUMA(A6:A10), when A6=7, A7=8, A8=8, A9=9, and A10=10- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()

        self.puntosAntesDespues(puntos_antes)

