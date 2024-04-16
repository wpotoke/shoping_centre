from django import forms


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField()
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField()


    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введите ваши имя'
    #         }
    #     )
    # )


    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введите свою фамилию'
    #         }
    #     )
    # )


    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Введите номер телефона'
    #         }
    #     )
    # )


    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ('0', False),
    #         ('1', True),
    #     ],
    #     initial=0
    # )


    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'delivery_address',
    #             'rows': 2,
    #             'placeholder': 'Введите адрес доставки'
    #         }
    #     ),
    #     required=False
    # )


    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ('0', False),
    #         ('1', True)
    #     ],
    #     initial='card'
    # )

    # FUUUCK