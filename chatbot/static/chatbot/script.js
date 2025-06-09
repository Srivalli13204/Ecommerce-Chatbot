const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");

async function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  appendMessage("user", message);
  input.value = "";

  showTypingIndicator();

  try {
    const response = await fetch("http://127.0.0.1:8000/api/chat/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await response.json();

    await new Promise(resolve => setTimeout(resolve, 1200));
    hideTypingIndicator();

    appendMessage("bot", data.reply);

    if (data.products && data.products.length > 0) {
      const productMessages = data.products.slice(0, 3).map(p =>
        `🛍️ <strong>${p.name}</strong> - ₹${p.price}`
      ).join("<br>");
      appendProductCards(data.products);
    }

  } catch (err) {
    hideTypingIndicator(); // Hide if error
    appendMessage("bot", "⚠️ Oops! Something went wrong.");
  }
}

function appendMessage(sender, text) {
  const chatBox = document.getElementById('chat-box');
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message');

  if (sender === 'user') {
    messageDiv.classList.add('user-message');
    messageDiv.innerHTML = text;
  } else {
    messageDiv.classList.add('bot-message');
    messageDiv.innerHTML = text;
  }

  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function showTypingIndicator() {
  const typing = document.createElement('div');
  typing.id = 'typing-indicator';
  typing.classList.add('bot-message');
  typing.innerHTML = '🤖 Bot is typing...';
  chatBox.appendChild(typing);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function hideTypingIndicator() {
  const typing = document.getElementById('typing-indicator');
  if (typing) typing.remove();
}

function appendProductCards(products) {
  const chatBox = document.getElementById('chat-box');

  const cardWrapper = document.createElement('div');
  cardWrapper.classList.add('card-wrapper');

  products.slice(0, 3).forEach(p => {
    const card = document.createElement('div');
    card.classList.add('product-card');

    card.innerHTML = `
      <div class="product-name">🛍️ ${p.name}</div>
      <div class="product-price">₹${p.price}</div>
      <button class="buy-button" onclick="alert('You selected ${p.name}')">Buy</button>
    `;

    cardWrapper.appendChild(card);
  });

  chatBox.appendChild(cardWrapper);
  chatBox.scrollTop = chatBox.scrollHeight;
}