async function askAI() {
  const question = document.getElementById("question").value;
  const answerBox = document.getElementById("answer");

  if (question.trim() === "") {
    answerBox.innerText = "Please enter a question.";
    return;
  }

  answerBox.innerText = "Thinking...";

  try {
    const response = await fetch("http://127.0.0.1:5000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question })
    });

    const data = await response.json();
    answerBox.innerText = data.answer;

  } catch (error) {
    answerBox.innerText = "Backend not reachable. Is Flask running?";
  }
}
