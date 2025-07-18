from interface.cli_interface import show_menu, get_choice, invalid_choice, show_message
from controllers import controller

def main():
    while True:
        show_menu()
        try:
            choice=int(get_choice())
        except ValueError:
            invalid_choice()
            continue
        if choice==1:
            controller.add_new_job()
        elif choice==2:
            controller.view_jobs()
        elif choice== 3:
            controller.update_status()
        elif choice == 4:
            controller.delete_job()
        elif choice == 5:
            controller.summary_count()
        elif choice == 6:
            controller.search_jobs()
        elif choice == 7:
            show_message ("Exiting Job Tracker. Goodbye !")
            break
        else :
            invalid_choice()
            
if __name__=="__main__":
    main()
