
var subjectObject = {
  "Ernamkulam": {
    "Kalamassery":[],
    "Angamaly":[],
    "Aluva":[],"Eloor":[],"Thrikkakara":[]
  },
  "Thrissur": {
    "Wadakkancherry":[],
    "Chalakudy":[],"Guruvayoor":[],"Kunnamkulam":[],"Irinjalakuda":[]
  },
  "Thiruvananthapuram":{
  "Varkala":[],"Kattakada":[],"Neyyattinkara":[],"Nedumangadu":[]
  },
  "Kozhikode": {
  "Feroke":[],"koyilandy":[],"Mukkam":[],"Payyoli":[],"Ramanattukara":[]
  },
  "Kannur": {
  "Payyannur":[],"Thalasseri":[],"Mattannur":[],"Anthur":[]
  }
}

window.onload = function() {
  var subjectSel = document.getElementById("district");
  var topicSel = document.getElementById("branch");

  for (var x in subjectObject) {
    subjectSel.options[subjectSel.options.length] = new Option(x, x);
  }

  subjectSel.onchange = function() {

  topicSel.length = 1;
    //display correct values
    for (var y in subjectObject[this.value]) {
      topicSel.options[topicSel.options.length] = new Option(y, y);
    }
  }
}
