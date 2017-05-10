class FormInstructions:
    def __init__(self, specs, form_factor=None, user=None):
        self.short_delay = '~d'
        self.long_delay = '~d~d'
        self.tab = '~t'
        self.enter = '~e'
        self.space = '\x20'
        self.status = 'Ready'
        self.model_id = specs.model_identifier
        self.model_name = specs.model_name
        self.fieldset = form_factor or "Desktop"
        self.processor = "{} {}".format(specs.cpu_speed, specs.cpu_name)
        self.memory = specs.memory
        self.drive1 = specs.drive1
        self.drive2 = specs.drive2
        self.drive3 = specs.drive3
        self.drive4 = specs.drive4
        self.serial = specs.serial_number
        self.user = user or ''
        self.fieldsets = {'Desktop': (self._text_box(self.processor) +
                                      self._text_box(self.memory) +
                                      self._text_box(self.drive1) +
                                      self._text_box(self.drive2) +
                                      self._text_box(self.drive3) +
                                      self._text_box(self.drive4)),

                          'Portable': (self._text_box(self.processor) +
                                       self._text_box(self.memory) +
                                       self._text_box(self.drive1)),

                          'New Model': (self._text_box(self.model_name) +
                                        [self.tab,
                                         self.tab,
                                         self.short_delay +
                                         self.model_id])}

    def _common_fields(self, unique_fields):
        return (self._list_box(self.model_id) +
                unique_fields +
                self._list_box(self.status) +
                [self.short_delay,
                 self.space,
                 self.short_delay,
                 self.user,
                 self.short_delay,
                 self.enter,
                 self.short_delay,
                 self.tab] +
                [self.short_delay,
                 self.serial])

    def _text_box(self, field_content):
        return [self.short_delay,
                field_content,
                self.tab]

    def _list_box(self, field_content):
        return [self.space,
                self.short_delay,
                field_content,
                self.long_delay,
                self.enter,
                self.long_delay,
                self.tab,
                self.short_delay]

    def instruction_steps(self):
        if self.fieldset == 'New Model':
            return self.fieldsets['New Model']
        else:
            return self._common_fields(self.fieldsets[self.fieldset])
