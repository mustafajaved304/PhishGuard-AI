// ================================
// PhishGuard AI
// JavaScript
// ================================

console.log("🛡️ PhishGuard AI Loaded Successfully");

// Fade-in Animation
document.addEventListener("DOMContentLoaded", () => {

    const elements = document.querySelectorAll(".card, .hero, .analyzer-container, .result-card");

    elements.forEach((element, index) => {

        element.style.opacity = "0";
        element.style.transform = "translateY(25px)";

        setTimeout(() => {

            element.style.transition = "all .7s ease";

            element.style.opacity = "1";

            element.style.transform = "translateY(0px)";

        }, index * 120);

    });

});

// ================================
// Form Validation
// ================================

const form = document.querySelector("form");

if(form){

form.addEventListener("submit",function(e){

const textarea=document.querySelector("textarea");

if(textarea.value.trim()==""){

alert("Please enter some text to analyze.");

e.preventDefault();

return;

}

showLoading();

});

}

// ================================
// Loading Overlay
// ================================

function showLoading(){

const overlay=document.createElement("div");

overlay.id="loadingOverlay";

overlay.innerHTML=`

<div class="loader-box">

<h2>🛡️ PhishGuard AI</h2>

<div class="spinner"></div>

<p>Analyzing for phishing threats...</p>

</div>

`;

document.body.appendChild(overlay);

}

// ================================
// Button Hover Effect
// ================================

const buttons=document.querySelectorAll("button,.primary-btn");

buttons.forEach(btn=>{

btn.addEventListener("mouseenter",()=>{

btn.style.transform="scale(1.04)";

});

btn.addEventListener("mouseleave",()=>{

btn.style.transform="scale(1)";

});

});