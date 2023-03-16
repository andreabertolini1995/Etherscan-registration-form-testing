class User {
  constructor() {
    this.username = "";
    this.email_address = "";
    this.password = "";
  }

  shout(message) {
    this.network.broadcast(message);
  }

  hear(message) {
    this.messages.push(message);
  }

  messagesHeard() {
    return this.messages;
  }
}

module.exports = User;
