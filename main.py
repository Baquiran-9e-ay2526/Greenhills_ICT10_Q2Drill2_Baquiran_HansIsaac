from pyscript import document

grade7 = {"Emilio Aguinaldo", "Antonio Luna", "Manuel Quezon", "Rodrigo Duterte"}
grade8 = {"Thea Correa", "Reign Macachor", "Franco Garica", "Ethan Valerio"}
grade9 = {"Rico Gozum", "Oshri Gonzales", "Jamielle Orduna", "Renzo Madrono", "David Valeriano", "Ramon Santiago"}
grade10 = {"Hans Baquiran", "Zarina Perez", "Nathan Bautista", "Aiva Suson", "Maryam Ledesma", "Zoe Reyes"}

def add_member(event):
    first_name = document.getElementById("1name").value
    last_name = document.getElementById("2name").value
    
    new_member = {first_name + " " + last_name}
    
    # Combine sets using union operator (|)
    master_set = grade7 | grade8 | grade9 | grade10 | new_member
    
    # Convert to sorted list and join with <br> to list each name on a new line without quotes
    sorted_members = sorted(list(master_set))
    members_list_html = "<br>".join(sorted_members)
    
    # Format final innerHTML output
    output_html = f"All members:<br>{members_list_html}<br><br>Total members: {len(master_set)}"
    
    # Output to the page
    document.getElementById("output").innerHTML = output_html