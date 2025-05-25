const form = document.getElementById("predictForm");
const resultBox = document.getElementById("result");
form.addEventListener("submit", async function (e) {
  e.preventDefault();
  const formData = new FormData(form);
  const data = {};
  formData.forEach((value, key) => {
    data[key] = parseFloat(value);
  });
  const response = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  const result = await response.json();
  resultBox.className = "";
  if (result.prediction === "Diabetic") {
    resultBox.innerText =
      " Warning⚠️ \n You are likely Diabetic. \n 🚨Consult a doctor immediately! ";
    resultBox.classList.add("result-diabetic");
  } else if (result.prediction === "Non-Diabetic") {
    resultBox.innerText =
      "Hurray!🎉 \n You are likely Non-Diabetic \n Let's keep it that way ✅";
    resultBox.classList.add("result-nondiabetic");
  } else {
    resultBox.innerText = `Error: ${result.error}`;
  }
  setTimeout(() => {
    resultBox.scrollIntoView({ behavior: "smooth", block: "center" });
  }, 100);
});
