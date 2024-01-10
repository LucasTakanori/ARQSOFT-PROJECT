import traceback
from markerrun.ClasesCorrector import SuperClassForTests
from usecasesmarker.spread_sheet_factory_for_checker import SpreadSheetFactoryForChecker
from entities.circular_dependency_exception import CircularDependencyException


class CircularDependenciesTest(SuperClassForTests):

    numErrorsBefore = 0;

    numInstances = 0;

    nota = 0.0

    def __init__(self,*args, **kwargs):
        SuperClassForTests.__init__(self, *args, **kwargs)
        CircularDependenciesTest.numInstances = CircularDependenciesTest.numInstances + 1
        self.instance=SpreadSheetFactoryForChecker.create_spreadsheet_controller()
        if CircularDependenciesTest.numInstances == 1:
            CircularDependenciesTest.numErrorsBefore = len(SuperClassForTests.indErrors)
        try:
            self.instance.set_cell_content("A6", "1")
            self.instance.set_cell_content("A7", "2")
            self.instance.set_cell_content("A8", "3")
            self.instance.set_cell_content("A9", "4")
            self.instance.set_cell_content("A10", "5")
            self.instance.set_cell_content("A11", "6")
            self.instance.set_cell_content("A12", "7")
            self.instance.set_cell_content("A13", "8")
            self.instance.set_cell_content("A14", "9")
            self.instance.set_cell_content("A1", "=A2+A3+A4+A5")
            self.instance.set_cell_content("A2", "=A6+A7+A8")
            self.instance.set_cell_content("A3", "=A9+A10+A11")
            self.instance.set_cell_content("A4", "=A12+A13")
            self.instance.set_cell_content("A5", "=A14+1")
        except Exception as err:
            print("An error has occurred while trying to set either "
                  + "a numerical or a formula content in one cell. You should "
                  + "review your code as this should not happen. Details "
                  + "of the exception follow: " + str(err));
            traceback.print_exc()

    def setUpClass():
        # SuperClassForTests.nota = {}
        CircularDependenciesTest.nota = 0.0
        print("\nMarking detection of circular dependencies (CircularDependenciesTest)")
        print("***********************")

    def tearDownClass():
        SuperClassForTests.showErrors(SuperClassForTests.indErrors, "CircularDependencies")
        SuperClassForTests.acumulaErrores()
        SuperClassForTests.indErrors = []
        CircularDependenciesTest.nota = SuperClassForTests.puntosTotales
        SuperClassForTests.puntosTotales = 0;

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test01_direct_circular_dependency(self):
        valor_total = 4
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nChecking that the program detects direct circular dependencies. Value: " + str(valor_total))
        cell_str="A2"
        try:
            content = self.instance.get_cell_content_as_float("A2")
            error = self.sAssertEquals(6.0,content,0,"The cell " + cell_str \
                                       + " should contain the value: 6 -result of formula =A6+A7+A8, when A6=1, A7=2, and A8=3- Instead, it contains the value " + str(content))
            to_throw=self.toThrow(error,to_throw)
            try:
                self.instance.set_cell_content("A2","=A1+A7+A8")
                content = self.instance.get_cell_content_as_float("B1")
                error = self.sAssertTrue(False,0,"Cell A1 contains the formula =A2+A3+A4+A5, and now a try has been done to " \
                                         +"set cell A2 to =A1+A7+A8. This introduces a direct circular dependency that your program should have detected and the " \
                                         + "corresponding CircularDependencyException should have been trhown. Instead no exception has been thrown")
            except CircularDependencyException as err:
                error = self.sAssertTrue(True,valor_total,"")
                to_throw=self.toThrow(error,to_throw)
            except Exception as err:
                error = self.sAssertTrue(False,0,"Cell A1 contains the formula =A2+A3+A4+A5, and now a try has been done to "\
                    +"set cell A2 to =A1+A7+A8. This introduces a direct circular dependency that your program should have detected and the "\
                    + "corresponding CircularDependencyException should have been trhown. Instead a " + err.__class__.__name__ + " has been thrown")
                to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        self.puntosAntesDespues(puntos_antes)

    def test02_indirect_circular_dependency(self):
        valor_total = 6
        to_throw = None
        error = None
        puntos_antes = SuperClassForTests.puntosTotales
        print("\nChecking that the program detects indirect circular dependencies. Value: " + str(valor_total))
        try:
            print("\tCase 1: a change is introduced in a cell that does not introduce a circular dependency. Value: " + str(valor_total*0.3))
            try:
                self.instance.set_cell_content("A11","=A2+A5")
                error = self.sAssertTrue(True, valor_total * 0.3, "")
                to_throw=self.toThrow(error,to_throw)
            except CircularDependencyException as err:
                error = self.sAssertTrue(False,0,"Cell A2 contains the formula =A6+A7+A8, and now a try has been done to "\
                    +"set cell A11 to =A2+A5. This does not introduce any circular dependency, BUT your program has thrown "\
                    +"an exception notifying a circular dependency")
                to_throw=self.toThrow(error,to_throw)
            except Exception as err:
                error = self.sAssertTrue(False,0,"Cell A2 contains the formula =A6+A7+A8, and now a try has been done to " \
                                         +"set cell A11 to =A2+A5. This does not introduce any circular dependency, BUT your program has thrown " \
                                         +"an exception " + err.__class__.__name__ )
                to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        try:
            print("\tCase 2: a change is introduced in a cell that does introduce a circular dependency. Value: " + str(valor_total*0.35))
            try:
                self.instance.set_cell_content("A11","=A1+A5")
                error = self.sAssertTrue(False,0,"Cell A1 contains the formula =A2+A3+A4+A5, cel A3 contains the formula " \
                                         +"=A9+A10+A11, and now a try has been made to set cell A11 to =A1+5. This introduces a circular dependency, BUT your program HAS NOT thrown " \
                                         +"an exception notifying a circular dependency")
                to_throw=self.toThrow(error,to_throw)
            except CircularDependencyException as err:
                error = self.sAssertTrue(True, valor_total * 0.35, "")
                to_throw=self.toThrow(error,to_throw)
            except Exception as err:
                error = self.sAssertTrue(False,0,"Cell A1 contains the formula =A2+A3+A4+A5, cell A3 contains the formula " \
                                         +"=A9+A10+A11, and now a try has been made to set cell A11 to =A1+5. This introduces a circular dependency, BUT your program HAS thrown " \
                                         +"an exception " + err.__class__.__name__ + " instead CircularDependencyException")
                to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()
        try:
            print("\tCase 3: another change is introduced in a cell that does introduce a circular dependency. Value: " + str(valor_total*0.35))
            try:
                self.instance.set_cell_content("A6","=A1+A5")
                error = self.sAssertTrue(False,0,"Cell A1 contains the formula =A2+A3+A4+A5, cell A2 contains the formula " \
                                         +"=A6+A7+A8, and now a try has been made to set cell A6 to =A1+5. This introduces a circular dependency, BUT your program HAS NOT thrown " \
                                         +"an exception notifying a circular dependency")
                to_throw=self.toThrow(error,to_throw)
            except CircularDependencyException as err:
                error = self.sAssertTrue(True, valor_total * 0.35, "")
                to_throw=self.toThrow(error,to_throw)
            except Exception as err:
                error = self.sAssertTrue(False,0,"Cell A1 contains the formula =A2+A3+A4+A5, cell A2 contains the formula " \
                                         +"=A6+A7+A8, and now a try has been made to set cell A6 to =A1+5. This introduces a circular dependency, BUT your program has thrown " \
                                         +"an exception " + err.__class__.__name__ + " instead CircularDependencyException")
                to_throw=self.toThrow(error,to_throw)
        except  Exception as err:
            print("*** An exception has been caught that likely has been thrown by your code. " \
                  +"Check the trace for detecting it has been created and raised. Details: " + str(err))
            traceback.print_exc()


        self.puntosAntesDespues(puntos_antes)
