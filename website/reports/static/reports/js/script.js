        var categorySelect = addpub.category;
        var checkBox1 = document.getElementById("monograph_check");
        var checkBox2 = document.getElementById("collective_monograph");
        var checkBox3 = document.getElementById("professional_publication");
        var checkBox4 = document.getElementById("foreign_editions");
        var checkBox5 = document.getElementById("mnbd_publications");
        var checkBox6 = document.getElementById("foreign_authors");
        var checkBox7 = document.getElementById("publications_with_students");
        var checkBox8 = document.getElementById("published");
        var checkBox9 = document.getElementById("ready_for_print");

        function Select() {
        var selectedOption = categorySelect.options[categorySelect.selectedIndex];
        if (selectedOption.text == "Монографія"){
            checkBox1.style.display = "block";
            checkBox2.style.display = "block";
            checkBox3.style.display = "none";
            checkBox4.style.display = "none";
            checkBox5.style.display = "none";
            checkBox6.style.display = "none";
	        checkBox7.style.display = "none";
            checkBox8.style.display = "none";
            checkBox9.style.display = "none";
            }
        if (selectedOption.text == "Стаття"){
            checkBox1.style.display = "none";
            checkBox2.style.display = "none";
            checkBox3.style.display = "block";
            checkBox4.style.display = "block";
            checkBox5.style.display = "block";
            checkBox6.style.display = "block";
	        checkBox7.style.display = "block";
            checkBox8.style.display = "block";
            checkBox9.style.display = "block";
            }
	if (selectedOption.text == "Підручник"){
            checkBox1.style.display = "none";
            checkBox2.style.display = "none";
            checkBox3.style.display = "none";
            checkBox4.style.display = "none";
            checkBox5.style.display = "none";
            checkBox6.style.display = "none";
	        checkBox7.style.display = "none";
            checkBox8.style.display = "none";
            checkBox9.style.display = "none";
            }
	if (selectedOption.text == "Навчальний посібник"){
            checkBox1.style.display = "none";
            checkBox2.style.display = "none";
            checkBox3.style.display = "none";
            checkBox4.style.display = "none";
            checkBox5.style.display = "none";
            checkBox6.style.display = "none";
	        checkBox7.style.display = "none";
            checkBox8.style.display = "none";
            checkBox9.style.display = "none";
            }
	if (selectedOption.text == "Інший вид публікації"){
            checkBox1.style.display = "none";
            checkBox2.style.display = "none";
            checkBox3.style.display = "none";
            checkBox4.style.display = "none";
            checkBox5.style.display = "none";
            checkBox6.style.display = "none";
	        checkBox7.style.display = "none";
            checkBox8.style.display = "none";
            checkBox9.style.display = "none";
            }
	if (selectedOption.text == "Тези"){
            checkBox1.style.display = "none";
            checkBox2.style.display = "none";
            checkBox3.style.display = "none";
            checkBox4.style.display = "block";
            checkBox5.style.display = "block";
            checkBox6.style.display = "block";
	        checkBox7.style.display = "block";
            checkBox8.style.display = "block";
            checkBox9.style.display = "block";
            }
	}

        categorySelect.addEventListener("change", Select);