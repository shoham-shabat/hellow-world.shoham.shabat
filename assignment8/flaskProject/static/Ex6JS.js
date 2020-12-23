
function changeImgSRC(id,s,px) {
    document.getElementById(id).src=s;
    document.getElementById(id).width=px;
}

function changeTextStyle(id,size) {
    document.getElementById(id).style.fontSize=size;

}

function changeBoxColor(id,col) {
    document.getElementById(id).style.background=col;
}

function CheckForm(First_Name,Family_Name,email,company_Name,Phone_number,free_comment) {
    var b1=document.getElementById(First_Name).value;
    var b2=document.getElementById(Family_Name).value;
    var b3=document.getElementById(email).value;
    var b4=document.getElementById(company_Name).value;
    var b5=document.getElementById(Phone_number).value;
    var b6=document.getElementById(free_comment).value;
    if (b1.length<1 || b2.length<1 || b3.length<1 || b4.length<1 || b5.length<1 || b6.length<1 ){
        alert("One of the fields is empty. Please fill all filds!");
    }
    else {
        b1=document.getElementById(First_Name).value="";
        b2=document.getElementById(Family_Name).value="";
        b3=document.getElementById(email).value="";
        b4=document.getElementById(company_Name).value="";
        b5=document.getElementById(Phone_number).value="";
        b6=document.getElementById(free_comment).value="";
        alert("Form submitted!") 
    }
}