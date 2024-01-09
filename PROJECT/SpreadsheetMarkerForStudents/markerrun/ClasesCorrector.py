# -*- coding: utf-8 -*-
import unittest

class SuperClassForTests(unittest.TestCase):

    showPrints = True
    someError = False
    someExceptionInTestedCode = False
    thrownExceptions = {} # is a Map<String, List<AssertionError>>
    errorsByClass  = {} # is a Map<String, List<AssertionError>> 
    puntosTotales = 0.0 # is a double
    creditsPrinted = False;
    indErrors = [] #errors in one class
    accErrors = [] #accummulated errors
    #nota  #is a map <String (nombre clase), float (nota de la corrección de la clase)>
    # nota = {}
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        #Presentar créditos
        if not SuperClassForTests.creditsPrinted:
            SuperClassForTests.showCredits()
            SuperClassForTests.creditsPrinted = True
        '''
        Si no se había creado la lista de errores para la clase prueba, crerala 
        y añadir la entrada en el mapa 
        '''
        className = type(self).__name__
        self.indErrors = SuperClassForTests.errorsByClass.get(className)
        SuperClassForTests.errorsByClass[className] = SuperClassForTests.indErrors
        self.exceptionsList = SuperClassForTests.thrownExceptions.get(className)
        if self.exceptionsList == None:
            self.exceptionsList = []
            SuperClassForTests.thrownExceptions[className] = self.exceptionsList

    def acumula(self,punts):
        SuperClassForTests.puntosTotales = SuperClassForTests.puntosTotales + punts

    def acumulaErrores():
        for error in SuperClassForTests.indErrors:
            SuperClassForTests.accErrors.append(error)

    def puntosAntesDespues(self,puntosAntes: float):
        print(f"\t\tPuntos obtenidos: {round(SuperClassForTests.puntosTotales-puntosAntes,3)}\
. Puntos acumulados: {round(SuperClassForTests.puntosTotales,3)}")

    def addError(self,err: AssertionError):
        if err!=None:
            SuperClassForTests.indErrors.append(err)
            SuperClassForTests.someError = True

    def tryToGetMessageFromAssertionError(self,t: AssertionError):       
        if t!=None:
            return str(t)
        return ""

    def toThrow(self,newT, oldT):
        if newT != None:
            return newT
        if oldT != None:
            return oldT
        return None

    def sAssertTrue(self,asserted: bool,puntos: float, errorMssg):
        try:
            self.assertTrue(asserted)
            self.acumula(puntos)
        except AssertionError as ex:
            addendum = self.tryToGetMessageFromAssertionError(ex)
            print(f"\t\t{errorMssg}; {addendum}")
            newT = AssertionError(errorMssg + "; " + addendum)
            self.addError(newT)
            return newT
        return None

    def sAssertFalse(self,asserted: bool,puntos: float, errorMssg):
        try:
            self.assertFalse(asserted)
            self.acumula(puntos)
        except AssertionError as ex:
            addendum = self.tryToGetMessageFromAssertionError(ex)
            print(f"\t\t {errorMssg}; {addendum}")
            newT = AssertionError(errorMssg + "; " + addendum)
            self.addError(newT)
            return newT
        return None

    def sAssertNone(self,asserted,puntos: float, errorMssg):
        try:
            self.assertIsNone(asserted)
            self.acumula(puntos)
        except AssertionError as ex:
            addendum = self.tryToGetMessageFromAssertionError(ex)
            print(f"\t\t {errorMssg}; {addendum}")
            newT = AssertionError(errorMssg + "; " + addendum)
            self.addError(newT)
            return newT
        return None

    def sAssertNotNone(self,asserted,puntos: float, errorMssg):
        try:
            self.assertIsNotNone(asserted)
            self.acumula(puntos)
        except AssertionError as ex:
            addendum = self.tryToGetMessageFromAssertionError(ex)
            print(f"\t\t {errorMssg}; {addendum}")
            newT = AssertionError(errorMssg + "; " + addendum)
            self.addError(newT)
            return newT
        return None

    def sAssertEquals(self,expected, value,puntos: float, errorMssg):
        try:
            self._baseAssertEqual(expected,value)
            # self.assertEqual(expected,value)
            self.acumula(puntos)
        except AssertionError as ex:
            addendum = self.tryToGetMessageFromAssertionError(ex)
            print(f"\t\t {errorMssg}; {addendum}")
            newT = AssertionError(errorMssg + "; " + addendum)
            self.addError(newT)
            return newT
        return None
    
    def checkFieldExists(self,fieldName,obj,puntos,toThrow)->AssertionError:
        if hasattr(obj,fieldName):
            SuperClassForTests.puntosTotales = SuperClassForTests.puntosTotales \
                + puntos
            return None
        mssg = "ERROR en el atributo \'" + fieldName \
               + "\'. No existe. Debe declararse ese atributo con ese nombre"
        print("\t\t"+mssg)
        newT = AssertionError(mssg)
        self.addError(newT)
        return newT

    def checkObjectIsOfASpecificClass(self,obj,expectedClass,puntos,toThrow)->AssertionError:
        if type(obj)==expectedClass:
            SuperClassForTests.puntosTotales = SuperClassForTests.puntosTotales  + puntos
            return None
            mssg = "ERROR al comprobar la clase delo objeto pasado, ya que no es de la clase esperada. "\
                + "Debería ser de clase " + (expectedClass).__name__ + " pero es de clase " + type(obj).__name__
            print("\t\t"+mssg)
            newT = AssertionError(mssg)
            self.addError(newT)
            return newT

    def checkFieldIsOfASpecificClass(self,fieldName,obj,fieldClass,puntos,toThrow)->AssertionError:
        if hasattr(obj,fieldName):
            # print(f"\t\tEl atributo {fieldName} debería ser de tipo {fieldClass}")
            # print(f"\t\tEl atributo {fieldName} es de tipo {type(getattr(obj, fieldName))}")
            if type(getattr(obj, fieldName))==fieldClass:
                SuperClassForTests.puntosTotales = SuperClassForTests.puntosTotales \
                    + puntos
                return None
            mssg = "ERROR en el atributo \'" + fieldName +"\'. " \
                   + "No es de la clase esperada. Debería ser de clase " \
                   + (fieldClass).__name__ + " pero es de clase " \
                   + type(getattr(obj, fieldName)).__name__
            print("\t\t"+mssg)
            newT = AssertionError("ERROR en el atributo \'" + fieldName +"\'. "\
                + "No es de la clase esperada. Debería ser de clase " \
                + (fieldClass).__name__ + " pero es de clase " \
                + type(getattr(obj, fieldName)).__name__)
            self.addError(newT)
            return newT
        newT = AssertionError(f"ERROR en el atributo \'{fieldName}. La "\
            + "clase debería tener dicho atributo, pero no lo tiene")
        self.addError(newT)
        return newT
        
    def checkFieldValue(self,fieldName,obj,value,puntos,toThrow)->AssertionError:
        err = self.checkFieldIsOfASpecificClass(fieldName, obj, type(value), 0, toThrow)
        attr = getattr(obj, fieldName)
        if err==None:
            if attr==value:
                SuperClassForTests.puntosTotales = SuperClassForTests.puntosTotales \
                    + puntos                    
                return None
            mssg = "ERROR en el atributo \'"+ fieldName + "\'. Su " \
                   + "valor debería ser "+ str(value) + ", pero es " + str(attr)
            print("\t\t"+mssg)
            newT = AssertionError(mssg)
            self.addError(newT)
            return newT
        return err
    
    def showCredits():
        print(
        "***********************************************************\n" \
        +"* La clase SuperClassForTests ha sido desarrollada por    *\n" \
        +"* Juan Carlos Cruellas. Se prohibe su utilización en todo *\n" \
        +"* programa distinto al corrector del proyecto de la       *\n" \
        +"* asignatura Software Architecture de la ETSETB, sin el   *\n" \
        +"* permiso otorgado por escrito de Juan Carlos Cruellas.   *\n" \
        +"***********************************************************\n"
        );

    def areThereErrors():
        return SuperClassForTests.someError;
    
    def getErrorsByClass()->{}:
        return SuperClassForTests.errorsByClass
    
    def showErrors(indErrors:[],className:str):
        if indErrors:
            print("\n\nResumen de errores en " + className)
            for assertion in indErrors:
                print("\t"+str(assertion))
    
    def showAlldErrors():
        if SuperClassForTests.accErrors:
            print("\n\nResumen de ERRORES en la corrección" )
            for assertion in SuperClassForTests.accErrors:
                print("\t"+str(assertion))
                
    def printIfOK(error):
        if error == None:
            print("\t\tOK");

    def throwIfAnError(self,t: AssertionError):
        if t!=None:
            raise t




