class Star_Cinema:
    def __init__(self):
        self.__hall_list = []


    def entry_hall(self, hall):
        self.__hall_list.append(hall)




class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)


    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        list_of_seats = []
        for i in range(1, self.__rows + 1):
            for j in range(1, self.__cols + 1):
                a = (i, j)
                list_of_seats.append(a)
        self.__seats.update({id : list_of_seats})



    def book_seats(self, id, seat):
        a = "you have enter wrong id"
        b = "this seat is already booked"
        c = f'you have booked this {seat} seat'
        d = "your desire seat is not in the list"
        if id not in self.__seats:
            return a
        else:
            row, col = seat
            if row > 10 or row < 1 or col > 10 or col < 1:
                return d
            elif seat not in self.__seats[id]:
                return b
            else:
                self.__seats[id].remove(seat)
                return c

    def view_show_list(self):
        return self.__show_list

    def view_available_seats(self, id):
        a = "you have enter wrong id"
        if id not in self.__seats:
            return a
        else:
            
            return self.__seats[id]
    
print()
hall = Hall(10, 10, 1)

hall.entry_show(111, 'young', '25/10/2023 at 9.30 AM')
hall.entry_show(222, 'young is tan', '25/10/2023 at 3.30 PM')
hall.entry_show(333, 'old is gold', '25/10/2023 at 7.00PM')


while True:
    def start_hall():
        print()
        print('All the options below:')
        print('\t1. View all the show today')
        print('\t2. View available seats')
        print('\t3. Book ticket')
        print('\t4. Exit')

        print()
        option = int(input('Enter your choice: '))



        # option 1 all the show list 
        if option == 1:
            show_list = hall.view_show_list()
            # print(show_list)
            print()
            for show in show_list:
                id, movie_name, time = show
                print(f"ID: {id}, MOVIE NAME: {movie_name}, TIME: {time}")
                print()



        # option 2 to see all the available seats
        elif option == 2:
            print()
            print()
            show_id = int(input('Enter show id: '))
            available_seats = hall.view_available_seats(show_id)
            if isinstance(available_seats, list):
                for seat in available_seats:
                    print(f"seat: {seat}")
            else:
                print(available_seats)



        # option 3 for booking a tickets
        elif option == 3:
            print()
            print()
            id = int(input('Enter show id: '))
            row = int(input('Enter row no: '))
            col = int(input('Enter col no: '))
            seat = (row, col)
            print()
            a = hall.book_seats(id, seat)
            print(a)
            print()

        
        # option 4 for exiting
        elif option == 4:
            exit()

        # option 5 for other value
        else:
            print('you have enter wrong option')
    
    start_hall()