from django import forms

from .models import WeightEntry


class WeightEntryForm(forms.ModelForm):
	class Meta:
		model = WeightEntry
		fields = ["date", "weight", "notes"]
		widgets = {
			"date": forms.DateInput(
				attrs={
					"type": "date",
					"class": "mt-1 block w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-slate-900 shadow-sm outline-none transition focus:border-purple-400 focus:ring-4 focus:ring-purple-100",
				}
			),
			"weight": forms.NumberInput(
				attrs={
					"step": "0.01",
					"min": "0",
					"class": "mt-1 block w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-slate-900 shadow-sm outline-none transition focus:border-purple-400 focus:ring-4 focus:ring-purple-100",
				}
			),
			"notes": forms.Textarea(
				attrs={
					"rows": 4,
					"class": "mt-1 block w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-slate-900 shadow-sm outline-none transition focus:border-purple-400 focus:ring-4 focus:ring-purple-100",
					"placeholder": "Optional notes about this entry",
				}
			),
		}
