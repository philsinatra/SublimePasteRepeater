import sublime, sublime_plugin

class RepeaterCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().show_input_panel("Paste how many times?", "", self.on_done, None, None)

  def on_done(self, user_input):
    pasteCount = int(float(user_input))
    for x in range(0,pasteCount):
      self.view.run_command('paste')