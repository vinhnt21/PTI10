class Film:
    def __init__(self, id, title, release_date, rating, link):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.rating = rating
        self.link = link

    def update(self, new_data: dict):
        for key, value in new_data.items():
            if value:
                setattr(self, key, value)

    def show_infor(self):
        print(
            f"{self.id} - {self.title} - {self.release_date} - {self.rating} - {self.link}"
        )


class Film_Manager:
    def __init__(self, list_films):
        self.list_films = list_films

    def add_film(self):
        id = input("Enter id: ")
        title = input("Enter title: ")
        release_date = input("Enter release date: ")
        rating = input("Enter rating: ")
        link = input("Enter link: ")
        new_film = Film(id, title, release_date, rating, link)
        self.list_films.append(new_film)

    def update_film(self):
        input_id = input("Enter id to update: ")
        for film in self.list_films:
            if film.id == input_id:
                new_data = {}
                title = input("Enter new title: ")
                release_date = input("Enter new release date: ")
                rating = input("Enter new rating: ")
                link = input("Enter new link: ")
                if title:
                    new_data["title"] = title
                if release_date:
                    new_data["release_date"] = release_date
                if rating:
                    new_data["rating"] = rating
                if link:
                    new_data["link"] = link
                film.update(new_data)
                break

    def show_all_films(self):
        for film in self.list_films:
            film.show_infor()

    def remove_film_by_id(self):
        input_id = input("Enter id to remove: ")
        deleted_film = None
        for film in self.list_films:
            if film.id == input_id:
                deleted_film = film
                break
        if deleted_film:
            self.list_films.remove(deleted_film)


film_manager = Film_Manager([])

while True:
    print("*" * 20)
    print("1. Add new film")
    print("2. Update film")
    print("3. Show all films")
    print("4. Remove film by id")
    print("5. Exit")
    print("*" * 20)
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Add new film")
        film_manager.add_film()
    elif choice == "2":
        print("Update film")
        film_manager.update_film()
    elif choice == "3":
        print("Show all films")
        film_manager.show_all_films()
    elif choice == "4":
        print("Remove film by id")
        film_manager.remove_film_by_id()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid choice")
        continue
