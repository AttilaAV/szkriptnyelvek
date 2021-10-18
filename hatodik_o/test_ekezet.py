from ekezet import remove_accent

def test_remove_accent():
	assert remove_accent('áéíóöőúüűÁÉÍÓÖŐÚÜŰ') == 'aeiooouuuAEIOOOUUU'