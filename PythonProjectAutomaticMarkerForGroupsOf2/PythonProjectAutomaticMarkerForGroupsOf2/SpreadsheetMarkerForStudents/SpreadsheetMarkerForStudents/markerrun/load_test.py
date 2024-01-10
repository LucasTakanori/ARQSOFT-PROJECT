import traceback
from markerrun.ClasesCorrector import SuperClassForTests
from usecasesmarker.spread_sheet_factory_for_checker import SpreadSheetFactoryForChecker


class LoadTest(SuperClassForTests):

    numErrorsBefore = 0

    numInstances = 0

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        LoadTest.numInstances = LoadTest.numInstances + 1
        self.instance=SpreadSheetFactoryForChecker.create_spreadsheet_controller()
        if LoadTest.numInstances == 1:
            LoadTest.numErrorsBefore = len(SuperClassForTests.indErrors)

    def setUpClass():
        # SuperClassForTests.nota = {}
        LoadTest.nota = 0.0
        print("\nMarking loading a spreadsheet (LoadTest)")
        print("***********************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Load")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        LoadTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_check_read_from_file(self):
        valor_total = 10
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nTesting load spreadsheet. Value: " + str(valor_total))
        try:
            print("\nThe spreadsheet shall be read from the reference file marker_save_test_ref.s2v")
            self.instance.load_spreadsheet_from_file("marker_save_test_ref.s2v")
            self.check_loaded_spreadsheet_contents(valor_total)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()

    def check_loaded_spreadsheet_contents(self,valor_total):
        for i in range(1,7):
            self.check_row_i(i,valor_total)
        self.check_row_i(7,valor_total)

    def check_row_i(self,row,valor_total):
        weight=None
        expected=None
        cell_coords=None
        if row==1:
            weight=0.7
            self.check_first_row(expected,cell_coords,valor_total*weight)
            return
        elif row==2:
            expected=[2.0,10.0]
            cell_coords=["A2","B2"]
            weight=0.05
        elif row==3:
            expected=[3.0,"",30.0]
            cell_coords=["A3","B3","C3"]
            weight=0.05
        elif row==4:
            expected=[4.0,"","",8.0]
            cell_coords=["A4","B4","C4","D4"]
            weight=0.05
        elif row==5:
            expected=[5.0,"","","",20.0]
            cell_coords=["A5","B5","C5","D5","E5"]
            weight=0.05
        elif row==6:
            expected=[6.0,"","","","",40.0]
            cell_coords=["A6","B6","C6","D6","E6","F6"]
            weight=0.05
        elif row==7:
            expected=["","","","","","","","","",""]
            cell_coords=["A7","B7","C7","D7","E7","F7","G7","H7","I7","J7"]
            weight=0.05
        self.check_row_without_formulas(row,expected,cell_coords,valor_total*weight)

    def check_first_row(self,expected,cell_coords,valor):
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        cell_coord=None
        expected_val=None
        expected=["=1+2","=10/(2+3)","=A1*10-5","=(A5*4)/(A2+A2)","=100/(A5+(A5*A5/5))" \
            ,"=(A5*4)/(A2+A2)+SUMA(1;2;3;4;5)","=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5)" \
            ,"=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5;A6:A12)","=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5;A6:A12;MIN(A13:A20))"]
        cell_coords=["B1","C1","D1","E1","F1","G1","H1","I1","J1"]
        print("\tTesting first row of the loaded spreadsheet. Value: " + str(valor))
        try:
            cell_coord="A1"
            expected_val=1.0
            content=self.instance.get_cell_content_as_float("A1")
            error = self.sAssertEquals(1.0,content,valor/10,"Error in cell " + cell_coord + ". It should be "\
                + str(expected_val) + " BUT instead it is " + str(content))
            to_throw=self.toThrow(error,to_throw)
            count=0
            for cell_coord in cell_coords:
                content=self.instance.get_cell_formula_expression(cell_coord)
                expected_val=expected[count]
                error = self.sAssertEquals(expected_val,content,valor/10,"Error in cell " + cell_coord + ". It should be " \
                                           + str(expected_val) + " BUT instead it is " + str(content))
                to_throw=self.toThrow(error,to_throw)
                count+=1

        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def check_row_without_formulas(self,num_row,expected,cell_coords,valor):
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        cell_coord=None
        expected_val=None
        print("\tTesting row number " + str(num_row) + ". Value: " + str(valor))
        count=0
        content=None
        num_tests=len(cell_coords)
        try:
            for cell_coord in cell_coords:
                expected_val = expected[count]
                if expected_val.__class__.__name__=="float":
                    content=self.instance.get_cell_content_as_float(cell_coord)
                else:
                    content=self.instance.get_cell_content_as_string(cell_coord)
                error=self.sAssertEquals(expected_val,content,valor/num_tests,"Error in cell " + cell_coord + ". It should be " \
                        + str(expected_val) + " BUT instead it is " + str(content))
                to_throw=self.toThrow(error,to_throw)
                count+=1
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)
