
const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
var progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const formSteps1 = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".ms-tabs");
const progressStepsclick = document.querySelectorAll(".count");

const step1 = document.getElementById("fs1");
const step2 = document.getElementById("fs2");
const step3 = document.getElementById("fs3");
const step4 = document.getElementById("fs4");
const step5 = document.getElementById("fs5");
const step6 = document.getElementById("fs6");
var tab1 = document.getElementById("tab1");
var tab2 = document.getElementById("tab2");
var tab3 = document.getElementById("tab3");
var tab4 = document.getElementById("tab4");
var tab5 = document.getElementById("tab5");
var tab6 = document.getElementById("tab6");
var count1 = document.getElementById("count1");
var count2 = document.getElementById("count2");
var count3 = document.getElementById("count3");
var count4 = document.getElementById("count4");
var count5 = document.getElementById("count5");
var next1 = document.getElementById("next1");
var next2 = document.getElementById("next2");
var next3 = document.getElementById("next3");
var next4 = document.getElementById("next4");
var next5 = document.getElementById("next5");
var prev1 = document.getElementById("prev1");
var prev2 = document.getElementById("prev2");
var prev3 = document.getElementById("prev3");
var prev4 = document.getElementById("prev4");
var prev5 = document.getElementById("prev5");
var manual = document.getElementById("EMaddress");
var manualadrs = document.querySelector(".manualaddress");
var manualclose = document.querySelector(".addrschoice1");
var manualopen = document.querySelector(".addrschoice");


// var x = document.forms["registervenue"]["vname"].value;
//   if (x == "") {
//       document.getElementById('tab1').style.background = 'green';

//   };


let formStepsNum = 0;

nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum++;
    updateFormSteps();
    updateProgressbar();

  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
    updateProgressbar();
  });
});

next1.addEventListener("click", () => {

  count1.classList.add("progress-steponclick");
  ManageVenueName();


});
manual.addEventListener("click", () => {
  manualadrs.style.display = 'flex';
  manualopen.style.display = "none";
  manualclose.style.display = "flex";
});


manualclose.addEventListener("click", () => {
  manualclose.style.display = "none";
  manualopen.style.display = "flex";
  manualadrs.style.display = "none";
})

next2.addEventListener("click", () => {

  count1.classList.add("progress-steponclick");
  count2.classList.add("progress-steponclick");
  ManageVenueType();

});

next3.addEventListener("click", () => {

  count1.classList.add("progress-steponclick");
  count2.classList.add("progress-steponclick");
  count3.classList.add("progress-steponclick");

  ManageCuisineType();

});

next4.addEventListener("click", () => {

  count1.classList.add("progress-steponclick");
  count2.classList.add("progress-steponclick");
  count3.classList.add("progress-steponclick");
  count4.classList.add("progress-steponclick");

  ManageHrsOperations();

});

next5.addEventListener("click", () => {

  count1.classList.add("progress-steponclick");
  count2.classList.add("progress-steponclick");
  count3.classList.add("progress-steponclick");
  count4.classList.add("progress-steponclick");
  count5.classList.add("progress-steponclick");

  ManageContactPerson();

});

// Save button field validation
var subsave = document.getElementById('subsave');
subsave.addEventListener("click", () => {

  ManageUserPass();
  ManageContactPerson();
  ManageHrsOperations();
  ManageCuisineType();
  ManageVenueType();

})

// -----------------------------------


prev1.addEventListener("click", () => { 
  ManageVenueType();
});

prev2.addEventListener("click", () => {
  ManageCuisineType();

});
prev3.addEventListener("click", () => {
  ManageHrsOperations();
});

prev4.addEventListener("click", () => {   
  ManageContactPerson();

});

prev5.addEventListener("click", () => {
  ManageUserPass();
});

function updateFormSteps() {
  formSteps1.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  formSteps1[formStepsNum].classList.add("form-step-active");
}

function updateProgressbar() {
  progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum + 1) {
      progressStep.classList.add("ms-tabs-active");
    } else {
      progressStep.classList.remove("ms-tabs-active");
    }
  });

  const progressActive = document.querySelectorAll(".ms-tabs-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}

// const pSteps = document.querySelectorAll(".ms-tabs");


tab1.addEventListener("click", () => {
  formStepsNum = 0;
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  progressSteps.forEach((mstabs) => {
    mstabs.classList.contains("ms-tabs-active") &&
      mstabs.classList.remove("ms-tabs-active");
  });

  step1.classList.add("form-step-active");

  tab1.classList.add("ms-tabs-active");
  // count1.classList.remove("progress-steponclick");
  // count2.classList.remove("progress-steponclick");

  // count3.classList.remove("progress-steponclick");
  // count4.classList.remove("progress-steponclick");
  // count5.classList.remove("progress-steponclick");


  const progressActive = document.querySelectorAll(".ms-tabs-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";

 

})

tab2.addEventListener("click", () => {
  formStepsNum = 1;
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  progressSteps.forEach((mstabs) => {
    mstabs.classList.contains("ms-tabs-active") &&
      mstabs.classList.remove("ms-tabs-active");
  });

  step2.classList.add("form-step-active");
  tab1.classList.add("ms-tabs-active");
  tab2.classList.add("ms-tabs-active");
  count1.classList.add("progress-steponclick");
  // count2.classList.remove("progress-steponclick");
  // count3.classList.remove("progress-steponclick");
  // count4.classList.remove("progress-steponclick");
  // count5.classList.remove("progress-steponclick");

  const progressActive = document.querySelectorAll(".ms-tabs-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";

  ManageVenueName(); 
 
})

tab3.addEventListener("click", () => {
  formStepsNum = 2;
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  progressSteps.forEach((mstabs) => {
    mstabs.classList.contains("ms-tabs-active") &&
      mstabs.classList.remove("ms-tabs-active");
  });

  step3.classList.add("form-step-active");
  tab1.classList.add("ms-tabs-active");
  tab2.classList.add("ms-tabs-active");
  tab3.classList.add("ms-tabs-active");
  count2.classList.add("progress-steponclick");

  count1.classList.add("progress-steponclick");



  // count3.classList.remove("progress-steponclick");
  // count4.classList.remove("progress-steponclick");
  // count5.classList.remove("progress-steponclick");


  const progressActive = document.querySelectorAll(".ms-tabs-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";

  ManageVenueType();  


})

tab4.addEventListener("click", () => {
  formStepsNum = 3;
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  progressSteps.forEach((mstabs) => {
    mstabs.classList.contains("ms-tabs-active") &&
      mstabs.classList.remove("ms-tabs-active");
  });

  step4.classList.add("form-step-active");
  tab1.classList.add("ms-tabs-active");
  tab2.classList.add("ms-tabs-active");
  tab3.classList.add("ms-tabs-active");
  tab4.classList.add("ms-tabs-active");
  count3.classList.add("progress-steponclick");
  count2.classList.add("progress-steponclick");
  count1.classList.add("progress-steponclick");



  // count4.classList.remove("progress-steponclick");
  // count5.classList.remove("progress-steponclick");


  const progressActive = document.querySelectorAll(".ms-tabs-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";

  ManageCuisineType();  
 

})

tab5.addEventListener("click", () => {
  formStepsNum = 4;
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  progressSteps.forEach((mstabs) => {
    mstabs.classList.contains("ms-tabs-active") &&
      mstabs.classList.remove("ms-tabs-active");
  });

  step5.classList.add("form-step-active");
  tab1.classList.add("ms-tabs-active");
  tab2.classList.add("ms-tabs-active");
  tab3.classList.add("ms-tabs-active");
  tab4.classList.add("ms-tabs-active");
  tab5.classList.add("ms-tabs-active");
  count4.classList.add("progress-steponclick");
  count3.classList.add("progress-steponclick");
  count2.classList.add("progress-steponclick");
  count1.classList.add("progress-steponclick");

  // count5.classList.remove("progress-steponclick")


  const progressActive = document.querySelectorAll(".ms-tabs-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";


  ManageHrsOperations();
  
})

tab6.addEventListener("click", () => {
  formStepsNum = 5;
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  progressSteps.forEach((mstabs) => {
    mstabs.classList.contains("ms-tabs-active") &&
      mstabs.classList.remove("ms-tabs-active");
  });

  step6.classList.add("form-step-active");
  tab1.classList.add("ms-tabs-active");
  tab2.classList.add("ms-tabs-active");
  tab3.classList.add("ms-tabs-active");
  tab4.classList.add("ms-tabs-active");
  tab5.classList.add("ms-tabs-active");
  tab6.classList.add("ms-tabs-active");
  count5.classList.add("progress-steponclick")
  count4.classList.add("progress-steponclick")
  count3.classList.add("progress-steponclick")
  count2.classList.add("progress-steponclick")
  count1.classList.add("progress-steponclick")


  const progressActive = document.querySelectorAll(".ms-tabs-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";

  ManageContactPerson(); 

})

var vname = document.getElementById("vpn");
vname.addEventListener('change', () => {

  var username = document.getElementById('vusername').value

  if (username == '' || username != vname.value) {

    document.getElementById('vusername').value = vname.value;
    document.getElementById('vusername').style.borderColor = 'green';
    
  }
})

var vemail = document.getElementById("ea");
vemail.addEventListener('change', () => {

  var cemail = document.getElementById('vemail').value

  if (cemail == '' || cemail != vemail.value) {

    document.getElementById('vemail').value = vemail.value;
    document.getElementById('vemail').style.borderColor = 'green';
  }
 
})

// Js for changing input field border green if it is filled
// --------------------------------------------------------

var form = document.getElementsByClassName('formMulti-step');
console.log(form);
var inputfield = form[0].getElementsByTagName('input');
for(let i=0; i < inputfield.length; i++){
  inputfield[i].addEventListener('change', () => {
    if (inputfield[i].value != ''){
      inputfield[i].style.borderColor = 'green'
    }
  })
}

// -------------------------------------------------------------

const box = document.getElementById('nominatemsg');
const box1 = document.getElementById('notify-method');
const boxn = document.getElementById('wrappershow');
const boxn1 = document.getElementById('wrappershow1');


function handleRadioClick() {
  if (document.getElementById('radio2').checked) {
    box.style.display = 'flex';
    box1.style.display = 'none';
  } else if (document.getElementById('radio1').checked) {
    box1.style.display = 'flex';
    box.style.display = 'none';
    boxn.style.display = 'none';
    boxn1.style.display = 'flex';
    boxn2.style.display = 'flex';
  }
}

const radioButtons = document.querySelectorAll('input[name="selector"]');
radioButtons.forEach(radio => {
  radio.addEventListener('click', handleRadioClick);
});

const box3 = document.getElementById('add-per');
const box4 = document.getElementById('vfields');
const boxn2 = document.getElementById('note');



function handleRadioClick1() {
  if (document.getElementById('y1').checked) {
    box3.style.display = 'flex';
    box1.style.display = 'flex';
    boxn2.style.display = 'flex';
    // box4.style.display = 'none';

  } else if (document.getElementById('n1').checked) {
    box3.style.display = 'none';
    //  box.style.display = 'none';
  }
}


const radioButtons1 = document.querySelectorAll('input[name="add_yes_no"]');
radioButtons1.forEach(radio => {
  radio.addEventListener('click', handleRadioClick1);
});


// tab1.addEventListener("click", function () {
//   document.getElementById("t2").style.background = "red";

// })

$(function () {
  var requiredCheckboxes = $('.venuetype :checkbox[required]');
  requiredCheckboxes.change(function () {
    if (requiredCheckboxes.is(':checked')) {
      requiredCheckboxes.removeAttr('required');
    } else {
      requiredCheckboxes.attr('required', 'required');
    }
  });
});
$(function () {
  var requiredCheckboxes = $('.venuetype1 :checkbox[required]');
  requiredCheckboxes.change(function () {
    if (requiredCheckboxes.is(':checked')) {
      requiredCheckboxes.removeAttr('required');
    } else {
      requiredCheckboxes.attr('required', 'required');
    }
  });
});

function ManageUserPass() {

  var x = document.getElementsByClassName("userpass");
  var y = x[0].getElementsByTagName("input");
  var filled = 0;
  for (i = 0; i < y.length; i++) {

    if (y[i].required) {
      let val = y[i].value; 
      if (val != "") {

        y[i].style.borderColor = "green";
        filled++;

      }
      else if (val == "") {
        y[i].style.borderColor = "red";
      }

    }
  }
  if (filled == 4) 
  {
    document.getElementById('tab6').style.background = '#28a745';

  }
  // else {

  //   Man

  //   // document.getElementById('tab6').style.background = '#da2c46';

  // } 

}

function ManageVenueType() {


  var vt = document.getElementsByClassName("venuetype1");
  var vty = vt[0].getElementsByTagName("input");
  var countcheck = 0;

  for (i = 0; i < vty.length; i++) {
    if (vty[i].checked == true) {
      countcheck++;
    }

  }
  if (countcheck > 0) {

    document.getElementById('tab2').style.background = '#28a745';
    document.querySelector(".vtvalidate").style.display = 'none';
  }
  else if (countcheck == 0) {
    document.querySelector(".vtvalidate").style.display = 'flex';
    // document.getElementById('tab2').style.background = '#da2c46';
  }
}

function ManageCuisineType() {
  var countcheck = 0;
  var vt1 = document.getElementsByClassName("venuetype");
  for (j = 0; j < vt1.length; j++) {
    var vt1y = vt1[j].getElementsByTagName("input");
    for (i = 0; i < vt1y.length; i++) {

      if (vt1y[i].checked == true) {
        countcheck++;
      }
    }
  }
  if (countcheck > 0) {

    document.getElementById('tab3').style.background = '#28a745';
    document.querySelector(".vtvalidate1").style.display = 'none';
  }
  else if (countcheck == 0) {
    document.querySelector(".vtvalidate1").style.display = 'flex';
    // document.getElementById('tab3').style.background = '#da2c46';
  }

}

function ManageHrsOperations() {
  var countselect = 0;
  var hrsop = document.getElementsByClassName("hrs-opera");
  var hrsselect = hrsop[0].getElementsByTagName("select");
  var optionscount = 0;
  for (i = 0; i < hrsselect.length; i++) {
    if (hrsselect[i].required) {
      countselect++;

      var selectedValue = hrsselect[i].options[hrsselect[i].selectedIndex].value;
      if (selectedValue != -1) {
        optionscount++;
        hrsselect[i].style.borderColor = '#28a745';
      }
      else {
        hrsselect[i].style.borderColor = '#dc3545';
      }

    }
  }
  if (optionscount == 14) {

    document.getElementById('tab4').style.background = '#28a745';
    document.querySelector(".hrsvalidate").style.display = 'none';
  }
  else if (optionscount < 14) {
    document.querySelector(".hrsvalidate").style.display = 'flex';
    // document.getElementById('tab4').style.background = '#da2c46';
  }
}

function ManageContactPerson() {
  var contactperson = document.getElementsByClassName("venuefields1");
  var cp = contactperson[0].getElementsByTagName("input");

  var filled = 0;
  for (i = 0; i < cp.length; i++) {

    if (cp[i].required) {
      let val = cp[i].value;

      if (val != "") {
        cp[i].style.borderColor = "#28a745";
        filled++;
      }
      else if (val == "") {
        cp[i].style.borderColor = "red";
      }

    }
  }
  var cpselect = contactperson[0].getElementsByTagName("select");
  var optionscount = 0;
  for (i = 0; i < cpselect.length; i++) {
    if (cpselect[i].required) {
      var selectedValue = cpselect[i].options[cpselect[i].selectedIndex].value;
      if (selectedValue != "") {
        optionscount++;
        cpselect[i].style.borderColor = '#28a745';
      }
      else {
        cpselect[i].style.borderColor = 'red';
      }
    }

  }
  if (optionscount == 1 && filled == 5) {
    document.getElementById('tab5').style.background = '#28a745';
    document.getElementById('wrappershow').style.display = 'flex';
  }

  // else if(filled < 5){
  //   document.getElementById('tab5').style.background = '#da2c46';
  // }
}

function ManageVenueName() {

  var x = document.getElementsByClassName("registervenue");
  var y = x[0].getElementsByTagName("input");
  var filled = 0;
  for (i = 0; i < y.length; i++) {

    if (y[i].required) {
      let val = y[i].value;
      if (val != "") {

        y[i].style.borderColor = "green";
        filled++;

      }
      else if (val == "") {
        y[i].style.borderColor = "red";
      }

    }
  }

  if (filled == 5) {
    document.getElementById('tab1').style.background = '#28a745';

  }





  // var x = document.forms["registervenue"]["vname"].value;
  // if(x == ""){


  //   document.getElementById('vname').style.borderColor = 'red';
  // }
  // else {
  //   document.getElementById('tab1').style.background = '#28a745';
  //   document.getElementById('vname').style.borderColor = '#28a745';
  // }  



}

var hrsop1 = document.getElementsByClassName("hrs-opera");
var hrsselect1 = hrsop1[0].getElementsByTagName("select");


for (i = 0; i < hrsselect1.length; i++) {

  hrsselect1[i].addEventListener('change', function handleChange(event) {
    console.log(event.target.value); // 👉️ get selected VALUE
    event.target.style.borderColor = '#28a745';


  });

}   

// JS for changing Menu Title on the Menu Display page

var mp = document.getElementsByClassName("menutabs");
var mtype = mp[0].getElementsByTagName("li");
for (i = 0; i < mtype.length; i++) {
  let titletext = mtype[i].innerHTML;
  
  mtype[i].addEventListener("click", () => {
    
    document.getElementById('menu-title').innerHTML=titletext;    
  
  });

}

//--------------------------------------------------------------

// JS for side menu navigation

var sidemenu = document.getElementById("select-subtitle");
console.log(sidemenu);
var sub = sidemenu[0].getElementsByTagName("li");
console.log(sub);



// for (i = 0; i < sub.length; i++) {
//   // let titletext = sub[i].innerHTML;
//   console.log(sub[i]);
//   console.log(sub.length);
  
//   // mtype[i].addEventListener("click", () => {
    
//   //   document.getElementById('menu-title').innerHTML=titletext;    
  
//   // });

// }







//----------------------------------

  






