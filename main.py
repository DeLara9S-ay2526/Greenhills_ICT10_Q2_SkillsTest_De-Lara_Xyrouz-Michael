from pyscript import display, document


def find(e):

    document.getElementById('result').innerHTML = " "

    input = document.getElementById('element').value.title().strip()
    element = {
        'H':{
            'Symbol': 'H',
            'Name':'Hydrogen',
            'Atomic Number':'1',
            'Atomic Mass':'1.0080'
        },
        'He':{
            'Symbol': 'He',
            'Name':'Helium',
            'Atomic Number':'2',
            'Atomic Mass':'4.0026'
        },
        'C':{
            'Symbol': 'C',
            'Name':'Carbon',
            'Atomic Number':'6',
            'Atomic Mass':'12.011'
        },
        'N':{
            'Symbol':'N',
            'Name':'Nitrogen',
            'Atomic Number':'7',
            'Atomic Mass':'14.007'
        },
        'O':{
            'Symbol':'O',
            'Name':'Oxygen',
            'Atomic Number':'8',
            'Atomic Mass':'15.999'
        },
        'F':{
            'Symbol':'F',
            'Name':'Fluorine',
            'Atomic Number':'9',
            'Atomic Mass':'18.998'
        },
        'Ne':{
            'Symbol':'Ne',
            'Name':'Neon',
            'Atomic Number':'10',
            'Atomic Mass':'20.180'
        },
        'P':{
            'Symbol':'P',
            'Name':'Phosphorus',
            'Atomic Number':'15',
            'Atomic Mass':'30.984'
        },
        'S':{
            'Symbol':'S',
            'Name':'Sulfur',
            'Atomic Number':'16',
            'Atomic Mass':'32.06'
        },
        'Cl':{
            'Symbol':'Cl',
            'Name':'Chlorine',
            'Atomic Number':'17',
            'Atomic Mass':'35.45'
        },
        'Ar':{
            'Symbol':'Ar',
            'Name':'Argon',
            'Atomic Number':'18',
            'Atomic Mass':'39.95'
        },
        'Se':{
            'Symbol':'Se',
            'Name':'Selenium',
            'Atomic Number':'34',
            'Atomic Mass':'78.971',
        },
        'Br':{
            'Symbol':'Br',
            'Name':'Bromine',
            'Atomic Number':'35',
            'Atomic Mass':'79.904',
        },
        'Kr':{
            'Symbol':'Kr',
            'Name':'Krypton',
            'Atomic Number':'36',
            'Atomic Mass':'83.798',
        },
        'I':{
            'Symbol':'I',
            'Name':'Iodine',
            'Atomic Number':'53',
            'Atomic Mass':'126.90',
        },
        'Xe':{
            'Symbol':'Xe',
            'Name':'Xenon',
            'Atomic Number':'54',
            'Atomic Mass':'131.29',
        },
        'Rn':{
            'Symbol':'Rn',
            'Name':'Radon',
            'Atomic Number':'86',
            'Atomic Mass':'No Stable Isotope',
        },
    }
    elem_check = input in element
    elem_check2 = (element[input])
    mssg_disp = (f'{input} is not a nonmetal element.', f'{elem_check2}')

    display(mssg_disp[elem_check], target='result')