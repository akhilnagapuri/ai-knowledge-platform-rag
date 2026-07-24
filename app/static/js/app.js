const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("pdfFile");
const uploadStatus = document.getElementById("uploadStatus");

uploadBtn.onclick = async function () {

    if (fileInput.files.length === 0) {

        uploadStatus.innerHTML = "❌ Please select a PDF first.";
        return;
    }

    uploadStatus.innerHTML = "Uploading PDF...";

    const formData = new FormData();

    formData.append(
        "file",
        fileInput.files[0]
    );

    try {

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        console.log(result);

        uploadStatus.innerHTML =
    result.message +
    "<br><br>" +
    "Chunks Created: " +
    result.data.chunks;

    }

    catch(error){

        console.log(error);

        uploadStatus.innerHTML = "❌ Upload Failed.";

    }

};

// =========================
// CHAT SECTION
// =========================

const askBtn = document.getElementById("askBtn");
const questionBox = document.getElementById("question");
const chatStatus = document.getElementById("chatStatus");
const answerBox = document.getElementById("response");

askBtn.onclick = async function () {

    const question = questionBox.value.trim();

    if (question === "") {

        chatStatus.innerHTML = "❌ Please enter a question.";

        return;
    }

    chatStatus.innerHTML = "🤖 Thinking...";

    answerBox.innerHTML = "";

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const result = await response.json();

        console.log(result);

        chatStatus.innerHTML = "✅ Answer Generated";

        answerBox.innerHTML = result.data.answer;

    }

    catch (error) {

        console.log(error);

        chatStatus.innerHTML = "❌ Something went wrong.";

    }

};