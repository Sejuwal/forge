# Forge: Unified Access to AI Model Providers 🌐🤖

[![Download Forge Releases](https://img.shields.io/badge/Download%20Releases-Forge-blue)](https://github.com/Sejuwal/forge/releases)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

---

## Overview

Forge is a self-hosted middleware designed to unify access to various AI model providers, such as OpenAI and Anthropic. With Forge, developers can interact with multiple AI models through a single API, simplifying the integration process into existing tools and frontends. It emphasizes security, scalability, and extensibility, making it an ideal choice for developers looking to leverage AI capabilities without the hassle of managing multiple integrations.

---

## Features

- **Unified API Access**: Interact with different AI model providers through a single interface.
- **OpenAI-Compatible**: Easily integrate with existing tools that support OpenAI interfaces.
- **Encrypted API Key Management**: Store and manage your API keys securely.
- **Scalability**: Built to handle growing demands as your application scales.
- **Extensibility**: Add new features and integrations as needed.
- **Self-Hosted**: Full control over your middleware environment.

---

## Installation

To install Forge, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sejuwal/forge.git
   ```

2. **Navigate to the Directory**:
   ```bash
   cd forge
   ```

3. **Install Dependencies**:
   Ensure you have Node.js installed, then run:
   ```bash
   npm install
   ```

4. **Run Forge**:
   After installation, start the server with:
   ```bash
   npm start
   ```

You can download the latest release from the [Releases section](https://github.com/Sejuwal/forge/releases). Follow the instructions in the release notes to execute the necessary files.

---

## Usage

Once Forge is running, you can start using the API. Here’s a simple example of how to make a request:

### Example Request

```bash
curl -X POST http://localhost:3000/api/v1/ai-model \
-H "Content-Type: application/json" \
-d '{"model": "openai-gpt-3", "prompt": "Hello, world!"}'
```

### Example Response

```json
{
  "response": "Hello, world! How can I assist you today?"
}
```

This example demonstrates how to interact with an AI model using a simple POST request. You can customize the model and prompt as needed.

---

## Configuration

Forge comes with a configuration file that allows you to set various parameters:

1. **Locate the Configuration File**: The configuration file is named `config.json` and is located in the root directory.

2. **Edit the Configuration**: Open the file in your favorite text editor and modify the following fields:

   - **apiKeys**: Add your API keys for the AI providers you wish to use.
   - **port**: Change the default port if needed.
   - **models**: Specify which models to enable.

### Sample Configuration

```json
{
  "apiKeys": {
    "openai": "your-openai-api-key",
    "anthropic": "your-anthropic-api-key"
  },
  "port": 3000,
  "models": ["openai-gpt-3", "anthropic-model"]
}
```

---

## API Reference

Forge provides a RESTful API for interacting with AI models. Below are the key endpoints:

### 1. Get Available Models

- **Endpoint**: `GET /api/v1/models`
- **Description**: Retrieve a list of available AI models.

### 2. Generate Response

- **Endpoint**: `POST /api/v1/ai-model`
- **Description**: Send a prompt to the specified AI model and receive a response.
- **Request Body**:
  ```json
  {
    "model": "model-name",
    "prompt": "Your prompt here"
  }
  ```

### 3. Health Check

- **Endpoint**: `GET /api/v1/health`
- **Description**: Check if the server is running.

---

## Contributing

We welcome contributions to Forge! If you’d like to help, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the top right of the repository page.
2. **Create a New Branch**: 
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make Your Changes**: Implement your feature or fix.
4. **Commit Your Changes**: 
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Fork**: 
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Create a Pull Request**: Go to the original repository and submit a pull request.

---

## License

Forge is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Support

If you encounter issues or have questions, please check the [Releases section](https://github.com/Sejuwal/forge/releases) for updates and troubleshooting tips. You can also open an issue in the repository for help.

--- 

Feel free to explore, contribute, and leverage Forge for your AI integration needs!