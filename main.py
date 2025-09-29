from pyscript import display, document



def sample_function(e):
    data1 = document.getElementById('input1').value
    data2 = document.getElementById('input2').value
    data3 = document.getElementById('input3').value

    message =  f'''
    Student\'s Profile

    Name: {data1}\n
    Age: {data2}\r
    School: {data3}\r

    {data1} is a {data2}yr old student who studies at {data3}.
    ''' 
    display (f'{message}',  target='output')