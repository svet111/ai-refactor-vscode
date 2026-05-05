import * as vscode from "vscode";
import axios from "axios";

export function activate(context: vscode.ExtensionContext) {

    let disposable = vscode.commands.registerCommand("ai-refactor.run", async () => {

        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showErrorMessage("No active editor");
            return;
        }

        const code = editor.document.getText();

        vscode.window.showInformationMessage("Analyzing code...");

        try {
            const response = await axios.post("http://localhost:8000/refactor", {
                code
            });

            const result = response.data.result;

            const panel = vscode.window.createWebviewPanel(
                "aiRefactor",
                "AI Refactor Result",
                vscode.ViewColumn.Beside,
                {}
            );

            panel.webview.html = getHtml(result);

        } catch (err) {
            vscode.window.showErrorMessage("Backend not running");
        }
    });

    context.subscriptions.push(disposable);
}

function getHtml(result: string) {
    return `
    <html>
    <body style="font-family: sans-serif; padding: 10px;">
        <h2>AI Refactoring Suggestions</h2>
        <pre>${result}</pre>
    </body>
    </html>
    `;
}

export function deactivate() {}
