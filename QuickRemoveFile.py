import sublime, sublime_plugin, os

class QuickRemoveFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name = self.view.file_name()
        view = self.view

        confirm = sublime.ok_cancel_dialog("You are about to remove this file the: \n%s" % file_name)

        if confirm:
            try:
                view.set_scratch(True)
                window = view.window()
                window.focus_view(view)
                window.run_command("close_file")

                os.remove(file_name)
            except OSError:
                pass
