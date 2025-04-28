import os
import ast

def list_classes_and_functions(base_path):
    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read(), filename=file_path)
                        for node in ast.walk(tree):
                            if isinstance(node, ast.ClassDef):
                                print(f"Class: {node.name} (in {file_path})")
                            elif isinstance(node, ast.FunctionDef):
                                print(f"Function: {node.name} (in {file_path})")
                except Exception as e:
                    print(f"[ERROR in {file_path}]: {e}")

if __name__ == "__main__":
    # Вкажи тут свій шлях:
    list_classes_and_functions("C:/Users/User/Desktop/poems-main")