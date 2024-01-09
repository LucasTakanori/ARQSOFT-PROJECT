import traceback
from markerrun.ClasesCorrector import SuperClassForTests
from usecasesmarker.spread_sheet_factory_for_checker import SpreadSheetFactoryForChecker
import os


class SaveTest(SuperClassForTests):

    numErrorsBefore = 0;

    numInstances = 0;

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        SaveTest.numInstances = SaveTest.numInstances + 1
        self.instance=SpreadSheetFactoryForChecker.create_spreadsheet_controller()
        if SaveTest.numInstances == 1:
            SaveTest.numErrorsBefore = len(SuperClassForTests.indErrors)
        try:
            self.instance.set_cell_content("A1","1")
            self.instance.set_cell_content("A2","2")
            self.instance.set_cell_content("A3","3")
            self.instance.set_cell_content("A4","4")
            self.instance.set_cell_content("A5","5")
            self.instance.set_cell_content("A6","6")
            self.instance.set_cell_content("B1", "=1+2")
            self.instance.set_cell_content("B2", "10")
            self.instance.set_cell_content("C1", "=10/(2+3)")
            self.instance.set_cell_content("C3", "30")
            self.instance.set_cell_content("D1", "=A1*10-5")
            self.instance.set_cell_content("D4", "8")
            self.instance.set_cell_content("E1", "=(A5*4)/(A2+A2)")
            self.instance.set_cell_content("E5", "20")
            self.instance.set_cell_content("F6", "40")
            self.instance.set_cell_content("F1", "=100/(A5+(A5*A5/5))")
            self.instance.set_cell_content("G1", "=(A5*4)/(A2+A2)+SUMA(1;2;3;4;5)")
            self.instance.set_cell_content("H1", "=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5)")
            self.instance.set_cell_content("I1", "=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5;A6:A12)")
            self.instance.set_cell_content("J1", "=(A5*4)/(A2+A2)+SUMA(A1;A2;3;4;5;A6:A12;MIN(A13:A20))")
        except Exception as err:
            print("An error has occurred while trying to set either "
              + "a numerical or a formula content in one cell. You should "
              + "review your code as this should not happen. Details "
              + "of the exception follow: " + str(err));
            traceback.print_exc()

    def setUpClass():
        # SuperClassForTests.nota = {}
        SaveTest.nota = 0.0
        print("\nMarking saving a spreadsheet (SaveTest)")
        print("***********************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "Save")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        SaveTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0;

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01_save(self):
        valor_total = 10
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nTesting save spreadsheet. Value: " + str(valor_total))
        try:
            print("\nThe spreadsheet shall be saved in file marker_save_test.s2v")
            self.instance.save_spreadsheet_to_file("marker_save_test.s2v")
            self.check_s2v_file_contents("marker_save_test.s2v",valor_total)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def check_s2v_file_contents(self,f_name,valor_total):
        to_throw = None
        error = None
        file = open(os.path.join(os.getcwd(),f_name), 'r')
        count = 0
        while True:
            count += 1
            # Get next line from file
            line = file.readline().strip()
            print("Line{}: {}".format(count, line.strip()))
            self.check_line(line,valor_total,count)
            # if line is empty
            # end of file is reached
            if not line:
                break
        file.close()

    def check_line(self,line,valor_total,count):
        line=line.replace(" ","")
        cells=line.split(";")
        weight=None
        expected=None
        cell_coords=None
        if count==1:
            expected=["1","=1+2","=10/(2+3)","=A1*10-5","=(A5*4)/(A2+A2)","=100/(A5+(A5*A5/5))" \
                ,"=(A5*4)/(A2+A2)+SUMA(1,2,3,4,5)","=(A5*4)/(A2+A2)+SUMA(A1,A2,3,4,5)" \
                ,"=(A5*4)/(A2+A2)+SUMA(A1,A2,3,4,5,A6:A12)","=(A5*4)/(A2+A2)+SUMA(A1,A2,3,4,5,A6:A12,MIN(A13:A20))"]
            cell_coords=["A1","B1","C1","D1","E1","F1","G1","H1","I1","J1"]
            weight=0.7
        elif count==2:
            expected=["2","10"]
            cell_coords=["A2","B2"]
            weight=0.05
        elif count==3:
            expected=["3","","30"]
            cell_coords=["A3","B3","C3"]
            weight=0.05
        elif count==4:
            expected=["4","","","8"]
            cell_coords=["A4","B4","C4","D4"]
            weight=0.05
        elif count==5:
            expected=["5","","","","20"]
            cell_coords=["A5","B5","C5","D5","E5"]
            weight=0.05
        elif count==6:
            expected=["6","","","","","40"]
            cell_coords=["A6","B6","C6","D6","E6","F6"]
            weight=0.05
        elif count==7:
            self.checkEmptyLine(7,cells,0.05*valor_total)
            return
        self.checkRow(count,expected,cell_coords,cells,weight*valor_total)


    def checkEmptyLine(self,num_row,cells,valor):
        to_throw = None
        error = None
        print("\tChecking line " + str(num_row) + " of the file")
        try:
            empty=True
            for cell in cells:
                if len(cell)!=0:
                    empty=False
                    break
            error=self.sAssertTrue(empty,valor,"Line 7 of the file should not contain any value. However "\
                                     +"it contains some non-empty value for some cell")
            to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()

    def checkRow(self,num_row,expected,cell_coords,cells,valor):
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\tChecking line " + str(num_row) + " of the file. Value: " + str(valor))
        try:
            num_tests = 1 + len(expected)
            count=0
            error=self.sAssertEquals(len(expected),len(cells),valor/num_tests,"The expected number of non-emtpy cells is " \
                                     + str(len(expected))+", but the actual number of non-empty cells is " \
                                     +str(len(cells)))
            for cell in cells:
                error=self.sAssertEquals(expected[count],cell,valor/num_tests,"Cell " + cell_coords[count] \
                                         + " contained " + expected[count] +" but the file contains " + cell + " at the position corresponding to this cell")
                to_throw=self.toThrow(error,to_throw)
                count+=1

        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)
