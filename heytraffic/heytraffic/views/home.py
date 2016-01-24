from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        # Feature Section
        context['features'] = [
            {
                'title': "Suspendisse posuere eget ex quis.",
                'content': "Suspendisse finibus sagittis ornare. Morbi euismod magna eget neque lacinia, non convallis nunc porttitor. Donec dictum, dui ac pharetra venenatis, justo diam facilisis nisl, non sagittis elit felis id felis. Fusce mauris mauris, euismod in sapien et, dapibus fermentum nisi. Morbi orci erat, rutrum nec dignissim sed, suscipit a lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sem dolor, congue ultrices erat sit amet, tincidunt posuere elit. Vestibulum porttitor, nisi quis vehicula bibendum, nibh metus molestie dolor, vitae cursus nisl tellus vitae leo. Aenean sit amet lacinia neque, at dapibus nunc. Vestibulum eget ullamcorper erat. Mauris sagittis luctus vestibulum. Nullam leo elit, dignissim nec nibh et, dictum finibus quam. Proin at laoreet augue. Sed commodo quam ac lobortis suscipit. Nunc rutrum, metus nec iaculis dapibus, enim lacus semper urna, vel ornare nisi mi sed turpis."
            },
            {
                'title': "Suspendisse posuere eget ex quis.",
                'content': "Suspendisse finibus sagittis ornare. Morbi euismod magna eget neque lacinia, non convallis nunc porttitor. Donec dictum, dui ac pharetra venenatis, justo diam facilisis nisl, non sagittis elit felis id felis. Fusce mauris mauris, euismod in sapien et, dapibus fermentum nisi. Morbi orci erat, rutrum nec dignissim sed, suscipit a lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sem dolor, congue ultrices erat sit amet, tincidunt posuere elit. Vestibulum porttitor, nisi quis vehicula bibendum, nibh metus molestie dolor, vitae cursus nisl tellus vitae leo. Aenean sit amet lacinia neque, at dapibus nunc. Vestibulum eget ullamcorper erat. Mauris sagittis luctus vestibulum. Nullam leo elit, dignissim nec nibh et, dictum finibus quam. Proin at laoreet augue. Sed commodo quam ac lobortis suscipit. Nunc rutrum, metus nec iaculis dapibus, enim lacus semper urna, vel ornare nisi mi sed turpis."
            },
            {
                'title': "Suspendisse posuere eget ex quis.",
                'content': "Suspendisse finibus sagittis ornare. Morbi euismod magna eget neque lacinia, non convallis nunc porttitor. Donec dictum, dui ac pharetra venenatis, justo diam facilisis nisl, non sagittis elit felis id felis. Fusce mauris mauris, euismod in sapien et, dapibus fermentum nisi. Morbi orci erat, rutrum nec dignissim sed, suscipit a lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sem dolor, congue ultrices erat sit amet, tincidunt posuere elit. Vestibulum porttitor, nisi quis vehicula bibendum, nibh metus molestie dolor, vitae cursus nisl tellus vitae leo. Aenean sit amet lacinia neque, at dapibus nunc. Vestibulum eget ullamcorper erat. Mauris sagittis luctus vestibulum. Nullam leo elit, dignissim nec nibh et, dictum finibus quam. Proin at laoreet augue. Sed commodo quam ac lobortis suscipit. Nunc rutrum, metus nec iaculis dapibus, enim lacus semper urna, vel ornare nisi mi sed turpis."
            },
        ]

        # FAQ Section
        context['faqs'] = [
            {
                'question': "Donec ac quam eu dui maximus imperdiet.",
                'answer': "Morbi pharetra lectus a odio dignissim blandit. Nullam sed interdum lectus. Fusce aliquam est consequat nisl gravida, non rutrum sem posuere. Integer finibus finibus venenatis. Maecenas quis dui sodales, vehicula velit vitae, vehicula lacus. Nullam fermentum, augue et tincidunt cursus, justo lacus tempus orci, vitae dapibus nibh nisl at erat. Nunc efficitur ultrices accumsan. Suspendisse placerat metus ut scelerisque molestie. Duis ultrices purus eget enim lacinia, viverra varius velit consectetur. Aenean id tellus non erat finibus dictum. Curabitur id est eget urna ultricies pharetra vitae in justo.",
            },
            {
                'question': "Donec ac quam eu dui maximus imperdiet.",
                'answer': "Morbi pharetra lectus a odio dignissim blandit. Nullam sed interdum lectus. Fusce aliquam est consequat nisl gravida, non rutrum sem posuere. Integer finibus finibus venenatis. Maecenas quis dui sodales, vehicula velit vitae, vehicula lacus. Nullam fermentum, augue et tincidunt cursus, justo lacus tempus orci, vitae dapibus nibh nisl at erat. Nunc efficitur ultrices accumsan. Suspendisse placerat metus ut scelerisque molestie. Duis ultrices purus eget enim lacinia, viverra varius velit consectetur. Aenean id tellus non erat finibus dictum. Curabitur id est eget urna ultricies pharetra vitae in justo.",
            },
            {
                'question': "Donec ac quam eu dui maximus imperdiet.",
                'answer': "Morbi pharetra lectus a odio dignissim blandit. Nullam sed interdum lectus. Fusce aliquam est consequat nisl gravida, non rutrum sem posuere. Integer finibus finibus venenatis. Maecenas quis dui sodales, vehicula velit vitae, vehicula lacus. Nullam fermentum, augue et tincidunt cursus, justo lacus tempus orci, vitae dapibus nibh nisl at erat. Nunc efficitur ultrices accumsan. Suspendisse placerat metus ut scelerisque molestie. Duis ultrices purus eget enim lacinia, viverra varius velit consectetur. Aenean id tellus non erat finibus dictum. Curabitur id est eget urna ultricies pharetra vitae in justo.",
            },
            {
                'question': "Donec ac quam eu dui maximus imperdiet.",
                'answer': "Morbi pharetra lectus a odio dignissim blandit. Nullam sed interdum lectus. Fusce aliquam est consequat nisl gravida, non rutrum sem posuere. Integer finibus finibus venenatis. Maecenas quis dui sodales, vehicula velit vitae, vehicula lacus. Nullam fermentum, augue et tincidunt cursus, justo lacus tempus orci, vitae dapibus nibh nisl at erat. Nunc efficitur ultrices accumsan. Suspendisse placerat metus ut scelerisque molestie. Duis ultrices purus eget enim lacinia, viverra varius velit consectetur. Aenean id tellus non erat finibus dictum. Curabitur id est eget urna ultricies pharetra vitae in justo.",
            },
        ]

        return context
