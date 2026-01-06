import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []
    
    def save_todos(self):
        """Save todos to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, task):
        """Add a new todo"""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Added: {task}")
    
    def list_todos(self):
        """Display all todos"""
        if not self.todos:
            print("\nNo todos yet! Add one to get started.")
            return
        
        print("\n" + "="*50)
        print("YOUR TODO LIST")
        print("="*50)
        for todo in self.todos:
            status = "✓" if todo['completed'] else "○"
            print(f"{status} [{todo['id']}] {todo['task']}")
        print("="*50)
    
    def complete_todo(self, todo_id):
        """Mark a todo as completed"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✓ Completed: {todo['task']}")
                return
        print(f"Todo with ID {todo_id} not found.")
    
    def delete_todo(self, todo_id):
        """Delete a todo"""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                deleted_task = self.todos.pop(i)
                self.save_todos()
                print(f"✓ Deleted: {deleted_task['task']}")
                return
        print(f"Todo with ID {todo_id} not found.")
    
    def run(self):
        """Main application loop"""
        print("\n🎯 Welcome to Todo App!")
        
        while True:
            print("\nOptions:")
            print("1. Add todo")
            print("2. List todos")
            print("3. Complete todo")
            print("4. Delete todo")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                task = input("Enter task: ").strip()
                if task:
                    self.add_todo(task)
                else:
                    print("Task cannot be empty!")
            
            elif choice == '2':
                self.list_todos()
            
            elif choice == '3':
                self.list_todos()
                try:
                    todo_id = int(input("Enter todo ID to complete: "))
                    self.complete_todo(todo_id)
                except ValueError:
                    print("Please enter a valid number!")
            
            elif choice == '4':
                self.list_todos()
                try:
                    todo_id = int(input("Enter todo ID to delete: "))
                    self.delete_todo(todo_id)
                except ValueError:
                    print("Please enter a valid number!")
            
            elif choice == '5':
                print("\n👋 Goodbye! Stay productive!")
                break
            
            else:
                print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()