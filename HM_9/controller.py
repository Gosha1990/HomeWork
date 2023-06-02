import viev
import model
import text


def start():
    global concurrent_id, index
    while True:
        choice = viev.main_menu()

        match choice:
            case 1:
                model.open_pb()
                viev.print_message(text.load_successful)

            case 2:
                model.save_pb9()
                viev.print_message(text.save_successful)
            case 3:
                pb = model.get_pb()
                viev.print_contact(pb, text.pb_empty)
            case 4:
                contact = viev.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                viev.print_message(text.new_contact_successful(name))
            case 5:
                key_word = viev.input_search(text.input_search)
                result = model.search_contact(key_word)
                viev.print_contact(result, text.empty_search(key_word))
            case 6:
                key_word = viev.input_search(text.input_change)
                result = model.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        viev.print_contact(result, '')
                        concurrent_id = viev.input_search(text.input_index)
                    else:
                        concurrent_id = result[0].get('id')
                    new_contact = viev.input_contact(text.change_contact)
                    name = model.change_contact(new_contact, concurrent_id)
                    viev.print_message(text.change_succ(name))
                else:
                    viev.print_message(text.empty_search(key_word))
            case 7:
                pb = model.get_pb()
                viev.print_contact(pb, text.pb_empty)
                if pb:
                    index = viev.input_in(pb, text.input_index)
                if pb[index - 1].get('name'):
                    model.delet_contakt(index)
                    viev.print_message(text.delet_cont)

            case 8:
                break
