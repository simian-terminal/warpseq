
from warpseq.theory.note import note
from warpseq.theory.chord import chord
from warpseq.theory.scale import scale
from warpseq.notation.roman import Roman, roman
from warpseq.notation.literal import Literal

class TestRoman(object):

    def test_basics(self):

        r = Roman(scale=scale("C4 major"))

        assert r.do("1") == note("C4")
        assert r.do("3") == note("E4")
        assert r.do("4") == note("F4")

        assert r.do("IV") == chord("F4 major")
        assert r.do("iv") == chord("F4 minor")

        # somewhat non-standard notation but allows describing other chord types (see chord.py)
        assert r.do("I:power") == chord(["C4", "G4"])

    def test_shortcuts(self):

        r = roman("C4 major")
        assert r.do("IV") == chord("F4 major")

    def test_inversions(self):

        # non-standard notation but I wanted a somewhat clean-ish way to describe inversions
        r = roman("C4 major")
        assert r.do("I'")  == chord(["E4","G4","C5"])
        assert r.do("I''") == chord(["G4","C5","E5"])
        assert r.do("I':power") == chord(["G4","C5"])

class TestLiteral(object):

    def test_basics(self):

        l = Literal()
        assert l.do("C4") == note("C4")
        assert l.do("C4-major") == chord("C4 major")
        assert l.do("C4,E4,G4") == chord("C4 major")

        # FIXME: inversions are not supported in literal.py yet, we'd ideally want
        # this in a common base class -- low priority
        #assert l.do("C4'-major") == chord("C5,E4,G4")