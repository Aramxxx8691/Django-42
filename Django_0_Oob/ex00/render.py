import sys, os, re
import settings


def render():
    error_msg = None
    if len(sys.argv) != 2:
        error_msg = "❌ Usage: render.py <file.template>"
    elif not sys.argv[1].endswith('.template'):
        error_msg = "⚠️ Template file must have ❗️.template❗️ extension"
    elif not os.path.exists(sys.argv[1]):
        error_msg = "❌ File not found"
    if error_msg:
        print(error_msg)
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as file:
            template = "".join(file.readlines())
        result = template.format(
            name=settings.name, surname=settings.surname, title=settings.title,
            age=settings.age, profession=settings.profession)
        path_new = re.sub(r'(\.template)$', '.html', sys.argv[1])
        with open(path_new, "w") as file:
            file.write(result)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)            

if __name__ == '__main__':
    render()
