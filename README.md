# Jarvis v2 — Windows Desktop AI Assistant

A voice-enabled desktop AI assistant for Windows, built with Python. Jarvis is being developed step by step, with an emphasis on a dark desktop interface, English and Urdu voice interaction, and carefully limited computer actions.

> **Project status:** Steps 1–5 have been implemented and tested in the developer's local project. Step 6 (File Assistant) is planned and is not complete yet.
>
> **Important repository note:** The current GitHub `main` branch still contains the original starter `main.py` and the initial dependency list. The updated Step 2–5 project files have been tested locally but are not yet fully synced to this branch. To run the complete Step 1–5 assistant, first copy/apply the files from the corresponding Step 2, Voice, Step 4 UI, and Step 5 update packages into this repository. Until that sync is done, the GitHub copy may open only the starter window.

## Features

### Completed in the local development build (Steps 1–5)

- Dark desktop interface with sidebar and chat area.
- English and Urdu/Roman Urdu interaction.
- Voice input using the microphone button.
- Optional wake-word activation ("Jarvis").
- Spoken responses with a speech toggle.
- Chat memory that keeps the latest 20 messages.
- Secure local storage for the Anthropic API key using Windows Credential Manager through Python Keyring.
- Allowlisted Windows app launching: Notepad, Calculator, Paint, and File Explorer.
- Open supported HTTPS websites in the default browser.
- Open Google searches from a spoken or typed query.
- Basic date/time, arithmetic, and system-information tools.

### Planned

- **Step 6 — File Assistant:** user-approved folders, file listing and reading, and creating text/Markdown files only after explicit confirmation. This step is not available yet.

## Requirements

- Windows 10 or Windows 11.
- Python 3.11 or newer (Python 3.11 is the recommended baseline).
- Git.
- An Anthropic API key.
- A working microphone and speakers/headphones for voice features.
- Internet connection for AI responses and speech components that require downloads or online access.

Visual Studio Code is recommended, but any Python editor can be used.

## Step-by-step installation

### 1. Install Python

Download Python from [python.org](https://www.python.org/downloads/).

During installation on Windows, enable **Add Python to PATH**.

Open Command Prompt or PowerShell and verify:

```powershell
py -3.11 --version
```

You should see Python 3.11.x or a compatible newer version.

### 2. Install Git

Download Git from [git-scm.com](https://git-scm.com/downloads), install it, then verify:

```powershell
git --version
```

### 3. Clone the repository

Open PowerShell or Command Prompt and run:

```powershell
git clone https://github.com/primebecraftyt-art/Jarvis-v2.git
cd Jarvis-v2
```

### 4. Apply the completed Step 2–5 updates

Before launching the full assistant, make sure this repository folder contains the latest tested Step 2, Voice, Step 4 UI, and Step 5 files.

The current GitHub `main` branch is not yet fully synced with those local updates. If you have the step ZIP packages, extract each package into the repository folder and allow the updated files to replace older versions when prompted. Keep a backup of your project before replacing files.

### 5. Create a virtual environment

Run these commands from inside the `Jarvis-v2` folder:

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

When activated, you should see `(.venv)` at the start of your terminal prompt.

### 6. Install Python dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If a step update package includes an updated `requirements.txt`, use that updated file before installing dependencies.

### 7. Add your Anthropic API key

Create an API key in your Anthropic account. Do not paste your key into source code, README files, screenshots, or public GitHub commits.

The Step 2 build stores the key in your operating system's credential store. From the activated virtual environment, run:

```powershell
python -c "from getpass import getpass; from jarvis.core.credentials import save_anthropic_api_key; save_anthropic_api_key(getpass('Anthropic API key: ')); print('API key saved.')"
```

Paste the key when prompted. The input is hidden while typing.

### 8. Start Jarvis

With the virtual environment active, run:

```powershell
python main.py
```

The Jarvis desktop window should open. If the full Step 2–5 updates have not been applied, the repository's current starter entry point may open instead of the complete assistant UI.

## Voice usage

- Click the microphone button to start voice input.
- If wake-word mode is enabled, say **Jarvis** before your request.
- Use the available language controls/settings for English or Urdu.
- Turn spoken responses on or off using the speech toggle.
- Allow microphone access in Windows if prompted.

For the best results, use a quiet environment and check that the correct microphone is selected in Windows sound settings.

## Run the tests

From the repository root, with the virtual environment activated:

```powershell
python -m unittest discover -s tests -v
```

The developer reported that all 10 Python tests in the Step 5 test suite passed, along with the Step 5 voice/app/browser checks. Run the tests again after changing or updating files.

## Safety and permissions

- Jarvis's computer actions are limited to a fixed allowlist of supported apps and browser actions.
- Arbitrary shell commands are not enabled as a general-purpose assistant action.
- Do not give the assistant access to folders or files you do not intend it to use.
- Keep API keys private. If a key is accidentally exposed, revoke it with the provider and create a new one.

## Troubleshooting

**`py` is not recognized**  
Reinstall Python and enable **Add Python to PATH**, then reopen your terminal.

**`ModuleNotFoundError` appears**  
Activate `.venv` and run `pip install -r requirements.txt` again. Confirm you are in the repository root.

**Jarvis cannot hear you**  
Check Windows microphone permissions, the selected input device, and whether another application is using the microphone.

**AI replies do not work**  
Check your internet connection and confirm that the Anthropic API key was saved correctly.

**The old starter window opens**  
The current GitHub branch has not yet been fully updated with the Step 2–5 local project files. Apply the matching step update packages before starting the full assistant.

## Development progress

| Step | Description | Status |
|---|---|---|
| 1 | Project foundation and configuration | Complete |
| 2 | AI chat, memory, and basic tools | Complete |
| 3 | Voice input and spoken responses | Complete |
| 4 | Desktop UI integration | Complete |
| 5 | Allowlisted computer actions | Complete |
| 6 | Approved-folder File Assistant | Planned |

## Contributing

This is an actively developed project. Suggestions, bug reports, and improvement ideas are welcome through GitHub Issues.

## License

No license has been added yet. Unless a license is added, standard copyright rules apply and reuse or redistribution is not automatically permitted.
