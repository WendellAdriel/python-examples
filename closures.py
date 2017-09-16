def transmit_to_space(message):
    def data_transmitter():
        print(message)

    data_transmitter()

transmit_to_space("Test message")

def print_msg(number):
    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)

print_msg(9)

def transmit(message):
    def data_transmitter():
        print(message)
    
    return data_transmitter

func = transmit("Burn the Sun!")
func()