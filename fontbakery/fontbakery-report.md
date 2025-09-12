## FontBakery report

fontbakery version: 1.0.1







## Check results



<details><summary>[26] LXGWMarkerGothic-Regular.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 💥 **ERROR** <p>Failed with KeyError: 'Berf'</p>
<pre><code>  File &quot;/home/runner/work/LxgwMarkerGothic/LxgwMarkerGothic/venv-test/lib/python3.10/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/runner/work/LxgwMarkerGothic/LxgwMarkerGothic/venv-test/lib/python3.10/site-packages/fontbakery/checks/vendorspecific/googlefonts/glyphsets/shape_languages.py&quot;, line 48, in check_glyphsets_shape_languages
    for language_code in languages_per_glyphset(glyphset):
  File &quot;/home/runner/work/LxgwMarkerGothic/LxgwMarkerGothic/venv-test/lib/python3.10/site-packages/glyphsets/__init__.py&quot;, line 669, in languages_per_glyphset
    return GlyphSet.load(glyphset_name).get_language_codes()
  File &quot;/home/runner/work/LxgwMarkerGothic/LxgwMarkerGothic/venv-test/lib/python3.10/site-packages/glyphsets/__init__.py&quot;, line 222, in get_language_codes
    and SCRIPT_NAMES[language.script] == self.script

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+019E: LATIN SMALL LETTER N WITH LONG RIGHT LEG</td>
<td align="left">U+0220: LATIN CAPITAL LETTER N WITH LONG RIGHT LEG</td>
</tr>
<tr>
<td align="left">U+023A: LATIN CAPITAL LETTER A WITH STROKE</td>
<td align="left">U+2C65: LATIN SMALL LETTER A WITH STROKE</td>
</tr>
<tr>
<td align="left">U+023E: LATIN CAPITAL LETTER T WITH DIAGONAL STROKE</td>
<td align="left">U+2C66: LATIN SMALL LETTER T WITH DIAGONAL STROKE</td>
</tr>
<tr>
<td align="left">U+0253: LATIN SMALL LETTER B WITH HOOK</td>
<td align="left">U+0181: LATIN CAPITAL LETTER B WITH HOOK</td>
</tr>
<tr>
<td align="left">U+0257: LATIN SMALL LETTER D WITH HOOK</td>
<td align="left">U+018A: LATIN CAPITAL LETTER D WITH HOOK</td>
</tr>
<tr>
<td align="left">U+0260: LATIN SMALL LETTER G WITH HOOK</td>
<td align="left">U+0193: LATIN CAPITAL LETTER G WITH HOOK</td>
</tr>
<tr>
<td align="left">U+0263: LATIN SMALL LETTER GAMMA</td>
<td align="left">U+0194: LATIN CAPITAL LETTER GAMMA</td>
</tr>
<tr>
<td align="left">U+0265: LATIN SMALL LETTER TURNED H</td>
<td align="left">U+A78D: LATIN CAPITAL LETTER TURNED H</td>
</tr>
<tr>
<td align="left">U+0266: LATIN SMALL LETTER H WITH HOOK</td>
<td align="left">U+A7AA: LATIN CAPITAL LETTER H WITH HOOK</td>
</tr>
<tr>
<td align="left">U+0269: LATIN SMALL LETTER IOTA</td>
<td align="left">U+0196: LATIN CAPITAL LETTER IOTA</td>
</tr>
<tr>
<td align="left">U+026A: LATIN LETTER SMALL CAPITAL I</td>
<td align="left">U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I</td>
</tr>
<tr>
<td align="left">U+026C: LATIN SMALL LETTER L WITH BELT</td>
<td align="left">U+A7AD: LATIN CAPITAL LETTER L WITH BELT</td>
</tr>
<tr>
<td align="left">U+026F: LATIN SMALL LETTER TURNED M</td>
<td align="left">U+019C: LATIN CAPITAL LETTER TURNED M</td>
</tr>
<tr>
<td align="left">U+0272: LATIN SMALL LETTER N WITH LEFT HOOK</td>
<td align="left">U+019D: LATIN CAPITAL LETTER N WITH LEFT HOOK</td>
</tr>
<tr>
<td align="left">U+027D: LATIN SMALL LETTER R WITH TAIL</td>
<td align="left">U+2C64: LATIN CAPITAL LETTER R WITH TAIL</td>
</tr>
<tr>
<td align="left">U+0280: LATIN LETTER SMALL CAPITAL R</td>
<td align="left">U+01A6: LATIN LETTER YR</td>
</tr>
<tr>
<td align="left">U+0288: LATIN SMALL LETTER T WITH RETROFLEX HOOK</td>
<td align="left">U+01AE: LATIN CAPITAL LETTER T WITH RETROFLEX HOOK</td>
</tr>
<tr>
<td align="left">U+028B: LATIN SMALL LETTER V WITH HOOK</td>
<td align="left">U+01B2: LATIN CAPITAL LETTER V WITH HOOK</td>
</tr>
<tr>
<td align="left">U+029D: LATIN SMALL LETTER J WITH CROSSED-TAIL</td>
<td align="left">U+A7B2: LATIN CAPITAL LETTER J WITH CROSSED-TAIL</td>
</tr>
<tr>
<td align="left">U+04F4: CYRILLIC CAPITAL LETTER CHE WITH DIAERESIS</td>
<td align="left">U+04F5: CYRILLIC SMALL LETTER CHE WITH DIAERESIS</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure smart dropout control is enabled in "prep" table instructions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#smart-dropout">smart_dropout</a></summary>
    <div>







* 🔥 **FAIL** <p>The 'prep' table does not contain TrueType instructions enabling smart dropout control. To fix, export the font with autohinting enabled, or run ttfautohint on the font, or run the <code>gftools fix-nonhinting</code> script.</p>
 [code: lacks-smart-dropout]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check family name for GF Guide compliance. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-family-name-compliance">googlefonts/family_name_compliance</a></summary>
    <div>







* 🔥 **FAIL** <p>&quot;LXGW Marker Gothic&quot; contains an abbreviation.</p>
 [code: abbreviation]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check if the vertical metrics of a CJK family are similar to the same family hosted on Google Fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics-regressions">googlefonts/cjk_vertical_metrics_regressions</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2 sTypoAscender is 880 when it should be 982</p>
 [code: cjk-metric-regression]



* 🔥 **FAIL** <p>OS/2 sTypoDescender is -120 when it should be -198</p>
 [code: cjk-metric-regression]



* 🔥 **FAIL** <p>OS/2 usWinAscent is 1050 when it should be 1160</p>
 [code: cjk-metric-regression]



* 🔥 **FAIL** <p>OS/2 usWinDescent is 267 when it should be 288</p>
 [code: cjk-metric-regression]



* 🔥 **FAIL** <p>hhea ascent is 880 when it should be 982</p>
 [code: cjk-metric-regression]



* 🔥 **FAIL** <p>hhea descent is -120 when it should be -198</p>
 [code: cjk-metric-regression]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
dotbelowcomb (U+0323), hookabovecomb (U+0309), u0304 (U+0304), u0306 (U+0306), u030B (U+030B), u030D (U+030D), u030E (U+030E), u030F (U+030F), u0311 (U+0311), u0312 (U+0312), u0313 (U+0313), u0324 (U+0324), u0325 (U+0325), u0326 (U+0326), u0328 (U+0328), u0329 (U+0329), u032C (U+032C), u032D (U+032D), u032E (U+032E), u032F (U+032F), u0330 (U+0330), u0331 (U+0331), u0332 (U+0332), u0337 (U+0337), u3099 (U+3099) and u309A (U+309A)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check GDEF mark glyph class doesn't have characters that are not marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-non-mark-chars">opentype/gdef_non_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following non-mark characters should not be in the GDEF mark glyph class:
U+0384</p>
 [code: non-mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check glyphs in mark glyph class are non-spacing. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-spacing-marks">opentype/gdef_spacing_marks</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs seem to be spacing (because they have width &gt; 0 on the hmtx table) so they may be in the GDEF mark glyph class by mistake, or they should have zero width instead:
tonos (U+0384)</p>
 [code: spacing-mark-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>Tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain chws and vchw features? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-chws-feature">cjk_chws_feature</a></summary>
    <div>







* ⚠️ **WARN** <p>chws feature not found in font. Use chws_tool (<a href="https://github.com/googlefonts/chws_tool">https://github.com/googlefonts/chws_tool</a>) to add it.</p>
 [code: missing-chws-feature]



* ⚠️ **WARN** <p>vchw feature not found in font. Use chws_tool (<a href="https://github.com/googlefonts/chws_tool">https://github.com/googlefonts/chws_tool</a>) to add it.</p>
 [code: missing-vchw-feature]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: u013B	Contours detected: 1	Expected: 2

- Glyph name: beta	Contours detected: 1	Expected: 2

- Glyph name: u04EA	Contours detected: 3	Expected: 5

- Glyph name: u04EB	Contours detected: 3	Expected: 5

- Glyph name: trademark	Contours detected: 1	Expected: 2

- Glyph name: u2213	Contours detected: 1	Expected: 2

- Glyph name: u222C	Contours detected: 3	Expected: 2

- Glyph name: u222D	Contours detected: 4	Expected: 3

- Glyph name: propersuperset	Contours detected: 2	Expected: 1

- Glyph name: notsubset	Contours detected: 1	Expected: 2

- Glyph name: objectreplacementcharacter	Contours detected: 11	Expected: 22

- Glyph name: beta	Contours detected: 1	Expected: 2

- Glyph name: notsubset	Contours detected: 1	Expected: 2

- Glyph name: propersuperset	Contours detected: 2	Expected: 1

- Glyph name: trademark	Contours detected: 1	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure files are not too large. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#file-size">file_size</a></summary>
    <div>







* ⚠️ **WARN** <p>Font file is 3.0Mb; ideally it should be less than 1.0Mb</p>
 [code: large-font]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos-kerning-info">gpos_kerning_info</a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 1000 among a set of 36 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 500:
u2213, greater, equal, divide, plus, plusminus, multiply, approxequal, less, minus, similar, logicalnot</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* u1EFF (U+1EFF): L&lt;&lt;217.0,-91.0&gt;--&lt;217.0,-91.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking that the typoAscender exceeds the yMax of the /Agrave. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#typoascender-exceeds-Agrave">typoascender_exceeds_Agrave</a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2.sTypoAscender value should be greater than 1003, but got 880 instead</p>
 [code: typoAscender]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- quotedbl.1

- u00AD
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02CD MODIFIER LETTER LOW MACRON: try adding lisu</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, math, cherokee</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, tifinagh, malayalam, coptic, math, syriac, tai-le, todhri, old-permic, duployan, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030E COMBINING DOUBLE VERTICAL LINE ABOVE: try adding ethiopic</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: coptic, todhri</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, duployan, cherokee</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032C COMBINING CARON BELOW: try adding math</li>
<li>U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding one of: sunuwar, syriac</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, math, cherokee</li>
<li>U+0331 COMBINING MACRON BELOW: try adding one of: tifinagh, thai, sunuwar, syriac, cherokee, gothic, caucasian-albanian</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+2010 HYPHEN: try adding one of: yi, hebrew, kaithi, lisu, kayah-li, coptic, kharoshthi, armenian, arabic, sundanese, cham, sora-sompeng, syloti-nagri</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2031 PER TEN THOUSAND SIGN: not included in any glyphset definition</li>
<li>U+2034 TRIPLE PRIME: try adding math</li>
<li>U+2035 REVERSED PRIME: try adding math</li>
<li>U+2036 REVERSED DOUBLE PRIME: try adding math</li>
<li>U+2037 REVERSED TRIPLE PRIME: try adding math</li>
<li>U+203B REFERENCE MARK: not included in any glyphset definition</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+205D TRICOLON: try adding one of: meroitic, old-hungarian, meroitic-hieroglyphs, carian</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+2103 DEGREE CELSIUS: try adding math</li>
<li>U+2109 DEGREE FAHRENHEIT: try adding math</li>
<li>U+210E PLANCK CONSTANT: try adding math</li>
<li>U+210F PLANCK CONSTANT OVER TWO PI: try adding math</li>
<li>U+2121 TELEPHONE SIGN: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212A KELVIN SIGN: try adding math</li>
<li>U+212B ANGSTROM SIGN: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2160 ROMAN NUMERAL ONE: try adding symbols</li>
<li>U+2161 ROMAN NUMERAL TWO: try adding symbols</li>
<li>U+2162 ROMAN NUMERAL THREE: try adding symbols</li>
<li>U+2163 ROMAN NUMERAL FOUR: try adding symbols</li>
<li>U+2164 ROMAN NUMERAL FIVE: try adding symbols</li>
<li>U+2165 ROMAN NUMERAL SIX: try adding symbols</li>
<li>U+2166 ROMAN NUMERAL SEVEN: try adding symbols</li>
<li>U+2167 ROMAN NUMERAL EIGHT: try adding symbols</li>
<li>U+2168 ROMAN NUMERAL NINE: try adding symbols</li>
<li>U+2169 ROMAN NUMERAL TEN: try adding symbols</li>
<li>U+216A ROMAN NUMERAL ELEVEN: try adding symbols</li>
<li>U+216B ROMAN NUMERAL TWELVE: try adding symbols</li>
<li>U+216C ROMAN NUMERAL FIFTY: try adding symbols</li>
<li>U+216D ROMAN NUMERAL ONE HUNDRED: try adding symbols</li>
<li>U+216E ROMAN NUMERAL FIVE HUNDRED: try adding symbols</li>
<li>U+216F ROMAN NUMERAL ONE THOUSAND: try adding symbols</li>
<li>U+2170 SMALL ROMAN NUMERAL ONE: try adding symbols</li>
<li>U+2171 SMALL ROMAN NUMERAL TWO: try adding symbols</li>
<li>U+2172 SMALL ROMAN NUMERAL THREE: try adding symbols</li>
<li>U+2173 SMALL ROMAN NUMERAL FOUR: try adding symbols</li>
<li>U+2174 SMALL ROMAN NUMERAL FIVE: try adding symbols</li>
<li>U+2175 SMALL ROMAN NUMERAL SIX: try adding symbols</li>
<li>U+2176 SMALL ROMAN NUMERAL SEVEN: try adding symbols</li>
<li>U+2177 SMALL ROMAN NUMERAL EIGHT: try adding symbols</li>
<li>U+2178 SMALL ROMAN NUMERAL NINE: try adding symbols</li>
<li>U+2179 SMALL ROMAN NUMERAL TEN: try adding symbols</li>
<li>U+217A SMALL ROMAN NUMERAL ELEVEN: try adding symbols</li>
<li>U+217B SMALL ROMAN NUMERAL TWELVE: try adding symbols</li>
<li>U+217C SMALL ROMAN NUMERAL FIFTY: try adding symbols</li>
<li>U+217D SMALL ROMAN NUMERAL ONE HUNDRED: try adding symbols</li>
<li>U+217E SMALL ROMAN NUMERAL FIVE HUNDRED: try adding symbols</li>
<li>U+217F SMALL ROMAN NUMERAL ONE THOUSAND: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+21CB LEFTWARDS HARPOON OVER RIGHTWARDS HARPOON: try adding math</li>
<li>U+21CC RIGHTWARDS HARPOON OVER LEFTWARDS HARPOON: try adding math</li>
<li>U+21CD LEFTWARDS DOUBLE ARROW WITH STROKE: try adding math</li>
<li>U+21CE LEFT RIGHT DOUBLE ARROW WITH STROKE: try adding math</li>
<li>U+21CF RIGHTWARDS DOUBLE ARROW WITH STROKE: try adding math</li>
<li>U+21D0 LEFTWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D1 UPWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D2 RIGHTWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D3 DOWNWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D4 LEFT RIGHT DOUBLE ARROW: try adding math</li>
<li>U+2200 FOR ALL: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2203 THERE EXISTS: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+2207 NABLA: try adding math</li>
<li>U+2208 ELEMENT OF: try adding math</li>
<li>U+2209 NOT AN ELEMENT OF: try adding math</li>
<li>U+220B CONTAINS AS MEMBER: try adding math</li>
<li>U+220C DOES NOT CONTAIN AS MEMBER: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2213 MINUS-OR-PLUS SIGN: try adding math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221D PROPORTIONAL TO: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+221F RIGHT ANGLE: try adding math</li>
<li>U+2220 ANGLE: try adding math</li>
<li>U+2223 DIVIDES: try adding math</li>
<li>U+2224 DOES NOT DIVIDE: try adding math</li>
<li>U+2225 PARALLEL TO: try adding math</li>
<li>U+2226 NOT PARALLEL TO: try adding math</li>
<li>U+2227 LOGICAL AND: try adding math</li>
<li>U+2228 LOGICAL OR: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+222C DOUBLE INTEGRAL: try adding math</li>
<li>U+222D TRIPLE INTEGRAL: try adding math</li>
<li>U+222E CONTOUR INTEGRAL: try adding math</li>
<li>U+222F SURFACE INTEGRAL: try adding math</li>
<li>U+2230 VOLUME INTEGRAL: try adding math</li>
<li>U+2234 THEREFORE: try adding math</li>
<li>U+2235 BECAUSE: try adding math</li>
<li>U+2236 RATIO: try adding math</li>
<li>U+2237 PROPORTION: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+223D REVERSED TILDE: try adding math</li>
<li>U+2243 ASYMPTOTICALLY EQUAL TO: try adding math</li>
<li>U+2245 APPROXIMATELY EQUAL TO: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+224C ALL EQUAL TO: try adding math</li>
<li>U+2252 APPROXIMATELY EQUAL TO OR THE IMAGE OF: try adding math</li>
<li>U+2253 IMAGE OF OR APPROXIMATELY EQUAL TO: try adding math</li>
<li>U+225C DELTA EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2262 NOT IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2266 LESS-THAN OVER EQUAL TO: try adding math</li>
<li>U+2267 GREATER-THAN OVER EQUAL TO: try adding math</li>
<li>U+226A MUCH LESS-THAN: try adding math</li>
<li>U+226B MUCH GREATER-THAN: try adding math</li>
<li>U+226E NOT LESS-THAN: try adding math</li>
<li>U+226F NOT GREATER-THAN: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+2284 NOT A SUBSET OF: try adding math</li>
<li>U+2285 NOT A SUPERSET OF: try adding math</li>
<li>U+2286 SUBSET OF OR EQUAL TO: try adding math</li>
<li>U+2287 SUPERSET OF OR EQUAL TO: try adding math</li>
<li>U+228A SUBSET OF WITH NOT EQUAL TO: try adding math</li>
<li>U+228B SUPERSET OF WITH NOT EQUAL TO: try adding math</li>
<li>U+2299 CIRCLED DOT OPERATOR: try adding one of: symbols, math</li>
<li>U+22A5 UP TACK: try adding math</li>
<li>U+22BF RIGHT TRIANGLE: try adding math</li>
<li>U+2312 ARC: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
<li>U+2469 CIRCLED NUMBER TEN: try adding one of: mongolian, symbols, yi</li>
<li>U+246A CIRCLED NUMBER ELEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+246B CIRCLED NUMBER TWELVE: try adding one of: mongolian, symbols, yi</li>
<li>U+246C CIRCLED NUMBER THIRTEEN: try adding one of: mongolian, symbols, yi</li>
<li>U+246D CIRCLED NUMBER FOURTEEN: try adding one of: mongolian, symbols, yi</li>
<li>U+246E CIRCLED NUMBER FIFTEEN: try adding one of: mongolian, symbols, yi</li>
<li>U+246F CIRCLED NUMBER SIXTEEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2470 CIRCLED NUMBER SEVENTEEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2471 CIRCLED NUMBER EIGHTEEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2472 CIRCLED NUMBER NINETEEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2473 CIRCLED NUMBER TWENTY: try adding one of: mongolian, symbols, yi</li>
<li>U+2474 PARENTHESIZED DIGIT ONE: try adding one of: symbols, math</li>
<li>U+2475 PARENTHESIZED DIGIT TWO: try adding one of: symbols, math</li>
<li>U+2476 PARENTHESIZED DIGIT THREE: try adding symbols</li>
<li>U+2477 PARENTHESIZED DIGIT FOUR: try adding symbols</li>
<li>U+2478 PARENTHESIZED DIGIT FIVE: try adding symbols</li>
<li>U+2479 PARENTHESIZED DIGIT SIX: try adding symbols</li>
<li>U+247A PARENTHESIZED DIGIT SEVEN: try adding symbols</li>
<li>U+247B PARENTHESIZED DIGIT EIGHT: try adding symbols</li>
<li>U+247C PARENTHESIZED DIGIT NINE: try adding symbols</li>
<li>U+247D PARENTHESIZED NUMBER TEN: try adding symbols</li>
<li>U+247E PARENTHESIZED NUMBER ELEVEN: try adding symbols</li>
<li>U+247F PARENTHESIZED NUMBER TWELVE: try adding symbols</li>
<li>U+2480 PARENTHESIZED NUMBER THIRTEEN: try adding symbols</li>
<li>U+2481 PARENTHESIZED NUMBER FOURTEEN: try adding symbols</li>
<li>U+2482 PARENTHESIZED NUMBER FIFTEEN: try adding symbols</li>
<li>U+2483 PARENTHESIZED NUMBER SIXTEEN: try adding symbols</li>
<li>U+2484 PARENTHESIZED NUMBER SEVENTEEN: try adding symbols</li>
<li>U+2485 PARENTHESIZED NUMBER EIGHTEEN: try adding symbols</li>
<li>U+2486 PARENTHESIZED NUMBER NINETEEN: try adding symbols</li>
<li>U+2487 PARENTHESIZED NUMBER TWENTY: try adding symbols</li>
<li>U+2488 DIGIT ONE FULL STOP: try adding symbols</li>
<li>U+2489 DIGIT TWO FULL STOP: try adding symbols</li>
<li>U+248A DIGIT THREE FULL STOP: try adding symbols</li>
<li>U+248B DIGIT FOUR FULL STOP: try adding symbols</li>
<li>U+248C DIGIT FIVE FULL STOP: try adding symbols</li>
<li>U+248D DIGIT SIX FULL STOP: try adding symbols</li>
<li>U+248E DIGIT SEVEN FULL STOP: try adding symbols</li>
<li>U+248F DIGIT EIGHT FULL STOP: try adding symbols</li>
<li>U+2490 DIGIT NINE FULL STOP: try adding symbols</li>
<li>U+2491 NUMBER TEN FULL STOP: try adding symbols</li>
<li>U+2492 NUMBER ELEVEN FULL STOP: try adding symbols</li>
<li>U+2493 NUMBER TWELVE FULL STOP: try adding symbols</li>
<li>U+2494 NUMBER THIRTEEN FULL STOP: try adding symbols</li>
<li>U+2495 NUMBER FOURTEEN FULL STOP: try adding symbols</li>
<li>U+2496 NUMBER FIFTEEN FULL STOP: try adding symbols</li>
<li>U+2497 NUMBER SIXTEEN FULL STOP: try adding symbols</li>
<li>U+2498 NUMBER SEVENTEEN FULL STOP: try adding symbols</li>
<li>U+2499 NUMBER EIGHTEEN FULL STOP: try adding symbols</li>
<li>U+249A NUMBER NINETEEN FULL STOP: try adding symbols</li>
<li>U+249B NUMBER TWENTY FULL STOP: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25EF LARGE CIRCLE: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: symbols, music</li>
<li>U+266D MUSIC FLAT SIGN: try adding one of: symbols, math, music</li>
<li>U+266E MUSIC NATURAL SIGN: try adding one of: symbols, math, music</li>
<li>U+266F MUSIC SHARP SIGN: try adding one of: symbols, math, music</li>
<li>U+2ACB SUBSET OF ABOVE NOT EQUAL TO: try adding math</li>
<li>U+2ACC SUPERSET OF ABOVE NOT EQUAL TO: try adding math</li>
<li>U+301F LOW DOUBLE PRIME QUOTATION MARK: not included in any glyphset definition</li>
<li>U+3022 HANGZHOU NUMERAL TWO: not included in any glyphset definition</li>
<li>U+3023 HANGZHOU NUMERAL THREE: not included in any glyphset definition</li>
<li>U+3024 HANGZHOU NUMERAL FOUR: not included in any glyphset definition</li>
<li>U+3025 HANGZHOU NUMERAL FIVE: not included in any glyphset definition</li>
<li>U+3026 HANGZHOU NUMERAL SIX: not included in any glyphset definition</li>
<li>U+3027 HANGZHOU NUMERAL SEVEN: not included in any glyphset definition</li>
<li>U+3028 HANGZHOU NUMERAL EIGHT: not included in any glyphset definition</li>
<li>U+3029 HANGZHOU NUMERAL NINE: not included in any glyphset definition</li>
<li>U+3038 HANGZHOU NUMERAL TEN: not included in any glyphset definition</li>
<li>U+3039 HANGZHOU NUMERAL TWENTY: not included in any glyphset definition</li>
<li>U+303A HANGZHOU NUMERAL THIRTY: not included in any glyphset definition</li>
<li>U+3225 PARENTHESIZED IDEOGRAPH SIX: not included in any glyphset definition</li>
<li>U+3226 PARENTHESIZED IDEOGRAPH SEVEN: not included in any glyphset definition</li>
<li>U+3227 PARENTHESIZED IDEOGRAPH EIGHT: not included in any glyphset definition</li>
<li>U+3228 PARENTHESIZED IDEOGRAPH NINE: not included in any glyphset definition</li>
<li>U+3229 PARENTHESIZED IDEOGRAPH TEN: not included in any glyphset definition</li>
<li>U+3231 PARENTHESIZED IDEOGRAPH STOCK: not included in any glyphset definition</li>
<li>U+3232 PARENTHESIZED IDEOGRAPH HAVE: not included in any glyphset definition</li>
<li>U+3239 PARENTHESIZED IDEOGRAPH REPRESENT: not included in any glyphset definition</li>
<li>U+3251 CIRCLED NUMBER TWENTY ONE: not included in any glyphset definition</li>
<li>U+3252 CIRCLED NUMBER TWENTY TWO: not included in any glyphset definition</li>
<li>U+3253 CIRCLED NUMBER TWENTY THREE: not included in any glyphset definition</li>
<li>U+3254 CIRCLED NUMBER TWENTY FOUR: not included in any glyphset definition</li>
<li>U+3255 CIRCLED NUMBER TWENTY FIVE: not included in any glyphset definition</li>
<li>U+3256 CIRCLED NUMBER TWENTY SIX: not included in any glyphset definition</li>
<li>U+3257 CIRCLED NUMBER TWENTY SEVEN: not included in any glyphset definition</li>
<li>U+3258 CIRCLED NUMBER TWENTY EIGHT: not included in any glyphset definition</li>
<li>U+3259 CIRCLED NUMBER TWENTY NINE: not included in any glyphset definition</li>
<li>U+325A CIRCLED NUMBER THIRTY: not included in any glyphset definition</li>
<li>U+325B CIRCLED NUMBER THIRTY ONE: not included in any glyphset definition</li>
<li>U+325C CIRCLED NUMBER THIRTY TWO: not included in any glyphset definition</li>
<li>U+325D CIRCLED NUMBER THIRTY THREE: not included in any glyphset definition</li>
<li>U+325E CIRCLED NUMBER THIRTY FOUR: not included in any glyphset definition</li>
<li>U+325F CIRCLED NUMBER THIRTY FIVE: not included in any glyphset definition</li>
<li>U+3280 CIRCLED IDEOGRAPH ONE: not included in any glyphset definition</li>
<li>U+3281 CIRCLED IDEOGRAPH TWO: not included in any glyphset definition</li>
<li>U+3282 CIRCLED IDEOGRAPH THREE: not included in any glyphset definition</li>
<li>U+3283 CIRCLED IDEOGRAPH FOUR: not included in any glyphset definition</li>
<li>U+3284 CIRCLED IDEOGRAPH FIVE: not included in any glyphset definition</li>
<li>U+3285 CIRCLED IDEOGRAPH SIX: not included in any glyphset definition</li>
<li>U+3286 CIRCLED IDEOGRAPH SEVEN: not included in any glyphset definition</li>
<li>U+3287 CIRCLED IDEOGRAPH EIGHT: not included in any glyphset definition</li>
<li>U+3288 CIRCLED IDEOGRAPH NINE: not included in any glyphset definition</li>
<li>U+3289 CIRCLED IDEOGRAPH TEN: not included in any glyphset definition</li>
<li>U+32A4 CIRCLED IDEOGRAPH HIGH: not included in any glyphset definition</li>
<li>U+32A5 CIRCLED IDEOGRAPH CENTRE: not included in any glyphset definition</li>
<li>U+32A6 CIRCLED IDEOGRAPH LOW: not included in any glyphset definition</li>
<li>U+32A7 CIRCLED IDEOGRAPH LEFT: not included in any glyphset definition</li>
<li>U+32A8 CIRCLED IDEOGRAPH RIGHT: not included in any glyphset definition</li>
<li>U+32B1 CIRCLED NUMBER THIRTY SIX: not included in any glyphset definition</li>
<li>U+32B2 CIRCLED NUMBER THIRTY SEVEN: not included in any glyphset definition</li>
<li>U+32B3 CIRCLED NUMBER THIRTY EIGHT: not included in any glyphset definition</li>
<li>U+32B4 CIRCLED NUMBER THIRTY NINE: not included in any glyphset definition</li>
<li>U+32B5 CIRCLED NUMBER FORTY: not included in any glyphset definition</li>
<li>U+32B6 CIRCLED NUMBER FORTY ONE: not included in any glyphset definition</li>
<li>U+32B7 CIRCLED NUMBER FORTY TWO: not included in any glyphset definition</li>
<li>U+32B8 CIRCLED NUMBER FORTY THREE: not included in any glyphset definition</li>
<li>U+32B9 CIRCLED NUMBER FORTY FOUR: not included in any glyphset definition</li>
<li>U+32BA CIRCLED NUMBER FORTY FIVE: not included in any glyphset definition</li>
<li>U+32BB CIRCLED NUMBER FORTY SIX: not included in any glyphset definition</li>
<li>U+32BC CIRCLED NUMBER FORTY SEVEN: not included in any glyphset definition</li>
<li>U+32BD CIRCLED NUMBER FORTY EIGHT: not included in any glyphset definition</li>
<li>U+32BE CIRCLED NUMBER FORTY NINE: not included in any glyphset definition</li>
<li>U+32BF CIRCLED NUMBER FIFTY: not included in any glyphset definition</li>
<li>U+32FF SQUARE ERA NAME REIWA: not included in any glyphset definition</li>
<li>U+3303 SQUARE AARU: not included in any glyphset definition</li>
<li>U+330D SQUARE KARORII: not included in any glyphset definition</li>
<li>U+3314 SQUARE KIRO: not included in any glyphset definition</li>
<li>U+3318 SQUARE GURAMU: not included in any glyphset definition</li>
<li>U+3322 SQUARE SENTI: not included in any glyphset definition</li>
<li>U+3323 SQUARE SENTO: not included in any glyphset definition</li>
<li>U+3326 SQUARE DORU: not included in any glyphset definition</li>
<li>U+3327 SQUARE TON: not included in any glyphset definition</li>
<li>U+332B SQUARE PAASENTO: not included in any glyphset definition</li>
<li>U+3336 SQUARE HEKUTAARU: not included in any glyphset definition</li>
<li>U+333B SQUARE PEEZI: not included in any glyphset definition</li>
<li>U+3349 SQUARE MIRI: not included in any glyphset definition</li>
<li>U+334A SQUARE MIRIBAARU: not included in any glyphset definition</li>
<li>U+334D SQUARE MEETORU: not included in any glyphset definition</li>
<li>U+3351 SQUARE RITTORU: not included in any glyphset definition</li>
<li>U+3357 SQUARE WATTO: not included in any glyphset definition</li>
<li>U+337B SQUARE ERA NAME HEISEI: not included in any glyphset definition</li>
<li>U+337C SQUARE ERA NAME SYOUWA: not included in any glyphset definition</li>
<li>U+337D SQUARE ERA NAME TAISYOU: not included in any glyphset definition</li>
<li>U+337E SQUARE ERA NAME MEIZI: not included in any glyphset definition</li>
<li>U+338E SQUARE MG: not included in any glyphset definition</li>
<li>U+338F SQUARE KG: not included in any glyphset definition</li>
<li>U+339E SQUARE KM: not included in any glyphset definition</li>
<li>U+33C4 SQUARE CC: not included in any glyphset definition</li>
<li>U+33CD SQUARE KK: not included in any glyphset definition</li>
<li>U+3447 CJK UNIFIED IDEOGRAPH-3447: not included in any glyphset definition</li>
<li>U+344A CJK UNIFIED IDEOGRAPH-344A: not included in any glyphset definition</li>
<li>U+3473 CJK UNIFIED IDEOGRAPH-3473: not included in any glyphset definition</li>
<li>U+34E4 CJK UNIFIED IDEOGRAPH-34E4: not included in any glyphset definition</li>
<li>U+356E CJK UNIFIED IDEOGRAPH-356E: not included in any glyphset definition</li>
<li>U+3577 CJK UNIFIED IDEOGRAPH-3577: not included in any glyphset definition</li>
<li>U+35A1 CJK UNIFIED IDEOGRAPH-35A1: not included in any glyphset definition</li>
<li>U+35AD CJK UNIFIED IDEOGRAPH-35AD: not included in any glyphset definition</li>
<li>U+35BF CJK UNIFIED IDEOGRAPH-35BF: not included in any glyphset definition</li>
<li>U+35CE CJK UNIFIED IDEOGRAPH-35CE: not included in any glyphset definition</li>
<li>U+35F3 CJK UNIFIED IDEOGRAPH-35F3: not included in any glyphset definition</li>
<li>U+35FE CJK UNIFIED IDEOGRAPH-35FE: not included in any glyphset definition</li>
<li>U+360E CJK UNIFIED IDEOGRAPH-360E: not included in any glyphset definition</li>
<li>U+361A CJK UNIFIED IDEOGRAPH-361A: not included in any glyphset definition</li>
<li>U+364D CJK UNIFIED IDEOGRAPH-364D: not included in any glyphset definition</li>
<li>U+3658 CJK UNIFIED IDEOGRAPH-3658: not included in any glyphset definition</li>
<li>U+3666 CJK UNIFIED IDEOGRAPH-3666: not included in any glyphset definition</li>
<li>U+36C3 CJK UNIFIED IDEOGRAPH-36C3: not included in any glyphset definition</li>
<li>U+36DA CJK UNIFIED IDEOGRAPH-36DA: not included in any glyphset definition</li>
<li>U+36F9 CJK UNIFIED IDEOGRAPH-36F9: not included in any glyphset definition</li>
<li>U+37C3 CJK UNIFIED IDEOGRAPH-37C3: not included in any glyphset definition</li>
<li>U+3807 CJK UNIFIED IDEOGRAPH-3807: not included in any glyphset definition</li>
<li>U+3813 CJK UNIFIED IDEOGRAPH-3813: not included in any glyphset definition</li>
<li>U+3823 CJK UNIFIED IDEOGRAPH-3823: not included in any glyphset definition</li>
<li>U+3918 CJK UNIFIED IDEOGRAPH-3918: not included in any glyphset definition</li>
<li>U+3944 CJK UNIFIED IDEOGRAPH-3944: not included in any glyphset definition</li>
<li>U+3960 CJK UNIFIED IDEOGRAPH-3960: not included in any glyphset definition</li>
<li>U+396E CJK UNIFIED IDEOGRAPH-396E: not included in any glyphset definition</li>
<li>U+39D0 CJK UNIFIED IDEOGRAPH-39D0: not included in any glyphset definition</li>
<li>U+39D1 CJK UNIFIED IDEOGRAPH-39D1: not included in any glyphset definition</li>
<li>U+39DF CJK UNIFIED IDEOGRAPH-39DF: not included in any glyphset definition</li>
<li>U+39F8 CJK UNIFIED IDEOGRAPH-39F8: not included in any glyphset definition</li>
<li>U+39FE CJK UNIFIED IDEOGRAPH-39FE: not included in any glyphset definition</li>
<li>U+3A18 CJK UNIFIED IDEOGRAPH-3A18: not included in any glyphset definition</li>
<li>U+3A52 CJK UNIFIED IDEOGRAPH-3A52: not included in any glyphset definition</li>
<li>U+3A67 CJK UNIFIED IDEOGRAPH-3A67: not included in any glyphset definition</li>
<li>U+3A73 CJK UNIFIED IDEOGRAPH-3A73: not included in any glyphset definition</li>
<li>U+3AF0 CJK UNIFIED IDEOGRAPH-3AF0: not included in any glyphset definition</li>
<li>U+3B0A CJK UNIFIED IDEOGRAPH-3B0A: not included in any glyphset definition</li>
<li>U+3B0E CJK UNIFIED IDEOGRAPH-3B0E: not included in any glyphset definition</li>
<li>U+3B1A CJK UNIFIED IDEOGRAPH-3B1A: not included in any glyphset definition</li>
<li>U+3B39 CJK UNIFIED IDEOGRAPH-3B39: not included in any glyphset definition</li>
<li>U+3B4E CJK UNIFIED IDEOGRAPH-3B4E: not included in any glyphset definition</li>
<li>U+3B55 CJK UNIFIED IDEOGRAPH-3B55: not included in any glyphset definition</li>
<li>U+3BBE CJK UNIFIED IDEOGRAPH-3BBE: not included in any glyphset definition</li>
<li>U+3C00 CJK UNIFIED IDEOGRAPH-3C00: not included in any glyphset definition</li>
<li>U+3CC7 CJK UNIFIED IDEOGRAPH-3CC7: not included in any glyphset definition</li>
<li>U+3CD8 CJK UNIFIED IDEOGRAPH-3CD8: not included in any glyphset definition</li>
<li>U+3CDA CJK UNIFIED IDEOGRAPH-3CDA: not included in any glyphset definition</li>
<li>U+3D14 CJK UNIFIED IDEOGRAPH-3D14: not included in any glyphset definition</li>
<li>U+3D50 CJK UNIFIED IDEOGRAPH-3D50: not included in any glyphset definition</li>
<li>U+3DB2 CJK UNIFIED IDEOGRAPH-3DB2: not included in any glyphset definition</li>
<li>U+3DE7 CJK UNIFIED IDEOGRAPH-3DE7: not included in any glyphset definition</li>
<li>U+3DEB CJK UNIFIED IDEOGRAPH-3DEB: not included in any glyphset definition</li>
<li>U+3E06 CJK UNIFIED IDEOGRAPH-3E06: not included in any glyphset definition</li>
<li>U+3E0C CJK UNIFIED IDEOGRAPH-3E0C: not included in any glyphset definition</li>
<li>U+3E74 CJK UNIFIED IDEOGRAPH-3E74: not included in any glyphset definition</li>
<li>U+3E84 CJK UNIFIED IDEOGRAPH-3E84: not included in any glyphset definition</li>
<li>U+3ED0 CJK UNIFIED IDEOGRAPH-3ED0: not included in any glyphset definition</li>
<li>U+3EEC CJK UNIFIED IDEOGRAPH-3EEC: not included in any glyphset definition</li>
<li>U+3F4F CJK UNIFIED IDEOGRAPH-3F4F: not included in any glyphset definition</li>
<li>U+3FE0 CJK UNIFIED IDEOGRAPH-3FE0: not included in any glyphset definition</li>
<li>U+4056 CJK UNIFIED IDEOGRAPH-4056: not included in any glyphset definition</li>
<li>U+4065 CJK UNIFIED IDEOGRAPH-4065: not included in any glyphset definition</li>
<li>U+406A CJK UNIFIED IDEOGRAPH-406A: not included in any glyphset definition</li>
<li>U+40AE CJK UNIFIED IDEOGRAPH-40AE: not included in any glyphset definition</li>
<li>U+40BB CJK UNIFIED IDEOGRAPH-40BB: not included in any glyphset definition</li>
<li>U+40C5 CJK UNIFIED IDEOGRAPH-40C5: not included in any glyphset definition</li>
<li>U+40CE CJK UNIFIED IDEOGRAPH-40CE: not included in any glyphset definition</li>
<li>U+40DF CJK UNIFIED IDEOGRAPH-40DF: not included in any glyphset definition</li>
<li>U+40EE CJK UNIFIED IDEOGRAPH-40EE: not included in any glyphset definition</li>
<li>U+4137 CJK UNIFIED IDEOGRAPH-4137: not included in any glyphset definition</li>
<li>U+415F CJK UNIFIED IDEOGRAPH-415F: not included in any glyphset definition</li>
<li>U+4337 CJK UNIFIED IDEOGRAPH-4337: not included in any glyphset definition</li>
<li>U+4339 CJK UNIFIED IDEOGRAPH-4339: not included in any glyphset definition</li>
<li>U+4383 CJK UNIFIED IDEOGRAPH-4383: not included in any glyphset definition</li>
<li>U+4396 CJK UNIFIED IDEOGRAPH-4396: not included in any glyphset definition</li>
<li>U+43DD CJK UNIFIED IDEOGRAPH-43DD: not included in any glyphset definition</li>
<li>U+43E1 CJK UNIFIED IDEOGRAPH-43E1: not included in any glyphset definition</li>
<li>U+43F2 CJK UNIFIED IDEOGRAPH-43F2: not included in any glyphset definition</li>
<li>U+4403 CJK UNIFIED IDEOGRAPH-4403: not included in any glyphset definition</li>
<li>U+44D6 CJK UNIFIED IDEOGRAPH-44D6: not included in any glyphset definition</li>
<li>U+44DB CJK UNIFIED IDEOGRAPH-44DB: not included in any glyphset definition</li>
<li>U+44E3 CJK UNIFIED IDEOGRAPH-44E3: not included in any glyphset definition</li>
<li>U+44E8 CJK UNIFIED IDEOGRAPH-44E8: not included in any glyphset definition</li>
<li>U+44EA CJK UNIFIED IDEOGRAPH-44EA: not included in any glyphset definition</li>
<li>U+44EB CJK UNIFIED IDEOGRAPH-44EB: not included in any glyphset definition</li>
<li>U+44EC CJK UNIFIED IDEOGRAPH-44EC: not included in any glyphset definition</li>
<li>U+45D6 CJK UNIFIED IDEOGRAPH-45D6: not included in any glyphset definition</li>
<li>U+45DB CJK UNIFIED IDEOGRAPH-45DB: not included in any glyphset definition</li>
<li>U+45EA CJK UNIFIED IDEOGRAPH-45EA: not included in any glyphset definition</li>
<li>U+45F4 CJK UNIFIED IDEOGRAPH-45F4: not included in any glyphset definition</li>
<li>U+4606 CJK UNIFIED IDEOGRAPH-4606: not included in any glyphset definition</li>
<li>U+4723 CJK UNIFIED IDEOGRAPH-4723: not included in any glyphset definition</li>
<li>U+4729 CJK UNIFIED IDEOGRAPH-4729: not included in any glyphset definition</li>
<li>U+4759 CJK UNIFIED IDEOGRAPH-4759: not included in any glyphset definition</li>
<li>U+47F4 CJK UNIFIED IDEOGRAPH-47F4: not included in any glyphset definition</li>
<li>U+4875 CJK UNIFIED IDEOGRAPH-4875: not included in any glyphset definition</li>
<li>U+48B5 CJK UNIFIED IDEOGRAPH-48B5: not included in any glyphset definition</li>
<li>U+48BA CJK UNIFIED IDEOGRAPH-48BA: not included in any glyphset definition</li>
<li>U+48BC CJK UNIFIED IDEOGRAPH-48BC: not included in any glyphset definition</li>
<li>U+48C5 CJK UNIFIED IDEOGRAPH-48C5: not included in any glyphset definition</li>
<li>U+48D3 CJK UNIFIED IDEOGRAPH-48D3: not included in any glyphset definition</li>
<li>U+48D8 CJK UNIFIED IDEOGRAPH-48D8: not included in any glyphset definition</li>
<li>U+4951 CJK UNIFIED IDEOGRAPH-4951: not included in any glyphset definition</li>
<li>U+4955 CJK UNIFIED IDEOGRAPH-4955: not included in any glyphset definition</li>
<li>U+497D CJK UNIFIED IDEOGRAPH-497D: not included in any glyphset definition</li>
<li>U+4983 CJK UNIFIED IDEOGRAPH-4983: not included in any glyphset definition</li>
<li>U+4986 CJK UNIFIED IDEOGRAPH-4986: not included in any glyphset definition</li>
<li>U+49D1 CJK UNIFIED IDEOGRAPH-49D1: not included in any glyphset definition</li>
<li>U+4A12 CJK UNIFIED IDEOGRAPH-4A12: not included in any glyphset definition</li>
<li>U+4AB8 CJK UNIFIED IDEOGRAPH-4AB8: not included in any glyphset definition</li>
<li>U+4B84 CJK UNIFIED IDEOGRAPH-4B84: not included in any glyphset definition</li>
<li>U+4C3E CJK UNIFIED IDEOGRAPH-4C3E: not included in any glyphset definition</li>
<li>U+4C7D CJK UNIFIED IDEOGRAPH-4C7D: not included in any glyphset definition</li>
<li>U+4C81 CJK UNIFIED IDEOGRAPH-4C81: not included in any glyphset definition</li>
<li>U+4C85 CJK UNIFIED IDEOGRAPH-4C85: not included in any glyphset definition</li>
<li>U+4C98 CJK UNIFIED IDEOGRAPH-4C98: not included in any glyphset definition</li>
<li>U+4C9F CJK UNIFIED IDEOGRAPH-4C9F: not included in any glyphset definition</li>
<li>U+4CA0 CJK UNIFIED IDEOGRAPH-4CA0: not included in any glyphset definition</li>
<li>U+4CA1 CJK UNIFIED IDEOGRAPH-4CA1: not included in any glyphset definition</li>
<li>U+4CA2 CJK UNIFIED IDEOGRAPH-4CA2: not included in any glyphset definition</li>
<li>U+4CB3 CJK UNIFIED IDEOGRAPH-4CB3: not included in any glyphset definition</li>
<li>U+4D08 CJK UNIFIED IDEOGRAPH-4D08: not included in any glyphset definition</li>
<li>U+4D09 CJK UNIFIED IDEOGRAPH-4D09: not included in any glyphset definition</li>
<li>U+4D13 CJK UNIFIED IDEOGRAPH-4D13: not included in any glyphset definition</li>
<li>U+4D14 CJK UNIFIED IDEOGRAPH-4D14: not included in any glyphset definition</li>
<li>U+4D15 CJK UNIFIED IDEOGRAPH-4D15: not included in any glyphset definition</li>
<li>U+4D16 CJK UNIFIED IDEOGRAPH-4D16: not included in any glyphset definition</li>
<li>U+4D17 CJK UNIFIED IDEOGRAPH-4D17: not included in any glyphset definition</li>
<li>U+4D18 CJK UNIFIED IDEOGRAPH-4D18: not included in any glyphset definition</li>
<li>U+4D19 CJK UNIFIED IDEOGRAPH-4D19: not included in any glyphset definition</li>
<li>U+4DAE CJK UNIFIED IDEOGRAPH-4DAE: not included in any glyphset definition</li>
<li>U+4E0C CJK UNIFIED IDEOGRAPH-4E0C: not included in any glyphset definition</li>
<li>U+4E0F CJK UNIFIED IDEOGRAPH-4E0F: not included in any glyphset definition</li>
<li>U+4E47 CJK UNIFIED IDEOGRAPH-4E47: not included in any glyphset definition</li>
<li>U+4E6B CJK UNIFIED IDEOGRAPH-4E6B: not included in any glyphset definition</li>
<li>U+4E6D CJK UNIFIED IDEOGRAPH-4E6D: not included in any glyphset definition</li>
<li>U+4E76 CJK UNIFIED IDEOGRAPH-4E76: not included in any glyphset definition</li>
<li>U+4E77 CJK UNIFIED IDEOGRAPH-4E77: not included in any glyphset definition</li>
<li>U+4E78 CJK UNIFIED IDEOGRAPH-4E78: not included in any glyphset definition</li>
<li>U+4E90 CJK UNIFIED IDEOGRAPH-4E90: not included in any glyphset definition</li>
<li>U+4EB8 CJK UNIFIED IDEOGRAPH-4EB8: not included in any glyphset definition</li>
<li>U+4EB9 CJK UNIFIED IDEOGRAPH-4EB9: not included in any glyphset definition</li>
<li>U+4EBC CJK UNIFIED IDEOGRAPH-4EBC: not included in any glyphset definition</li>
<li>U+4EC9 CJK UNIFIED IDEOGRAPH-4EC9: not included in any glyphset definition</li>
<li>U+4EEB CJK UNIFIED IDEOGRAPH-4EEB: not included in any glyphset definition</li>
<li>U+4EF3 CJK UNIFIED IDEOGRAPH-4EF3: not included in any glyphset definition</li>
<li>U+4EFC CJK UNIFIED IDEOGRAPH-4EFC: not included in any glyphset definition</li>
<li>U+4F00 CJK UNIFIED IDEOGRAPH-4F00: not included in any glyphset definition</li>
<li>U+4F03 CJK UNIFIED IDEOGRAPH-4F03: not included in any glyphset definition</li>
<li>U+4F08 CJK UNIFIED IDEOGRAPH-4F08: not included in any glyphset definition</li>
<li>U+4F0B CJK UNIFIED IDEOGRAPH-4F0B: not included in any glyphset definition</li>
<li>U+4F1B CJK UNIFIED IDEOGRAPH-4F1B: not included in any glyphset definition</li>
<li>U+4F23 CJK UNIFIED IDEOGRAPH-4F23: not included in any glyphset definition</li>
<li>U+4F25 CJK UNIFIED IDEOGRAPH-4F25: not included in any glyphset definition</li>
<li>U+4F32 CJK UNIFIED IDEOGRAPH-4F32: not included in any glyphset definition</li>
<li>U+4F39 CJK UNIFIED IDEOGRAPH-4F39: not included in any glyphset definition</li>
<li>U+4F3E CJK UNIFIED IDEOGRAPH-4F3E: not included in any glyphset definition</li>
<li>U+4F41 CJK UNIFIED IDEOGRAPH-4F41: not included in any glyphset definition</li>
<li>U+4F56 CJK UNIFIED IDEOGRAPH-4F56: not included in any glyphset definition</li>
<li>U+4F67 CJK UNIFIED IDEOGRAPH-4F67: not included in any glyphset definition</li>
<li>U+4F6B CJK UNIFIED IDEOGRAPH-4F6B: not included in any glyphset definition</li>
<li>U+4F6E CJK UNIFIED IDEOGRAPH-4F6E: not included in any glyphset definition</li>
<li>U+4F74 CJK UNIFIED IDEOGRAPH-4F74: not included in any glyphset definition</li>
<li>U+4F81 CJK UNIFIED IDEOGRAPH-4F81: not included in any glyphset definition</li>
<li>U+4F82 CJK UNIFIED IDEOGRAPH-4F82: not included in any glyphset definition</li>
<li>U+4F89 CJK UNIFIED IDEOGRAPH-4F89: not included in any glyphset definition</li>
<li>U+4F8A CJK UNIFIED IDEOGRAPH-4F8A: not included in any glyphset definition</li>
<li>U+4F92 CJK UNIFIED IDEOGRAPH-4F92: not included in any glyphset definition</li>
<li>U+4F94 CJK UNIFIED IDEOGRAPH-4F94: not included in any glyphset definition</li>
<li>U+4F9A CJK UNIFIED IDEOGRAPH-4F9A: not included in any glyphset definition</li>
<li>U+4FB9 CJK UNIFIED IDEOGRAPH-4FB9: not included in any glyphset definition</li>
<li>U+4FC1 CJK UNIFIED IDEOGRAPH-4FC1: not included in any glyphset definition</li>
<li>U+4FC9 CJK UNIFIED IDEOGRAPH-4FC9: not included in any glyphset definition</li>
<li>U+4FD3 CJK UNIFIED IDEOGRAPH-4FD3: not included in any glyphset definition</li>
<li>U+4FD9 CJK UNIFIED IDEOGRAPH-4FD9: not included in any glyphset definition</li>
<li>U+4FDC CJK UNIFIED IDEOGRAPH-4FDC: not included in any glyphset definition</li>
<li>U+4FEB CJK UNIFIED IDEOGRAPH-4FEB: not included in any glyphset definition</li>
<li>U+4FFF CJK UNIFIED IDEOGRAPH-4FFF: not included in any glyphset definition</li>
<li>U+5002 CJK UNIFIED IDEOGRAPH-5002: not included in any glyphset definition</li>
<li>U+5008 CJK UNIFIED IDEOGRAPH-5008: not included in any glyphset definition</li>
<li>U+5013 CJK UNIFIED IDEOGRAPH-5013: not included in any glyphset definition</li>
<li>U+5015 CJK UNIFIED IDEOGRAPH-5015: not included in any glyphset definition</li>
<li>U+501E CJK UNIFIED IDEOGRAPH-501E: not included in any glyphset definition</li>
<li>U+5027 CJK UNIFIED IDEOGRAPH-5027: not included in any glyphset definition</li>
<li>U+5032 CJK UNIFIED IDEOGRAPH-5032: not included in any glyphset definition</li>
<li>U+503B CJK UNIFIED IDEOGRAPH-503B: not included in any glyphset definition</li>
<li>U+5040 CJK UNIFIED IDEOGRAPH-5040: not included in any glyphset definition</li>
<li>U+5041 CJK UNIFIED IDEOGRAPH-5041: not included in any glyphset definition</li>
<li>U+5042 CJK UNIFIED IDEOGRAPH-5042: not included in any glyphset definition</li>
<li>U+5046 CJK UNIFIED IDEOGRAPH-5046: not included in any glyphset definition</li>
<li>U+5053 CJK UNIFIED IDEOGRAPH-5053: not included in any glyphset definition</li>
<li>U+5061 CJK UNIFIED IDEOGRAPH-5061: not included in any glyphset definition</li>
<li>U+506D CJK UNIFIED IDEOGRAPH-506D: not included in any glyphset definition</li>
<li>U+506F CJK UNIFIED IDEOGRAPH-506F: not included in any glyphset definition</li>
<li>U+5070 CJK UNIFIED IDEOGRAPH-5070: not included in any glyphset definition</li>
<li>U+507A CJK UNIFIED IDEOGRAPH-507A: not included in any glyphset definition</li>
<li>U+507E CJK UNIFIED IDEOGRAPH-507E: not included in any glyphset definition</li>
<li>U+5083 CJK UNIFIED IDEOGRAPH-5083: not included in any glyphset definition</li>
<li>U+5089 CJK UNIFIED IDEOGRAPH-5089: not included in any glyphset definition</li>
<li>U+508C CJK UNIFIED IDEOGRAPH-508C: not included in any glyphset definition</li>
<li>U+5092 CJK UNIFIED IDEOGRAPH-5092: not included in any glyphset definition</li>
<li>U+5094 CJK UNIFIED IDEOGRAPH-5094: not included in any glyphset definition</li>
<li>U+5095 CJK UNIFIED IDEOGRAPH-5095: not included in any glyphset definition</li>
<li>U+5096 CJK UNIFIED IDEOGRAPH-5096: not included in any glyphset definition</li>
<li>U+50A7 CJK UNIFIED IDEOGRAPH-50A7: not included in any glyphset definition</li>
<li>U+50AA CJK UNIFIED IDEOGRAPH-50AA: not included in any glyphset definition</li>
<li>U+50AF CJK UNIFIED IDEOGRAPH-50AF: not included in any glyphset definition</li>
<li>U+50BA CJK UNIFIED IDEOGRAPH-50BA: not included in any glyphset definition</li>
<li>U+50C7 CJK UNIFIED IDEOGRAPH-50C7: not included in any glyphset definition</li>
<li>U+50CE CJK UNIFIED IDEOGRAPH-50CE: not included in any glyphset definition</li>
<li>U+50D4 CJK UNIFIED IDEOGRAPH-50D4: not included in any glyphset definition</li>
<li>U+50D8 CJK UNIFIED IDEOGRAPH-50D8: not included in any glyphset definition</li>
<li>U+50E4 CJK UNIFIED IDEOGRAPH-50E4: not included in any glyphset definition</li>
<li>U+50E6 CJK UNIFIED IDEOGRAPH-50E6: not included in any glyphset definition</li>
<li>U+50E8 CJK UNIFIED IDEOGRAPH-50E8: not included in any glyphset definition</li>
<li>U+50E9 CJK UNIFIED IDEOGRAPH-50E9: not included in any glyphset definition</li>
<li>U+50EB CJK UNIFIED IDEOGRAPH-50EB: not included in any glyphset definition</li>
<li>U+50EC CJK UNIFIED IDEOGRAPH-50EC: not included in any glyphset definition</li>
<li>U+50F0 CJK UNIFIED IDEOGRAPH-50F0: not included in any glyphset definition</li>
<li>U+50FF CJK UNIFIED IDEOGRAPH-50FF: not included in any glyphset definition</li>
<li>U+5105 CJK UNIFIED IDEOGRAPH-5105: not included in any glyphset definition</li>
<li>U+5107 CJK UNIFIED IDEOGRAPH-5107: not included in any glyphset definition</li>
<li>U+5110 CJK UNIFIED IDEOGRAPH-5110: not included in any glyphset definition</li>
<li>U+5126 CJK UNIFIED IDEOGRAPH-5126: not included in any glyphset definition</li>
<li>U+5133 CJK UNIFIED IDEOGRAPH-5133: not included in any glyphset definition</li>
<li>U+514A CJK UNIFIED IDEOGRAPH-514A: not included in any glyphset definition</li>
<li>U+5155 CJK UNIFIED IDEOGRAPH-5155: not included in any glyphset definition</li>
<li>U+5159 CJK UNIFIED IDEOGRAPH-5159: not included in any glyphset definition</li>
<li>U+515B CJK UNIFIED IDEOGRAPH-515B: not included in any glyphset definition</li>
<li>U+515D CJK UNIFIED IDEOGRAPH-515D: not included in any glyphset definition</li>
<li>U+515E CJK UNIFIED IDEOGRAPH-515E: not included in any glyphset definition</li>
<li>U+5161 CJK UNIFIED IDEOGRAPH-5161: not included in any glyphset definition</li>
<li>U+5163 CJK UNIFIED IDEOGRAPH-5163: not included in any glyphset definition</li>
<li>U+5164 CJK UNIFIED IDEOGRAPH-5164: not included in any glyphset definition</li>
<li>U+5181 CJK UNIFIED IDEOGRAPH-5181: not included in any glyphset definition</li>
<li>U+5194 CJK UNIFIED IDEOGRAPH-5194: not included in any glyphset definition</li>
<li>U+519A CJK UNIFIED IDEOGRAPH-519A: not included in any glyphset definition</li>
<li>U+519D CJK UNIFIED IDEOGRAPH-519D: not included in any glyphset definition</li>
<li>U+51AE CJK UNIFIED IDEOGRAPH-51AE: not included in any glyphset definition</li>
<li>U+51BE CJK UNIFIED IDEOGRAPH-51BE: not included in any glyphset definition</li>
<li>U+51C3 CJK UNIFIED IDEOGRAPH-51C3: not included in any glyphset definition</li>
<li>U+51CA CJK UNIFIED IDEOGRAPH-51CA: not included in any glyphset definition</li>
<li>U+51D8 CJK UNIFIED IDEOGRAPH-51D8: not included in any glyphset definition</li>
<li>U+51DE CJK UNIFIED IDEOGRAPH-51DE: not included in any glyphset definition</li>
<li>U+51EC CJK UNIFIED IDEOGRAPH-51EC: not included in any glyphset definition</li>
<li>U+51F4 CJK UNIFIED IDEOGRAPH-51F4: not included in any glyphset definition</li>
<li>U+5215 CJK UNIFIED IDEOGRAPH-5215: not included in any glyphset definition</li>
<li>U+5216 CJK UNIFIED IDEOGRAPH-5216: not included in any glyphset definition</li>
<li>U+522C CJK UNIFIED IDEOGRAPH-522C: not included in any glyphset definition</li>
<li>U+522D CJK UNIFIED IDEOGRAPH-522D: not included in any glyphset definition</li>
<li>U+523F CJK UNIFIED IDEOGRAPH-523F: not included in any glyphset definition</li>
<li>U+5240 CJK UNIFIED IDEOGRAPH-5240: not included in any glyphset definition</li>
<li>U+5245 CJK UNIFIED IDEOGRAPH-5245: not included in any glyphset definition</li>
<li>U+5255 CJK UNIFIED IDEOGRAPH-5255: not included in any glyphset definition</li>
<li>U+5257 CJK UNIFIED IDEOGRAPH-5257: not included in any glyphset definition</li>
<li>U+525F CJK UNIFIED IDEOGRAPH-525F: not included in any glyphset definition</li>
<li>U+5261 CJK UNIFIED IDEOGRAPH-5261: not included in any glyphset definition</li>
<li>U+5281 CJK UNIFIED IDEOGRAPH-5281: not included in any glyphset definition</li>
<li>U+5282 CJK UNIFIED IDEOGRAPH-5282: not included in any glyphset definition</li>
<li>U+528C CJK UNIFIED IDEOGRAPH-528C: not included in any glyphset definition</li>
<li>U+528F CJK UNIFIED IDEOGRAPH-528F: not included in any glyphset definition</li>
<li>U+5293 CJK UNIFIED IDEOGRAPH-5293: not included in any glyphset definition</li>
<li>U+529C CJK UNIFIED IDEOGRAPH-529C: not included in any glyphset definition</li>
<li>U+52A2 CJK UNIFIED IDEOGRAPH-52A2: not included in any glyphset definition</li>
<li>U+52AF CJK UNIFIED IDEOGRAPH-52AF: not included in any glyphset definition</li>
<li>U+52BB CJK UNIFIED IDEOGRAPH-52BB: not included in any glyphset definition</li>
<li>U+52C0 CJK UNIFIED IDEOGRAPH-52C0: not included in any glyphset definition</li>
<li>U+52D4 CJK UNIFIED IDEOGRAPH-52D4: not included in any glyphset definition</li>
<li>U+52DA CJK UNIFIED IDEOGRAPH-52DA: not included in any glyphset definition</li>
<li>U+52E9 CJK UNIFIED IDEOGRAPH-52E9: not included in any glyphset definition</li>
<li>U+52F1 CJK UNIFIED IDEOGRAPH-52F1: not included in any glyphset definition</li>
<li>U+52F7 CJK UNIFIED IDEOGRAPH-52F7: not included in any glyphset definition</li>
<li>U+5307 CJK UNIFIED IDEOGRAPH-5307: not included in any glyphset definition</li>
<li>U+530B CJK UNIFIED IDEOGRAPH-530B: not included in any glyphset definition</li>
<li>U+531C CJK UNIFIED IDEOGRAPH-531C: not included in any glyphset definition</li>
<li>U+5326 CJK UNIFIED IDEOGRAPH-5326: not included in any glyphset definition</li>
<li>U+532D CJK UNIFIED IDEOGRAPH-532D: not included in any glyphset definition</li>
<li>U+533C CJK UNIFIED IDEOGRAPH-533C: not included in any glyphset definition</li>
<li>U+5344 CJK UNIFIED IDEOGRAPH-5344: not included in any glyphset definition</li>
<li>U+5363 CJK UNIFIED IDEOGRAPH-5363: not included in any glyphset definition</li>
<li>U+5368 CJK UNIFIED IDEOGRAPH-5368: not included in any glyphset definition</li>
<li>U+536C CJK UNIFIED IDEOGRAPH-536C: not included in any glyphset definition</li>
<li>U+5372 CJK UNIFIED IDEOGRAPH-5372: not included in any glyphset definition</li>
<li>U+537A CJK UNIFIED IDEOGRAPH-537A: not included in any glyphset definition</li>
<li>U+537D CJK UNIFIED IDEOGRAPH-537D: not included in any glyphset definition</li>
<li>U+538E CJK UNIFIED IDEOGRAPH-538E: not included in any glyphset definition</li>
<li>U+5393 CJK UNIFIED IDEOGRAPH-5393: not included in any glyphset definition</li>
<li>U+5399 CJK UNIFIED IDEOGRAPH-5399: not included in any glyphset definition</li>
<li>U+53A3 CJK UNIFIED IDEOGRAPH-53A3: not included in any glyphset definition</li>
<li>U+53B4 CJK UNIFIED IDEOGRAPH-53B4: not included in any glyphset definition</li>
<li>U+53BE CJK UNIFIED IDEOGRAPH-53BE: not included in any glyphset definition</li>
<li>U+53C4 CJK UNIFIED IDEOGRAPH-53C4: not included in any glyphset definition</li>
<li>U+53C7 CJK UNIFIED IDEOGRAPH-53C7: not included in any glyphset definition</li>
<li>U+53DA CJK UNIFIED IDEOGRAPH-53DA: not included in any glyphset definition</li>
<li>U+53DD CJK UNIFIED IDEOGRAPH-53DD: not included in any glyphset definition</li>
<li>U+5447 CJK UNIFIED IDEOGRAPH-5447: not included in any glyphset definition</li>
<li>U+5452 CJK UNIFIED IDEOGRAPH-5452: not included in any glyphset definition</li>
<li>U+5456 CJK UNIFIED IDEOGRAPH-5456: not included in any glyphset definition</li>
<li>U+5459 CJK UNIFIED IDEOGRAPH-5459: not included in any glyphset definition</li>
<li>U+5463 CJK UNIFIED IDEOGRAPH-5463: not included in any glyphset definition</li>
<li>U+5488 CJK UNIFIED IDEOGRAPH-5488: not included in any glyphset definition</li>
<li>U+5489 CJK UNIFIED IDEOGRAPH-5489: not included in any glyphset definition</li>
<li>U+548A CJK UNIFIED IDEOGRAPH-548A: not included in any glyphset definition</li>
<li>U+548D CJK UNIFIED IDEOGRAPH-548D: not included in any glyphset definition</li>
<li>U+549C CJK UNIFIED IDEOGRAPH-549C: not included in any glyphset definition</li>
<li>U+549D CJK UNIFIED IDEOGRAPH-549D: not included in any glyphset definition</li>
<li>U+54A1 CJK UNIFIED IDEOGRAPH-54A1: not included in any glyphset definition</li>
<li>U+54BA CJK UNIFIED IDEOGRAPH-54BA: not included in any glyphset definition</li>
<li>U+54C3 CJK UNIFIED IDEOGRAPH-54C3: not included in any glyphset definition</li>
<li>U+54D3 CJK UNIFIED IDEOGRAPH-54D3: not included in any glyphset definition</li>
<li>U+54D5 CJK UNIFIED IDEOGRAPH-54D5: not included in any glyphset definition</li>
<li>U+54D9 CJK UNIFIED IDEOGRAPH-54D9: not included in any glyphset definition</li>
<li>U+54DC CJK UNIFIED IDEOGRAPH-54DC: not included in any glyphset definition</li>
<li>U+54F1 CJK UNIFIED IDEOGRAPH-54F1: not included in any glyphset definition</li>
<li>U+54F3 CJK UNIFIED IDEOGRAPH-54F3: not included in any glyphset definition</li>
<li>U+54FF CJK UNIFIED IDEOGRAPH-54FF: not included in any glyphset definition</li>
<li>U+550E CJK UNIFIED IDEOGRAPH-550E: not included in any glyphset definition</li>
<li>U+5513 CJK UNIFIED IDEOGRAPH-5513: not included in any glyphset definition</li>
<li>U+551A CJK UNIFIED IDEOGRAPH-551A: not included in any glyphset definition</li>
<li>U+551C CJK UNIFIED IDEOGRAPH-551C: not included in any glyphset definition</li>
<li>U+551D CJK UNIFIED IDEOGRAPH-551D: not included in any glyphset definition</li>
<li>U+551E CJK UNIFIED IDEOGRAPH-551E: not included in any glyphset definition</li>
<li>U+552A CJK UNIFIED IDEOGRAPH-552A: not included in any glyphset definition</li>
<li>U+553C CJK UNIFIED IDEOGRAPH-553C: not included in any glyphset definition</li>
<li>U+553F CJK UNIFIED IDEOGRAPH-553F: not included in any glyphset definition</li>
<li>U+554B CJK UNIFIED IDEOGRAPH-554B: not included in any glyphset definition</li>
<li>U+554D CJK UNIFIED IDEOGRAPH-554D: not included in any glyphset definition</li>
<li>U+5569 CJK UNIFIED IDEOGRAPH-5569: not included in any glyphset definition</li>
<li>U+5574 CJK UNIFIED IDEOGRAPH-5574: not included in any glyphset definition</li>
<li>U+5579 CJK UNIFIED IDEOGRAPH-5579: not included in any glyphset definition</li>
<li>U+5581 CJK UNIFIED IDEOGRAPH-5581: not included in any glyphset definition</li>
<li>U+5588 CJK UNIFIED IDEOGRAPH-5588: not included in any glyphset definition</li>
<li>U+55A4 CJK UNIFIED IDEOGRAPH-55A4: not included in any glyphset definition</li>
<li>U+55BC CJK UNIFIED IDEOGRAPH-55BC: not included in any glyphset definition</li>
<li>U+55BE CJK UNIFIED IDEOGRAPH-55BE: not included in any glyphset definition</li>
<li>U+55C9 CJK UNIFIED IDEOGRAPH-55C9: not included in any glyphset definition</li>
<li>U+55CA CJK UNIFIED IDEOGRAPH-55CA: not included in any glyphset definition</li>
<li>U+55CD CJK UNIFIED IDEOGRAPH-55CD: not included in any glyphset definition</li>
<li>U+55D0 CJK UNIFIED IDEOGRAPH-55D0: not included in any glyphset definition</li>
<li>U+55DE CJK UNIFIED IDEOGRAPH-55DE: not included in any glyphset definition</li>
<li>U+55E5 CJK UNIFIED IDEOGRAPH-55E5: not included in any glyphset definition</li>
<li>U+55E7 CJK UNIFIED IDEOGRAPH-55E7: not included in any glyphset definition</li>
<li>U+55EB CJK UNIFIED IDEOGRAPH-55EB: not included in any glyphset definition</li>
<li>U+55EC CJK UNIFIED IDEOGRAPH-55EC: not included in any glyphset definition</li>
<li>U+55F1 CJK UNIFIED IDEOGRAPH-55F1: not included in any glyphset definition</li>
<li>U+55F5 CJK UNIFIED IDEOGRAPH-55F5: not included in any glyphset definition</li>
<li>U+5601 CJK UNIFIED IDEOGRAPH-5601: not included in any glyphset definition</li>
<li>U+560F CJK UNIFIED IDEOGRAPH-560F: not included in any glyphset definition</li>
<li>U+5610 CJK UNIFIED IDEOGRAPH-5610: not included in any glyphset definition</li>
<li>U+5613 CJK UNIFIED IDEOGRAPH-5613: not included in any glyphset definition</li>
<li>U+5625 CJK UNIFIED IDEOGRAPH-5625: not included in any glyphset definition</li>
<li>U+5635 CJK UNIFIED IDEOGRAPH-5635: not included in any glyphset definition</li>
<li>U+563D CJK UNIFIED IDEOGRAPH-563D: not included in any glyphset definition</li>
<li>U+5640 CJK UNIFIED IDEOGRAPH-5640: not included in any glyphset definition</li>
<li>U+5643 CJK UNIFIED IDEOGRAPH-5643: not included in any glyphset definition</li>
<li>U+5647 CJK UNIFIED IDEOGRAPH-5647: not included in any glyphset definition</li>
<li>U+564D CJK UNIFIED IDEOGRAPH-564D: not included in any glyphset definition</li>
<li>U+565D CJK UNIFIED IDEOGRAPH-565D: not included in any glyphset definition</li>
<li>U+5666 CJK UNIFIED IDEOGRAPH-5666: not included in any glyphset definition</li>
<li>U+5672 CJK UNIFIED IDEOGRAPH-5672: not included in any glyphset definition</li>
<li>U+5684 CJK UNIFIED IDEOGRAPH-5684: not included in any glyphset definition</li>
<li>U+568C CJK UNIFIED IDEOGRAPH-568C: not included in any glyphset definition</li>
<li>U+569A CJK UNIFIED IDEOGRAPH-569A: not included in any glyphset definition</li>
<li>U+56A1 CJK UNIFIED IDEOGRAPH-56A1: not included in any glyphset definition</li>
<li>U+56A4 CJK UNIFIED IDEOGRAPH-56A4: not included in any glyphset definition</li>
<li>U+56A6 CJK UNIFIED IDEOGRAPH-56A6: not included in any glyphset definition</li>
<li>U+56AC CJK UNIFIED IDEOGRAPH-56AC: not included in any glyphset definition</li>
<li>U+56AD CJK UNIFIED IDEOGRAPH-56AD: not included in any glyphset definition</li>
<li>U+56B2 CJK UNIFIED IDEOGRAPH-56B2: not included in any glyphset definition</li>
<li>U+56B3 CJK UNIFIED IDEOGRAPH-56B3: not included in any glyphset definition</li>
<li>U+56BF CJK UNIFIED IDEOGRAPH-56BF: not included in any glyphset definition</li>
<li>U+56C5 CJK UNIFIED IDEOGRAPH-56C5: not included in any glyphset definition</li>
<li>U+56CC CJK UNIFIED IDEOGRAPH-56CC: not included in any glyphset definition</li>
<li>U+56D6 CJK UNIFIED IDEOGRAPH-56D6: not included in any glyphset definition</li>
<li>U+56F7 CJK UNIFIED IDEOGRAPH-56F7: not included in any glyphset definition</li>
<li>U+570A CJK UNIFIED IDEOGRAPH-570A: not included in any glyphset definition</li>
<li>U+570C CJK UNIFIED IDEOGRAPH-570C: not included in any glyphset definition</li>
<li>U+5710 CJK UNIFIED IDEOGRAPH-5710: not included in any glyphset definition</li>
<li>U+5719 CJK UNIFIED IDEOGRAPH-5719: not included in any glyphset definition</li>
<li>U+5722 CJK UNIFIED IDEOGRAPH-5722: not included in any glyphset definition</li>
<li>U+572B CJK UNIFIED IDEOGRAPH-572B: not included in any glyphset definition</li>
<li>U+572C CJK UNIFIED IDEOGRAPH-572C: not included in any glyphset definition</li>
<li>U+572F CJK UNIFIED IDEOGRAPH-572F: not included in any glyphset definition</li>
<li>U+5739 CJK UNIFIED IDEOGRAPH-5739: not included in any glyphset definition</li>
<li>U+574B CJK UNIFIED IDEOGRAPH-574B: not included in any glyphset definition</li>
<li>U+574C CJK UNIFIED IDEOGRAPH-574C: not included in any glyphset definition</li>
<li>U+5752 CJK UNIFIED IDEOGRAPH-5752: not included in any glyphset definition</li>
<li>U+5754 CJK UNIFIED IDEOGRAPH-5754: not included in any glyphset definition</li>
<li>U+5759 CJK UNIFIED IDEOGRAPH-5759: not included in any glyphset definition</li>
<li>U+575C CJK UNIFIED IDEOGRAPH-575C: not included in any glyphset definition</li>
<li>U+5765 CJK UNIFIED IDEOGRAPH-5765: not included in any glyphset definition</li>
<li>U+576C CJK UNIFIED IDEOGRAPH-576C: not included in any glyphset definition</li>
<li>U+576E CJK UNIFIED IDEOGRAPH-576E: not included in any glyphset definition</li>
<li>U+5770 CJK UNIFIED IDEOGRAPH-5770: not included in any glyphset definition</li>
<li>U+5776 CJK UNIFIED IDEOGRAPH-5776: not included in any glyphset definition</li>
<li>U+577C CJK UNIFIED IDEOGRAPH-577C: not included in any glyphset definition</li>
<li>U+577D CJK UNIFIED IDEOGRAPH-577D: not included in any glyphset definition</li>
<li>U+5786 CJK UNIFIED IDEOGRAPH-5786: not included in any glyphset definition</li>
<li>U+578C CJK UNIFIED IDEOGRAPH-578C: not included in any glyphset definition</li>
<li>U+578F CJK UNIFIED IDEOGRAPH-578F: not included in any glyphset definition</li>
<li>U+5795 CJK UNIFIED IDEOGRAPH-5795: not included in any glyphset definition</li>
<li>U+5799 CJK UNIFIED IDEOGRAPH-5799: not included in any glyphset definition</li>
<li>U+579E CJK UNIFIED IDEOGRAPH-579E: not included in any glyphset definition</li>
<li>U+57AC CJK UNIFIED IDEOGRAPH-57AC: not included in any glyphset definition</li>
<li>U+57AF CJK UNIFIED IDEOGRAPH-57AF: not included in any glyphset definition</li>
<li>U+57B1 CJK UNIFIED IDEOGRAPH-57B1: not included in any glyphset definition</li>
<li>U+57B2 CJK UNIFIED IDEOGRAPH-57B2: not included in any glyphset definition</li>
<li>U+57B8 CJK UNIFIED IDEOGRAPH-57B8: not included in any glyphset definition</li>
<li>U+57BA CJK UNIFIED IDEOGRAPH-57BA: not included in any glyphset definition</li>
<li>U+57BB CJK UNIFIED IDEOGRAPH-57BB: not included in any glyphset definition</li>
<li>U+57BF CJK UNIFIED IDEOGRAPH-57BF: not included in any glyphset definition</li>
<li>U+57C8 CJK UNIFIED IDEOGRAPH-57C8: not included in any glyphset definition</li>
<li>U+57CF CJK UNIFIED IDEOGRAPH-57CF: not included in any glyphset definition</li>
<li>U+57D8 CJK UNIFIED IDEOGRAPH-57D8: not included in any glyphset definition</li>
<li>U+57DD CJK UNIFIED IDEOGRAPH-57DD: not included in any glyphset definition</li>
<li>U+57DE CJK UNIFIED IDEOGRAPH-57DE: not included in any glyphset definition</li>
<li>U+57E8 CJK UNIFIED IDEOGRAPH-57E8: not included in any glyphset definition</li>
<li>U+57EA CJK UNIFIED IDEOGRAPH-57EA: not included in any glyphset definition</li>
<li>U+57EB CJK UNIFIED IDEOGRAPH-57EB: not included in any glyphset definition</li>
<li>U+57F0 CJK UNIFIED IDEOGRAPH-57F0: not included in any glyphset definition</li>
<li>U+57FB CJK UNIFIED IDEOGRAPH-57FB: not included in any glyphset definition</li>
<li>U+57FD CJK UNIFIED IDEOGRAPH-57FD: not included in any glyphset definition</li>
<li>U+5808 CJK UNIFIED IDEOGRAPH-5808: not included in any glyphset definition</li>
<li>U+580C CJK UNIFIED IDEOGRAPH-580C: not included in any glyphset definition</li>
<li>U+580D CJK UNIFIED IDEOGRAPH-580D: not included in any glyphset definition</li>
<li>U+580E CJK UNIFIED IDEOGRAPH-580E: not included in any glyphset definition</li>
<li>U+5810 CJK UNIFIED IDEOGRAPH-5810: not included in any glyphset definition</li>
<li>U+5816 CJK UNIFIED IDEOGRAPH-5816: not included in any glyphset definition</li>
<li>U+5817 CJK UNIFIED IDEOGRAPH-5817: not included in any glyphset definition</li>
<li>U+581E CJK UNIFIED IDEOGRAPH-581E: not included in any glyphset definition</li>
<li>U+5820 CJK UNIFIED IDEOGRAPH-5820: not included in any glyphset definition</li>
<li>U+5823 CJK UNIFIED IDEOGRAPH-5823: not included in any glyphset definition</li>
<li>U+5827 CJK UNIFIED IDEOGRAPH-5827: not included in any glyphset definition</li>
<li>U+5828 CJK UNIFIED IDEOGRAPH-5828: not included in any glyphset definition</li>
<li>U+582D CJK UNIFIED IDEOGRAPH-582D: not included in any glyphset definition</li>
<li>U+5832 CJK UNIFIED IDEOGRAPH-5832: not included in any glyphset definition</li>
<li>U+583C CJK UNIFIED IDEOGRAPH-583C: not included in any glyphset definition</li>
<li>U+583E CJK UNIFIED IDEOGRAPH-583E: not included in any glyphset definition</li>
<li>U+5843 CJK UNIFIED IDEOGRAPH-5843: not included in any glyphset definition</li>
<li>U+5845 CJK UNIFIED IDEOGRAPH-5845: not included in any glyphset definition</li>
<li>U+5846 CJK UNIFIED IDEOGRAPH-5846: not included in any glyphset definition</li>
<li>U+5848 CJK UNIFIED IDEOGRAPH-5848: not included in any glyphset definition</li>
<li>U+584F CJK UNIFIED IDEOGRAPH-584F: not included in any glyphset definition</li>
<li>U+585D CJK UNIFIED IDEOGRAPH-585D: not included in any glyphset definition</li>
<li>U+5861 CJK UNIFIED IDEOGRAPH-5861: not included in any glyphset definition</li>
<li>U+5864 CJK UNIFIED IDEOGRAPH-5864: not included in any glyphset definition</li>
<li>U+5865 CJK UNIFIED IDEOGRAPH-5865: not included in any glyphset definition</li>
<li>U+586E CJK UNIFIED IDEOGRAPH-586E: not included in any glyphset definition</li>
<li>U+586F CJK UNIFIED IDEOGRAPH-586F: not included in any glyphset definition</li>
<li>U+5878 CJK UNIFIED IDEOGRAPH-5878: not included in any glyphset definition</li>
<li>U+587C CJK UNIFIED IDEOGRAPH-587C: not included in any glyphset definition</li>
<li>U+587D CJK UNIFIED IDEOGRAPH-587D: not included in any glyphset definition</li>
<li>U+587F CJK UNIFIED IDEOGRAPH-587F: not included in any glyphset definition</li>
<li>U+5881 CJK UNIFIED IDEOGRAPH-5881: not included in any glyphset definition</li>
<li>U+5888 CJK UNIFIED IDEOGRAPH-5888: not included in any glyphset definition</li>
<li>U+5890 CJK UNIFIED IDEOGRAPH-5890: not included in any glyphset definition</li>
<li>U+5895 CJK UNIFIED IDEOGRAPH-5895: not included in any glyphset definition</li>
<li>U+58A1 CJK UNIFIED IDEOGRAPH-58A1: not included in any glyphset definition</li>
<li>U+58A3 CJK UNIFIED IDEOGRAPH-58A3: not included in any glyphset definition</li>
<li>U+58B2 CJK UNIFIED IDEOGRAPH-58B2: not included in any glyphset definition</li>
<li>U+58BC CJK UNIFIED IDEOGRAPH-58BC: not included in any glyphset definition</li>
<li>U+58C2 CJK UNIFIED IDEOGRAPH-58C2: not included in any glyphset definition</li>
<li>U+58CE CJK UNIFIED IDEOGRAPH-58CE: not included in any glyphset definition</li>
<li>U+58DA CJK UNIFIED IDEOGRAPH-58DA: not included in any glyphset definition</li>
<li>U+58E0 CJK UNIFIED IDEOGRAPH-58E0: not included in any glyphset definition</li>
<li>U+58EA CJK UNIFIED IDEOGRAPH-58EA: not included in any glyphset definition</li>
<li>U+58F8 CJK UNIFIED IDEOGRAPH-58F8: not included in any glyphset definition</li>
<li>U+5924 CJK UNIFIED IDEOGRAPH-5924: not included in any glyphset definition</li>
<li>U+593C CJK UNIFIED IDEOGRAPH-593C: not included in any glyphset definition</li>
<li>U+593D CJK UNIFIED IDEOGRAPH-593D: not included in any glyphset definition</li>
<li>U+5941 CJK UNIFIED IDEOGRAPH-5941: not included in any glyphset definition</li>
<li>U+5953 CJK UNIFIED IDEOGRAPH-5953: not included in any glyphset definition</li>
<li>U+595B CJK UNIFIED IDEOGRAPH-595B: not included in any glyphset definition</li>
<li>U+595D CJK UNIFIED IDEOGRAPH-595D: not included in any glyphset definition</li>
<li>U+5961 CJK UNIFIED IDEOGRAPH-5961: not included in any glyphset definition</li>
<li>U+5963 CJK UNIFIED IDEOGRAPH-5963: not included in any glyphset definition</li>
<li>U+596B CJK UNIFIED IDEOGRAPH-596B: not included in any glyphset definition</li>
<li>U+59A7 CJK UNIFIED IDEOGRAPH-59A7: not included in any glyphset definition</li>
<li>U+59AD CJK UNIFIED IDEOGRAPH-59AD: not included in any glyphset definition</li>
<li>U+59B8 CJK UNIFIED IDEOGRAPH-59B8: not included in any glyphset definition</li>
<li>U+59C3 CJK UNIFIED IDEOGRAPH-59C3: not included in any glyphset definition</li>
<li>U+59C5 CJK UNIFIED IDEOGRAPH-59C5: not included in any glyphset definition</li>
<li>U+59C8 CJK UNIFIED IDEOGRAPH-59C8: not included in any glyphset definition</li>
<li>U+59F1 CJK UNIFIED IDEOGRAPH-59F1: not included in any glyphset definition</li>
<li>U+59F8 CJK UNIFIED IDEOGRAPH-59F8: not included in any glyphset definition</li>
<li>U+59FD CJK UNIFIED IDEOGRAPH-59FD: not included in any glyphset definition</li>
<li>U+5A00 CJK UNIFIED IDEOGRAPH-5A00: not included in any glyphset definition</li>
<li>U+5A19 CJK UNIFIED IDEOGRAPH-5A19: not included in any glyphset definition</li>
<li>U+5A2B CJK UNIFIED IDEOGRAPH-5A2B: not included in any glyphset definition</li>
<li>U+5A2D CJK UNIFIED IDEOGRAPH-5A2D: not included in any glyphset definition</li>
<li>U+5A33 CJK UNIFIED IDEOGRAPH-5A33: not included in any glyphset definition</li>
<li>U+5A4C CJK UNIFIED IDEOGRAPH-5A4C: not included in any glyphset definition</li>
<li>U+5A4D CJK UNIFIED IDEOGRAPH-5A4D: not included in any glyphset definition</li>
<li>U+5A58 CJK UNIFIED IDEOGRAPH-5A58: not included in any glyphset definition</li>
<li>U+5A60 CJK UNIFIED IDEOGRAPH-5A60: not included in any glyphset definition</li>
<li>U+5A64 CJK UNIFIED IDEOGRAPH-5A64: not included in any glyphset definition</li>
<li>U+5A7B CJK UNIFIED IDEOGRAPH-5A7B: not included in any glyphset definition</li>
<li>U+5A7C CJK UNIFIED IDEOGRAPH-5A7C: not included in any glyphset definition</li>
<li>U+5A82 CJK UNIFIED IDEOGRAPH-5A82: not included in any glyphset definition</li>
<li>U+5A93 CJK UNIFIED IDEOGRAPH-5A93: not included in any glyphset definition</li>
<li>U+5A96 CJK UNIFIED IDEOGRAPH-5A96: not included in any glyphset definition</li>
<li>U+5AA4 CJK UNIFIED IDEOGRAPH-5AA4: not included in any glyphset definition</li>
<li>U+5AAC CJK UNIFIED IDEOGRAPH-5AAC: not included in any glyphset definition</li>
<li>U+5AAD CJK UNIFIED IDEOGRAPH-5AAD: not included in any glyphset definition</li>
<li>U+5AAF CJK UNIFIED IDEOGRAPH-5AAF: not included in any glyphset definition</li>
<li>U+5AB1 CJK UNIFIED IDEOGRAPH-5AB1: not included in any glyphset definition</li>
<li>U+5AB4 CJK UNIFIED IDEOGRAPH-5AB4: not included in any glyphset definition</li>
<li>U+5AB5 CJK UNIFIED IDEOGRAPH-5AB5: not included in any glyphset definition</li>
<li>U+5AC4 CJK UNIFIED IDEOGRAPH-5AC4: not included in any glyphset definition</li>
<li>U+5AC8 CJK UNIFIED IDEOGRAPH-5AC8: not included in any glyphset definition</li>
<li>U+5AD5 CJK UNIFIED IDEOGRAPH-5AD5: not included in any glyphset definition</li>
<li>U+5AD9 CJK UNIFIED IDEOGRAPH-5AD9: not included in any glyphset definition</li>
<li>U+5ADC CJK UNIFIED IDEOGRAPH-5ADC: not included in any glyphset definition</li>
<li>U+5AE0 CJK UNIFIED IDEOGRAPH-5AE0: not included in any glyphset definition</li>
<li>U+5AEA CJK UNIFIED IDEOGRAPH-5AEA: not included in any glyphset definition</li>
<li>U+5AEB CJK UNIFIED IDEOGRAPH-5AEB: not included in any glyphset definition</li>
<li>U+5AED CJK UNIFIED IDEOGRAPH-5AED: not included in any glyphset definition</li>
<li>U+5AF1 CJK UNIFIED IDEOGRAPH-5AF1: not included in any glyphset definition</li>
<li>U+5AF2 CJK UNIFIED IDEOGRAPH-5AF2: not included in any glyphset definition</li>
<li>U+5AFD CJK UNIFIED IDEOGRAPH-5AFD: not included in any glyphset definition</li>
<li>U+5AFF CJK UNIFIED IDEOGRAPH-5AFF: not included in any glyphset definition</li>
<li>U+5B00 CJK UNIFIED IDEOGRAPH-5B00: not included in any glyphset definition</li>
<li>U+5B03 CJK UNIFIED IDEOGRAPH-5B03: not included in any glyphset definition</li>
<li>U+5B19 CJK UNIFIED IDEOGRAPH-5B19: not included in any glyphset definition</li>
<li>U+5B1D CJK UNIFIED IDEOGRAPH-5B1D: not included in any glyphset definition</li>
<li>U+5B25 CJK UNIFIED IDEOGRAPH-5B25: not included in any glyphset definition</li>
<li>U+5B4D CJK UNIFIED IDEOGRAPH-5B4D: not included in any glyphset definition</li>
<li>U+5B6D CJK UNIFIED IDEOGRAPH-5B6D: not included in any glyphset definition</li>
<li>U+5B82 CJK UNIFIED IDEOGRAPH-5B82: not included in any glyphset definition</li>
<li>U+5B84 CJK UNIFIED IDEOGRAPH-5B84: not included in any glyphset definition</li>
<li>U+5B96 CJK UNIFIED IDEOGRAPH-5B96: not included in any glyphset definition</li>
<li>U+5BA7 CJK UNIFIED IDEOGRAPH-5BA7: not included in any glyphset definition</li>
<li>U+5BC0 CJK UNIFIED IDEOGRAPH-5BC0: not included in any glyphset definition</li>
<li>U+5BC1 CJK UNIFIED IDEOGRAPH-5BC1: not included in any glyphset definition</li>
<li>U+5BCD CJK UNIFIED IDEOGRAPH-5BCD: not included in any glyphset definition</li>
<li>U+5BD7 CJK UNIFIED IDEOGRAPH-5BD7: not included in any glyphset definition</li>
<li>U+5BD8 CJK UNIFIED IDEOGRAPH-5BD8: not included in any glyphset definition</li>
<li>U+5BEF CJK UNIFIED IDEOGRAPH-5BEF: not included in any glyphset definition</li>
<li>U+5C19 CJK UNIFIED IDEOGRAPH-5C19: not included in any glyphset definition</li>
<li>U+5C1E CJK UNIFIED IDEOGRAPH-5C1E: not included in any glyphset definition</li>
<li>U+5C25 CJK UNIFIED IDEOGRAPH-5C25: not included in any glyphset definition</li>
<li>U+5C43 CJK UNIFIED IDEOGRAPH-5C43: not included in any glyphset definition</li>
<li>U+5C58 CJK UNIFIED IDEOGRAPH-5C58: not included in any glyphset definition</li>
<li>U+5C5B CJK UNIFIED IDEOGRAPH-5C5B: not included in any glyphset definition</li>
<li>U+5C5D CJK UNIFIED IDEOGRAPH-5C5D: not included in any glyphset definition</li>
<li>U+5C63 CJK UNIFIED IDEOGRAPH-5C63: not included in any glyphset definition</li>
<li>U+5C66 CJK UNIFIED IDEOGRAPH-5C66: not included in any glyphset definition</li>
<li>U+5C68 CJK UNIFIED IDEOGRAPH-5C68: not included in any glyphset definition</li>
<li>U+5C6D CJK UNIFIED IDEOGRAPH-5C6D: not included in any glyphset definition</li>
<li>U+5C7A CJK UNIFIED IDEOGRAPH-5C7A: not included in any glyphset definition</li>
<li>U+5C88 CJK UNIFIED IDEOGRAPH-5C88: not included in any glyphset definition</li>
<li>U+5C8A CJK UNIFIED IDEOGRAPH-5C8A: not included in any glyphset definition</li>
<li>U+5C8D CJK UNIFIED IDEOGRAPH-5C8D: not included in any glyphset definition</li>
<li>U+5C9C CJK UNIFIED IDEOGRAPH-5C9C: not included in any glyphset definition</li>
<li>U+5CA0 CJK UNIFIED IDEOGRAPH-5CA0: not included in any glyphset definition</li>
<li>U+5CA3 CJK UNIFIED IDEOGRAPH-5CA3: not included in any glyphset definition</li>
<li>U+5CB5 CJK UNIFIED IDEOGRAPH-5CB5: not included in any glyphset definition</li>
<li>U+5CBA CJK UNIFIED IDEOGRAPH-5CBA: not included in any glyphset definition</li>
<li>U+5CBD CJK UNIFIED IDEOGRAPH-5CBD: not included in any glyphset definition</li>
<li>U+5CC0 CJK UNIFIED IDEOGRAPH-5CC0: not included in any glyphset definition</li>
<li>U+5CC3 CJK UNIFIED IDEOGRAPH-5CC3: not included in any glyphset definition</li>
<li>U+5CD7 CJK UNIFIED IDEOGRAPH-5CD7: not included in any glyphset definition</li>
<li>U+5CD8 CJK UNIFIED IDEOGRAPH-5CD8: not included in any glyphset definition</li>
<li>U+5CDB CJK UNIFIED IDEOGRAPH-5CDB: not included in any glyphset definition</li>
<li>U+5CE3 CJK UNIFIED IDEOGRAPH-5CE3: not included in any glyphset definition</li>
<li>U+5CE7 CJK UNIFIED IDEOGRAPH-5CE7: not included in any glyphset definition</li>
<li>U+5CF1 CJK UNIFIED IDEOGRAPH-5CF1: not included in any glyphset definition</li>
<li>U+5CF5 CJK UNIFIED IDEOGRAPH-5CF5: not included in any glyphset definition</li>
<li>U+5CFF CJK UNIFIED IDEOGRAPH-5CFF: not included in any glyphset definition</li>
<li>U+5D00 CJK UNIFIED IDEOGRAPH-5D00: not included in any glyphset definition</li>
<li>U+5D04 CJK UNIFIED IDEOGRAPH-5D04: not included in any glyphset definition</li>
<li>U+5D0C CJK UNIFIED IDEOGRAPH-5D0C: not included in any glyphset definition</li>
<li>U+5D0D CJK UNIFIED IDEOGRAPH-5D0D: not included in any glyphset definition</li>
<li>U+5D10 CJK UNIFIED IDEOGRAPH-5D10: not included in any glyphset definition</li>
<li>U+5D12 CJK UNIFIED IDEOGRAPH-5D12: not included in any glyphset definition</li>
<li>U+5D1E CJK UNIFIED IDEOGRAPH-5D1E: not included in any glyphset definition</li>
<li>U+5D21 CJK UNIFIED IDEOGRAPH-5D21: not included in any glyphset definition</li>
<li>U+5D24 CJK UNIFIED IDEOGRAPH-5D24: not included in any glyphset definition</li>
<li>U+5D26 CJK UNIFIED IDEOGRAPH-5D26: not included in any glyphset definition</li>
<li>U+5D2C CJK UNIFIED IDEOGRAPH-5D2C: not included in any glyphset definition</li>
<li>U+5D36 CJK UNIFIED IDEOGRAPH-5D36: not included in any glyphset definition</li>
<li>U+5D3F CJK UNIFIED IDEOGRAPH-5D3F: not included in any glyphset definition</li>
<li>U+5D41 CJK UNIFIED IDEOGRAPH-5D41: not included in any glyphset definition</li>
<li>U+5D42 CJK UNIFIED IDEOGRAPH-5D42: not included in any glyphset definition</li>
<li>U+5D44 CJK UNIFIED IDEOGRAPH-5D44: not included in any glyphset definition</li>
<li>U+5D45 CJK UNIFIED IDEOGRAPH-5D45: not included in any glyphset definition</li>
<li>U+5D53 CJK UNIFIED IDEOGRAPH-5D53: not included in any glyphset definition</li>
<li>U+5D5A CJK UNIFIED IDEOGRAPH-5D5A: not included in any glyphset definition</li>
<li>U+5D5D CJK UNIFIED IDEOGRAPH-5D5D: not included in any glyphset definition</li>
<li>U+5D6B CJK UNIFIED IDEOGRAPH-5D6B: not included in any glyphset definition</li>
<li>U+5D6D CJK UNIFIED IDEOGRAPH-5D6D: not included in any glyphset definition</li>
<li>U+5D72 CJK UNIFIED IDEOGRAPH-5D72: not included in any glyphset definition</li>
<li>U+5D7D CJK UNIFIED IDEOGRAPH-5D7D: not included in any glyphset definition</li>
<li>U+5D81 CJK UNIFIED IDEOGRAPH-5D81: not included in any glyphset definition</li>
<li>U+5D8D CJK UNIFIED IDEOGRAPH-5D8D: not included in any glyphset definition</li>
<li>U+5D92 CJK UNIFIED IDEOGRAPH-5D92: not included in any glyphset definition</li>
<li>U+5D93 CJK UNIFIED IDEOGRAPH-5D93: not included in any glyphset definition</li>
<li>U+5D9F CJK UNIFIED IDEOGRAPH-5D9F: not included in any glyphset definition</li>
<li>U+5DA6 CJK UNIFIED IDEOGRAPH-5DA6: not included in any glyphset definition</li>
<li>U+5DA8 CJK UNIFIED IDEOGRAPH-5DA8: not included in any glyphset definition</li>
<li>U+5DAA CJK UNIFIED IDEOGRAPH-5DAA: not included in any glyphset definition</li>
<li>U+5DB2 CJK UNIFIED IDEOGRAPH-5DB2: not included in any glyphset definition</li>
<li>U+5DB4 CJK UNIFIED IDEOGRAPH-5DB4: not included in any glyphset definition</li>
<li>U+5DC7 CJK UNIFIED IDEOGRAPH-5DC7: not included in any glyphset definition</li>
<li>U+5DCB CJK UNIFIED IDEOGRAPH-5DCB: not included in any glyphset definition</li>
<li>U+5DD0 CJK UNIFIED IDEOGRAPH-5DD0: not included in any glyphset definition</li>
<li>U+5DD8 CJK UNIFIED IDEOGRAPH-5DD8: not included in any glyphset definition</li>
<li>U+5DEA CJK UNIFIED IDEOGRAPH-5DEA: not included in any glyphset definition</li>
<li>U+5DF0 CJK UNIFIED IDEOGRAPH-5DF0: not included in any glyphset definition</li>
<li>U+5E1F CJK UNIFIED IDEOGRAPH-5E1F: not included in any glyphset definition</li>
<li>U+5E21 CJK UNIFIED IDEOGRAPH-5E21: not included in any glyphset definition</li>
<li>U+5E28 CJK UNIFIED IDEOGRAPH-5E28: not included in any glyphset definition</li>
<li>U+5E31 CJK UNIFIED IDEOGRAPH-5E31: not included in any glyphset definition</li>
<li>U+5E3B CJK UNIFIED IDEOGRAPH-5E3B: not included in any glyphset definition</li>
<li>U+5E3F CJK UNIFIED IDEOGRAPH-5E3F: not included in any glyphset definition</li>
<li>U+5E56 CJK UNIFIED IDEOGRAPH-5E56: not included in any glyphset definition</li>
<li>U+5E58 CJK UNIFIED IDEOGRAPH-5E58: not included in any glyphset definition</li>
<li>U+5E5B CJK UNIFIED IDEOGRAPH-5E5B: not included in any glyphset definition</li>
<li>U+5E5E CJK UNIFIED IDEOGRAPH-5E5E: not included in any glyphset definition</li>
<li>U+5E6C CJK UNIFIED IDEOGRAPH-5E6C: not included in any glyphset definition</li>
<li>U+5E77 CJK UNIFIED IDEOGRAPH-5E77: not included in any glyphset definition</li>
<li>U+5E80 CJK UNIFIED IDEOGRAPH-5E80: not included in any glyphset definition</li>
<li>U+5E8B CJK UNIFIED IDEOGRAPH-5E8B: not included in any glyphset definition</li>
<li>U+5EA4 CJK UNIFIED IDEOGRAPH-5EA4: not included in any glyphset definition</li>
<li>U+5EA5 CJK UNIFIED IDEOGRAPH-5EA5: not included in any glyphset definition</li>
<li>U+5EB1 CJK UNIFIED IDEOGRAPH-5EB1: not included in any glyphset definition</li>
<li>U+5EB3 CJK UNIFIED IDEOGRAPH-5EB3: not included in any glyphset definition</li>
<li>U+5EBC CJK UNIFIED IDEOGRAPH-5EBC: not included in any glyphset definition</li>
<li>U+5EC6 CJK UNIFIED IDEOGRAPH-5EC6: not included in any glyphset definition</li>
<li>U+5ECD CJK UNIFIED IDEOGRAPH-5ECD: not included in any glyphset definition</li>
<li>U+5ECE CJK UNIFIED IDEOGRAPH-5ECE: not included in any glyphset definition</li>
<li>U+5ED1 CJK UNIFIED IDEOGRAPH-5ED1: not included in any glyphset definition</li>
<li>U+5ED2 CJK UNIFIED IDEOGRAPH-5ED2: not included in any glyphset definition</li>
<li>U+5ED9 CJK UNIFIED IDEOGRAPH-5ED9: not included in any glyphset definition</li>
<li>U+5EDE CJK UNIFIED IDEOGRAPH-5EDE: not included in any glyphset definition</li>
<li>U+5F06 CJK UNIFIED IDEOGRAPH-5F06: not included in any glyphset definition</li>
<li>U+5F07 CJK UNIFIED IDEOGRAPH-5F07: not included in any glyphset definition</li>
<li>U+5F21 CJK UNIFIED IDEOGRAPH-5F21: not included in any glyphset definition</li>
<li>U+5F28 CJK UNIFIED IDEOGRAPH-5F28: not included in any glyphset definition</li>
<li>U+5F2A CJK UNIFIED IDEOGRAPH-5F2A: not included in any glyphset definition</li>
<li>U+5F33 CJK UNIFIED IDEOGRAPH-5F33: not included in any glyphset definition</li>
<li>U+5F34 CJK UNIFIED IDEOGRAPH-5F34: not included in any glyphset definition</li>
<li>U+5F36 CJK UNIFIED IDEOGRAPH-5F36: not included in any glyphset definition</li>
<li>U+5F44 CJK UNIFIED IDEOGRAPH-5F44: not included in any glyphset definition</li>
<li>U+5F45 CJK UNIFIED IDEOGRAPH-5F45: not included in any glyphset definition</li>
<li>U+5F50 CJK UNIFIED IDEOGRAPH-5F50: not included in any glyphset definition</li>
<li>U+5F54 CJK UNIFIED IDEOGRAPH-5F54: not included in any glyphset definition</li>
<li>U+5F5B CJK UNIFIED IDEOGRAPH-5F5B: not included in any glyphset definition</li>
<li>U+5F5E CJK UNIFIED IDEOGRAPH-5F5E: not included in any glyphset definition</li>
<li>U+5F5F CJK UNIFIED IDEOGRAPH-5F5F: not included in any glyphset definition</li>
<li>U+5F60 CJK UNIFIED IDEOGRAPH-5F60: not included in any glyphset definition</li>
<li>U+5F63 CJK UNIFIED IDEOGRAPH-5F63: not included in any glyphset definition</li>
<li>U+5F9B CJK UNIFIED IDEOGRAPH-5F9B: not included in any glyphset definition</li>
<li>U+5FA7 CJK UNIFIED IDEOGRAPH-5FA7: not included in any glyphset definition</li>
<li>U+5FAB CJK UNIFIED IDEOGRAPH-5FAB: not included in any glyphset definition</li>
<li>U+5FC9 CJK UNIFIED IDEOGRAPH-5FC9: not included in any glyphset definition</li>
<li>U+5FDE CJK UNIFIED IDEOGRAPH-5FDE: not included in any glyphset definition</li>
<li>U+5FDF CJK UNIFIED IDEOGRAPH-5FDF: not included in any glyphset definition</li>
<li>U+5FED CJK UNIFIED IDEOGRAPH-5FED: not included in any glyphset definition</li>
<li>U+5FEE CJK UNIFIED IDEOGRAPH-5FEE: not included in any glyphset definition</li>
<li>U+5FF3 CJK UNIFIED IDEOGRAPH-5FF3: not included in any glyphset definition</li>
<li>U+5FFA CJK UNIFIED IDEOGRAPH-5FFA: not included in any glyphset definition</li>
<li>U+5FFC CJK UNIFIED IDEOGRAPH-5FFC: not included in any glyphset definition</li>
<li>U+6003 CJK UNIFIED IDEOGRAPH-6003: not included in any glyphset definition</li>
<li>U+600A CJK UNIFIED IDEOGRAPH-600A: not included in any glyphset definition</li>
<li>U+600D CJK UNIFIED IDEOGRAPH-600D: not included in any glyphset definition</li>
<li>U+6053 CJK UNIFIED IDEOGRAPH-6053: not included in any glyphset definition</li>
<li>U+6054 CJK UNIFIED IDEOGRAPH-6054: not included in any glyphset definition</li>
<li>U+605D CJK UNIFIED IDEOGRAPH-605D: not included in any glyphset definition</li>
<li>U+6067 CJK UNIFIED IDEOGRAPH-6067: not included in any glyphset definition</li>
<li>U+6079 CJK UNIFIED IDEOGRAPH-6079: not included in any glyphset definition</li>
<li>U+6086 CJK UNIFIED IDEOGRAPH-6086: not included in any glyphset definition</li>
<li>U+6088 CJK UNIFIED IDEOGRAPH-6088: not included in any glyphset definition</li>
<li>U+609D CJK UNIFIED IDEOGRAPH-609D: not included in any glyphset definition</li>
<li>U+60A2 CJK UNIFIED IDEOGRAPH-60A2: not included in any glyphset definition</li>
<li>U+60AB CJK UNIFIED IDEOGRAPH-60AB: not included in any glyphset definition</li>
<li>U+60B0 CJK UNIFIED IDEOGRAPH-60B0: not included in any glyphset definition</li>
<li>U+60CE CJK UNIFIED IDEOGRAPH-60CE: not included in any glyphset definition</li>
<li>U+60D4 CJK UNIFIED IDEOGRAPH-60D4: not included in any glyphset definition</li>
<li>U+60D9 CJK UNIFIED IDEOGRAPH-60D9: not included in any glyphset definition</li>
<li>U+60DB CJK UNIFIED IDEOGRAPH-60DB: not included in any glyphset definition</li>
<li>U+60DD CJK UNIFIED IDEOGRAPH-60DD: not included in any glyphset definition</li>
<li>U+6110 CJK UNIFIED IDEOGRAPH-6110: not included in any glyphset definition</li>
<li>U+6111 CJK UNIFIED IDEOGRAPH-6111: not included in any glyphset definition</li>
<li>U+6112 CJK UNIFIED IDEOGRAPH-6112: not included in any glyphset definition</li>
<li>U+6113 CJK UNIFIED IDEOGRAPH-6113: not included in any glyphset definition</li>
<li>U+6114 CJK UNIFIED IDEOGRAPH-6114: not included in any glyphset definition</li>
<li>U+6116 CJK UNIFIED IDEOGRAPH-6116: not included in any glyphset definition</li>
<li>U+6126 CJK UNIFIED IDEOGRAPH-6126: not included in any glyphset definition</li>
<li>U+6130 CJK UNIFIED IDEOGRAPH-6130: not included in any glyphset definition</li>
<li>U+6146 CJK UNIFIED IDEOGRAPH-6146: not included in any glyphset definition</li>
<li>U+6164 CJK UNIFIED IDEOGRAPH-6164: not included in any glyphset definition</li>
<li>U+616A CJK UNIFIED IDEOGRAPH-616A: not included in any glyphset definition</li>
<li>U+616C CJK UNIFIED IDEOGRAPH-616C: not included in any glyphset definition</li>
<li>U+616D CJK UNIFIED IDEOGRAPH-616D: not included in any glyphset definition</li>
<li>U+617C CJK UNIFIED IDEOGRAPH-617C: not included in any glyphset definition</li>
<li>U+6192 CJK UNIFIED IDEOGRAPH-6192: not included in any glyphset definition</li>
<li>U+619D CJK UNIFIED IDEOGRAPH-619D: not included in any glyphset definition</li>
<li>U+61AD CJK UNIFIED IDEOGRAPH-61AD: not included in any glyphset definition</li>
<li>U+61D4 CJK UNIFIED IDEOGRAPH-61D4: not included in any glyphset definition</li>
<li>U+61DE CJK UNIFIED IDEOGRAPH-61DE: not included in any glyphset definition</li>
<li>U+6206 CJK UNIFIED IDEOGRAPH-6206: not included in any glyphset definition</li>
<li>U+620B CJK UNIFIED IDEOGRAPH-620B: not included in any glyphset definition</li>
<li>U+6213 CJK UNIFIED IDEOGRAPH-6213: not included in any glyphset definition</li>
<li>U+6217 CJK UNIFIED IDEOGRAPH-6217: not included in any glyphset definition</li>
<li>U+6224 CJK UNIFIED IDEOGRAPH-6224: not included in any glyphset definition</li>
<li>U+6227 CJK UNIFIED IDEOGRAPH-6227: not included in any glyphset definition</li>
<li>U+622D CJK UNIFIED IDEOGRAPH-622D: not included in any glyphset definition</li>
<li>U+6231 CJK UNIFIED IDEOGRAPH-6231: not included in any glyphset definition</li>
<li>U+6242 CJK UNIFIED IDEOGRAPH-6242: not included in any glyphset definition</li>
<li>U+6243 CJK UNIFIED IDEOGRAPH-6243: not included in any glyphset definition</li>
<li>U+6245 CJK UNIFIED IDEOGRAPH-6245: not included in any glyphset definition</li>
<li>U+6246 CJK UNIFIED IDEOGRAPH-6246: not included in any glyphset definition</li>
<li>U+624A CJK UNIFIED IDEOGRAPH-624A: not included in any glyphset definition</li>
<li>U+6259 CJK UNIFIED IDEOGRAPH-6259: not included in any glyphset definition</li>
<li>U+627D CJK UNIFIED IDEOGRAPH-627D: not included in any glyphset definition</li>
<li>U+6286 CJK UNIFIED IDEOGRAPH-6286: not included in any glyphset definition</li>
<li>U+62A6 CJK UNIFIED IDEOGRAPH-62A6: not included in any glyphset definition</li>
<li>U+62AE CJK UNIFIED IDEOGRAPH-62AE: not included in any glyphset definition</li>
<li>U+62E4 CJK UNIFIED IDEOGRAPH-62E4: not included in any glyphset definition</li>
<li>U+6322 CJK UNIFIED IDEOGRAPH-6322: not included in any glyphset definition</li>
<li>U+6326 CJK UNIFIED IDEOGRAPH-6326: not included in any glyphset definition</li>
<li>U+6335 CJK UNIFIED IDEOGRAPH-6335: not included in any glyphset definition</li>
<li>U+633B CJK UNIFIED IDEOGRAPH-633B: not included in any glyphset definition</li>
<li>U+6343 CJK UNIFIED IDEOGRAPH-6343: not included in any glyphset definition</li>
<li>U+638A CJK UNIFIED IDEOGRAPH-638A: not included in any glyphset definition</li>
<li>U+639E CJK UNIFIED IDEOGRAPH-639E: not included in any glyphset definition</li>
<li>U+63AD CJK UNIFIED IDEOGRAPH-63AD: not included in any glyphset definition</li>
<li>U+63AF CJK UNIFIED IDEOGRAPH-63AF: not included in any glyphset definition</li>
<li>U+63B9 CJK UNIFIED IDEOGRAPH-63B9: not included in any glyphset definition</li>
<li>U+63CE CJK UNIFIED IDEOGRAPH-63CE: not included in any glyphset definition</li>
<li>U+63D5 CJK UNIFIED IDEOGRAPH-63D5: not included in any glyphset definition</li>
<li>U+63DE CJK UNIFIED IDEOGRAPH-63DE: not included in any glyphset definition</li>
<li>U+63E6 CJK UNIFIED IDEOGRAPH-63E6: not included in any glyphset definition</li>
<li>U+63F2 CJK UNIFIED IDEOGRAPH-63F2: not included in any glyphset definition</li>
<li>U+63F3 CJK UNIFIED IDEOGRAPH-63F3: not included in any glyphset definition</li>
<li>U+63F5 CJK UNIFIED IDEOGRAPH-63F5: not included in any glyphset definition</li>
<li>U+63F7 CJK UNIFIED IDEOGRAPH-63F7: not included in any glyphset definition</li>
<li>U+63FC CJK UNIFIED IDEOGRAPH-63FC: not included in any glyphset definition</li>
<li>U+63FE CJK UNIFIED IDEOGRAPH-63FE: not included in any glyphset definition</li>
<li>U+63FF CJK UNIFIED IDEOGRAPH-63FF: not included in any glyphset definition</li>
<li>U+640B CJK UNIFIED IDEOGRAPH-640B: not included in any glyphset definition</li>
<li>U+640C CJK UNIFIED IDEOGRAPH-640C: not included in any glyphset definition</li>
<li>U+6412 CJK UNIFIED IDEOGRAPH-6412: not included in any glyphset definition</li>
<li>U+641B CJK UNIFIED IDEOGRAPH-641B: not included in any glyphset definition</li>
<li>U+6420 CJK UNIFIED IDEOGRAPH-6420: not included in any glyphset definition</li>
<li>U+6422 CJK UNIFIED IDEOGRAPH-6422: not included in any glyphset definition</li>
<li>U+643F CJK UNIFIED IDEOGRAPH-643F: not included in any glyphset definition</li>
<li>U+6445 CJK UNIFIED IDEOGRAPH-6445: not included in any glyphset definition</li>
<li>U+644F CJK UNIFIED IDEOGRAPH-644F: not included in any glyphset definition</li>
<li>U+645B CJK UNIFIED IDEOGRAPH-645B: not included in any glyphset definition</li>
<li>U+6460 CJK UNIFIED IDEOGRAPH-6460: not included in any glyphset definition</li>
<li>U+646D CJK UNIFIED IDEOGRAPH-646D: not included in any glyphset definition</li>
<li>U+6474 CJK UNIFIED IDEOGRAPH-6474: not included in any glyphset definition</li>
<li>U+6475 CJK UNIFIED IDEOGRAPH-6475: not included in any glyphset definition</li>
<li>U+647D CJK UNIFIED IDEOGRAPH-647D: not included in any glyphset definition</li>
<li>U+6484 CJK UNIFIED IDEOGRAPH-6484: not included in any glyphset definition</li>
<li>U+648F CJK UNIFIED IDEOGRAPH-648F: not included in any glyphset definition</li>
<li>U+6496 CJK UNIFIED IDEOGRAPH-6496: not included in any glyphset definition</li>
<li>U+649D CJK UNIFIED IDEOGRAPH-649D: not included in any glyphset definition</li>
<li>U+649F CJK UNIFIED IDEOGRAPH-649F: not included in any glyphset definition</li>
<li>U+64D0 CJK UNIFIED IDEOGRAPH-64D0: not included in any glyphset definition</li>
<li>U+64D7 CJK UNIFIED IDEOGRAPH-64D7: not included in any glyphset definition</li>
<li>U+64ED CJK UNIFIED IDEOGRAPH-64ED: not included in any glyphset definition</li>
<li>U+64FF CJK UNIFIED IDEOGRAPH-64FF: not included in any glyphset definition</li>
<li>U+6504 CJK UNIFIED IDEOGRAPH-6504: not included in any glyphset definition</li>
<li>U+6509 CJK UNIFIED IDEOGRAPH-6509: not included in any glyphset definition</li>
<li>U+6516 CJK UNIFIED IDEOGRAPH-6516: not included in any glyphset definition</li>
<li>U+651B CJK UNIFIED IDEOGRAPH-651B: not included in any glyphset definition</li>
<li>U+652E CJK UNIFIED IDEOGRAPH-652E: not included in any glyphset definition</li>
<li>U+6530 CJK UNIFIED IDEOGRAPH-6530: not included in any glyphset definition</li>
<li>U+653D CJK UNIFIED IDEOGRAPH-653D: not included in any glyphset definition</li>
<li>U+6543 CJK UNIFIED IDEOGRAPH-6543: not included in any glyphset definition</li>
<li>U+6549 CJK UNIFIED IDEOGRAPH-6549: not included in any glyphset definition</li>
<li>U+654E CJK UNIFIED IDEOGRAPH-654E: not included in any glyphset definition</li>
<li>U+6554 CJK UNIFIED IDEOGRAPH-6554: not included in any glyphset definition</li>
<li>U+6569 CJK UNIFIED IDEOGRAPH-6569: not included in any glyphset definition</li>
<li>U+656B CJK UNIFIED IDEOGRAPH-656B: not included in any glyphset definition</li>
<li>U+656D CJK UNIFIED IDEOGRAPH-656D: not included in any glyphset definition</li>
<li>U+657B CJK UNIFIED IDEOGRAPH-657B: not included in any glyphset definition</li>
<li>U+657E CJK UNIFIED IDEOGRAPH-657E: not included in any glyphset definition</li>
<li>U+6586 CJK UNIFIED IDEOGRAPH-6586: not included in any glyphset definition</li>
<li>U+659D CJK UNIFIED IDEOGRAPH-659D: not included in any glyphset definition</li>
<li>U+65A0 CJK UNIFIED IDEOGRAPH-65A0: not included in any glyphset definition</li>
<li>U+65B2 CJK UNIFIED IDEOGRAPH-65B2: not included in any glyphset definition</li>
<li>U+65B6 CJK UNIFIED IDEOGRAPH-65B6: not included in any glyphset definition</li>
<li>U+65D0 CJK UNIFIED IDEOGRAPH-65D0: not included in any glyphset definition</li>
<li>U+65DE CJK UNIFIED IDEOGRAPH-65DE: not included in any glyphset definition</li>
<li>U+65E3 CJK UNIFIED IDEOGRAPH-65E3: not included in any glyphset definition</li>
<li>U+65F0 CJK UNIFIED IDEOGRAPH-65F0: not included in any glyphset definition</li>
<li>U+65F2 CJK UNIFIED IDEOGRAPH-65F2: not included in any glyphset definition</li>
<li>U+65F4 CJK UNIFIED IDEOGRAPH-65F4: not included in any glyphset definition</li>
<li>U+65F5 CJK UNIFIED IDEOGRAPH-65F5: not included in any glyphset definition</li>
<li>U+65FD CJK UNIFIED IDEOGRAPH-65FD: not included in any glyphset definition</li>
<li>U+6604 CJK UNIFIED IDEOGRAPH-6604: not included in any glyphset definition</li>
<li>U+6608 CJK UNIFIED IDEOGRAPH-6608: not included in any glyphset definition</li>
<li>U+6610 CJK UNIFIED IDEOGRAPH-6610: not included in any glyphset definition</li>
<li>U+6611 CJK UNIFIED IDEOGRAPH-6611: not included in any glyphset definition</li>
<li>U+6612 CJK UNIFIED IDEOGRAPH-6612: not included in any glyphset definition</li>
<li>U+661E CJK UNIFIED IDEOGRAPH-661E: not included in any glyphset definition</li>
<li>U+6621 CJK UNIFIED IDEOGRAPH-6621: not included in any glyphset definition</li>
<li>U+6624 CJK UNIFIED IDEOGRAPH-6624: not included in any glyphset definition</li>
<li>U+662A CJK UNIFIED IDEOGRAPH-662A: not included in any glyphset definition</li>
<li>U+662B CJK UNIFIED IDEOGRAPH-662B: not included in any glyphset definition</li>
<li>U+662E CJK UNIFIED IDEOGRAPH-662E: not included in any glyphset definition</li>
<li>U+6633 CJK UNIFIED IDEOGRAPH-6633: not included in any glyphset definition</li>
<li>U+663B CJK UNIFIED IDEOGRAPH-663B: not included in any glyphset definition</li>
<li>U+663D CJK UNIFIED IDEOGRAPH-663D: not included in any glyphset definition</li>
<li>U+6645 CJK UNIFIED IDEOGRAPH-6645: not included in any glyphset definition</li>
<li>U+664A CJK UNIFIED IDEOGRAPH-664A: not included in any glyphset definition</li>
<li>U+6650 CJK UNIFIED IDEOGRAPH-6650: not included in any glyphset definition</li>
<li>U+6659 CJK UNIFIED IDEOGRAPH-6659: not included in any glyphset definition</li>
<li>U+665B CJK UNIFIED IDEOGRAPH-665B: not included in any glyphset definition</li>
<li>U+6661 CJK UNIFIED IDEOGRAPH-6661: not included in any glyphset definition</li>
<li>U+6665 CJK UNIFIED IDEOGRAPH-6665: not included in any glyphset definition</li>
<li>U+666A CJK UNIFIED IDEOGRAPH-666A: not included in any glyphset definition</li>
<li>U+666C CJK UNIFIED IDEOGRAPH-666C: not included in any glyphset definition</li>
<li>U+6671 CJK UNIFIED IDEOGRAPH-6671: not included in any glyphset definition</li>
<li>U+6673 CJK UNIFIED IDEOGRAPH-6673: not included in any glyphset definition</li>
<li>U+6678 CJK UNIFIED IDEOGRAPH-6678: not included in any glyphset definition</li>
<li>U+6679 CJK UNIFIED IDEOGRAPH-6679: not included in any glyphset definition</li>
<li>U+668B CJK UNIFIED IDEOGRAPH-668B: not included in any glyphset definition</li>
<li>U+668D CJK UNIFIED IDEOGRAPH-668D: not included in any glyphset definition</li>
<li>U+6695 CJK UNIFIED IDEOGRAPH-6695: not included in any glyphset definition</li>
<li>U+6699 CJK UNIFIED IDEOGRAPH-6699: not included in any glyphset definition</li>
<li>U+66A0 CJK UNIFIED IDEOGRAPH-66A0: not included in any glyphset definition</li>
<li>U+66AA CJK UNIFIED IDEOGRAPH-66AA: not included in any glyphset definition</li>
<li>U+66B2 CJK UNIFIED IDEOGRAPH-66B2: not included in any glyphset definition</li>
<li>U+66B3 CJK UNIFIED IDEOGRAPH-66B3: not included in any glyphset definition</li>
<li>U+66B5 CJK UNIFIED IDEOGRAPH-66B5: not included in any glyphset definition</li>
<li>U+66DB CJK UNIFIED IDEOGRAPH-66DB: not included in any glyphset definition</li>
<li>U+66E3 CJK UNIFIED IDEOGRAPH-66E3: not included in any glyphset definition</li>
<li>U+66E8 CJK UNIFIED IDEOGRAPH-66E8: not included in any glyphset definition</li>
<li>U+66F1 CJK UNIFIED IDEOGRAPH-66F1: not included in any glyphset definition</li>
<li>U+66FA CJK UNIFIED IDEOGRAPH-66FA: not included in any glyphset definition</li>
<li>U+66FB CJK UNIFIED IDEOGRAPH-66FB: not included in any glyphset definition</li>
<li>U+670A CJK UNIFIED IDEOGRAPH-670A: not included in any glyphset definition</li>
<li>U+6713 CJK UNIFIED IDEOGRAPH-6713: not included in any glyphset definition</li>
<li>U+6718 CJK UNIFIED IDEOGRAPH-6718: not included in any glyphset definition</li>
<li>U+6733 CJK UNIFIED IDEOGRAPH-6733: not included in any glyphset definition</li>
<li>U+674B CJK UNIFIED IDEOGRAPH-674B: not included in any glyphset definition</li>
<li>U+6755 CJK UNIFIED IDEOGRAPH-6755: not included in any glyphset definition</li>
<li>U+6757 CJK UNIFIED IDEOGRAPH-6757: not included in any glyphset definition</li>
<li>U+6766 CJK UNIFIED IDEOGRAPH-6766: not included in any glyphset definition</li>
<li>U+6767 CJK UNIFIED IDEOGRAPH-6767: not included in any glyphset definition</li>
<li>U+676E CJK UNIFIED IDEOGRAPH-676E: not included in any glyphset definition</li>
<li>U+6774 CJK UNIFIED IDEOGRAPH-6774: not included in any glyphset definition</li>
<li>U+677B CJK UNIFIED IDEOGRAPH-677B: not included in any glyphset definition</li>
<li>U+678D CJK UNIFIED IDEOGRAPH-678D: not included in any glyphset definition</li>
<li>U+678F CJK UNIFIED IDEOGRAPH-678F: not included in any glyphset definition</li>
<li>U+6798 CJK UNIFIED IDEOGRAPH-6798: not included in any glyphset definition</li>
<li>U+67A8 CJK UNIFIED IDEOGRAPH-67A8: not included in any glyphset definition</li>
<li>U+67B2 CJK UNIFIED IDEOGRAPH-67B2: not included in any glyphset definition</li>
<li>U+67B5 CJK UNIFIED IDEOGRAPH-67B5: not included in any glyphset definition</li>
<li>U+67BB CJK UNIFIED IDEOGRAPH-67BB: not included in any glyphset definition</li>
<li>U+67BE CJK UNIFIED IDEOGRAPH-67BE: not included in any glyphset definition</li>
<li>U+67C0 CJK UNIFIED IDEOGRAPH-67C0: not included in any glyphset definition</li>
<li>U+67C3 CJK UNIFIED IDEOGRAPH-67C3: not included in any glyphset definition</li>
<li>U+67C8 CJK UNIFIED IDEOGRAPH-67C8: not included in any glyphset definition</li>
<li>U+67F6 CJK UNIFIED IDEOGRAPH-67F6: not included in any glyphset definition</li>
<li>U+67F7 CJK UNIFIED IDEOGRAPH-67F7: not included in any glyphset definition</li>
<li>U+67FD CJK UNIFIED IDEOGRAPH-67FD: not included in any glyphset definition</li>
<li>U+6801 CJK UNIFIED IDEOGRAPH-6801: not included in any glyphset definition</li>
<li>U+680A CJK UNIFIED IDEOGRAPH-680A: not included in any glyphset definition</li>
<li>U+6812 CJK UNIFIED IDEOGRAPH-6812: not included in any glyphset definition</li>
<li>U+6818 CJK UNIFIED IDEOGRAPH-6818: not included in any glyphset definition</li>
<li>U+681D CJK UNIFIED IDEOGRAPH-681D: not included in any glyphset definition</li>
<li>U+681F CJK UNIFIED IDEOGRAPH-681F: not included in any glyphset definition</li>
<li>U+682F CJK UNIFIED IDEOGRAPH-682F: not included in any glyphset definition</li>
<li>U+6833 CJK UNIFIED IDEOGRAPH-6833: not included in any glyphset definition</li>
<li>U+683B CJK UNIFIED IDEOGRAPH-683B: not included in any glyphset definition</li>
<li>U+6844 CJK UNIFIED IDEOGRAPH-6844: not included in any glyphset definition</li>
<li>U+6852 CJK UNIFIED IDEOGRAPH-6852: not included in any glyphset definition</li>
<li>U+6864 CJK UNIFIED IDEOGRAPH-6864: not included in any glyphset definition</li>
<li>U+686B CJK UNIFIED IDEOGRAPH-686B: not included in any glyphset definition</li>
<li>U+686D CJK UNIFIED IDEOGRAPH-686D: not included in any glyphset definition</li>
<li>U+686F CJK UNIFIED IDEOGRAPH-686F: not included in any glyphset definition</li>
<li>U+6872 CJK UNIFIED IDEOGRAPH-6872: not included in any glyphset definition</li>
<li>U+6879 CJK UNIFIED IDEOGRAPH-6879: not included in any glyphset definition</li>
<li>U+6882 CJK UNIFIED IDEOGRAPH-6882: not included in any glyphset definition</li>
<li>U+6887 CJK UNIFIED IDEOGRAPH-6887: not included in any glyphset definition</li>
<li>U+688C CJK UNIFIED IDEOGRAPH-688C: not included in any glyphset definition</li>
<li>U+6898 CJK UNIFIED IDEOGRAPH-6898: not included in any glyphset definition</li>
<li>U+689C CJK UNIFIED IDEOGRAPH-689C: not included in any glyphset definition</li>
<li>U+68A1 CJK UNIFIED IDEOGRAPH-68A1: not included in any glyphset definition</li>
<li>U+68B2 CJK UNIFIED IDEOGRAPH-68B2: not included in any glyphset definition</li>
<li>U+68B4 CJK UNIFIED IDEOGRAPH-68B4: not included in any glyphset definition</li>
<li>U+68BE CJK UNIFIED IDEOGRAPH-68BE: not included in any glyphset definition</li>
<li>U+68BF CJK UNIFIED IDEOGRAPH-68BF: not included in any glyphset definition</li>
<li>U+68C8 CJK UNIFIED IDEOGRAPH-68C8: not included in any glyphset definition</li>
<li>U+68CF CJK UNIFIED IDEOGRAPH-68CF: not included in any glyphset definition</li>
<li>U+68D0 CJK UNIFIED IDEOGRAPH-68D0: not included in any glyphset definition</li>
<li>U+68D3 CJK UNIFIED IDEOGRAPH-68D3: not included in any glyphset definition</li>
<li>U+68D6 CJK UNIFIED IDEOGRAPH-68D6: not included in any glyphset definition</li>
<li>U+68E4 CJK UNIFIED IDEOGRAPH-68E4: not included in any glyphset definition</li>
<li>U+68EA CJK UNIFIED IDEOGRAPH-68EA: not included in any glyphset definition</li>
<li>U+68EB CJK UNIFIED IDEOGRAPH-68EB: not included in any glyphset definition</li>
<li>U+68F6 CJK UNIFIED IDEOGRAPH-68F6: not included in any glyphset definition</li>
<li>U+68FC CJK UNIFIED IDEOGRAPH-68FC: not included in any glyphset definition</li>
<li>U+68FD CJK UNIFIED IDEOGRAPH-68FD: not included in any glyphset definition</li>
<li>U+6906 CJK UNIFIED IDEOGRAPH-6906: not included in any glyphset definition</li>
<li>U+6910 CJK UNIFIED IDEOGRAPH-6910: not included in any glyphset definition</li>
<li>U+6911 CJK UNIFIED IDEOGRAPH-6911: not included in any glyphset definition</li>
<li>U+6913 CJK UNIFIED IDEOGRAPH-6913: not included in any glyphset definition</li>
<li>U+691F CJK UNIFIED IDEOGRAPH-691F: not included in any glyphset definition</li>
<li>U+6920 CJK UNIFIED IDEOGRAPH-6920: not included in any glyphset definition</li>
<li>U+6927 CJK UNIFIED IDEOGRAPH-6927: not included in any glyphset definition</li>
<li>U+6938 CJK UNIFIED IDEOGRAPH-6938: not included in any glyphset definition</li>
<li>U+6952 CJK UNIFIED IDEOGRAPH-6952: not included in any glyphset definition</li>
<li>U+6957 CJK UNIFIED IDEOGRAPH-6957: not included in any glyphset definition</li>
<li>U+695B CJK UNIFIED IDEOGRAPH-695B: not included in any glyphset definition</li>
<li>U+6969 CJK UNIFIED IDEOGRAPH-6969: not included in any glyphset definition</li>
<li>U+696C CJK UNIFIED IDEOGRAPH-696C: not included in any glyphset definition</li>
<li>U+6971 CJK UNIFIED IDEOGRAPH-6971: not included in any glyphset definition</li>
<li>U+6980 CJK UNIFIED IDEOGRAPH-6980: not included in any glyphset definition</li>
<li>U+6983 CJK UNIFIED IDEOGRAPH-6983: not included in any glyphset definition</li>
<li>U+6985 CJK UNIFIED IDEOGRAPH-6985: not included in any glyphset definition</li>
<li>U+6987 CJK UNIFIED IDEOGRAPH-6987: not included in any glyphset definition</li>
<li>U+698D CJK UNIFIED IDEOGRAPH-698D: not included in any glyphset definition</li>
<li>U+6998 CJK UNIFIED IDEOGRAPH-6998: not included in any glyphset definition</li>
<li>U+69A3 CJK UNIFIED IDEOGRAPH-69A3: not included in any glyphset definition</li>
<li>U+69A5 CJK UNIFIED IDEOGRAPH-69A5: not included in any glyphset definition</li>
<li>U+69AA CJK UNIFIED IDEOGRAPH-69AA: not included in any glyphset definition</li>
<li>U+69B0 CJK UNIFIED IDEOGRAPH-69B0: not included in any glyphset definition</li>
<li>U+69D4 CJK UNIFIED IDEOGRAPH-69D4: not included in any glyphset definition</li>
<li>U+69DA CJK UNIFIED IDEOGRAPH-69DA: not included in any glyphset definition</li>
<li>U+69DC CJK UNIFIED IDEOGRAPH-69DC: not included in any glyphset definition</li>
<li>U+69E0 CJK UNIFIED IDEOGRAPH-69E0: not included in any glyphset definition</li>
<li>U+69E2 CJK UNIFIED IDEOGRAPH-69E2: not included in any glyphset definition</li>
<li>U+69EA CJK UNIFIED IDEOGRAPH-69EA: not included in any glyphset definition</li>
<li>U+69F1 CJK UNIFIED IDEOGRAPH-69F1: not included in any glyphset definition</li>
<li>U+6A30 CJK UNIFIED IDEOGRAPH-6A30: not included in any glyphset definition</li>
<li>U+6A46 CJK UNIFIED IDEOGRAPH-6A46: not included in any glyphset definition</li>
<li>U+6A50 CJK UNIFIED IDEOGRAPH-6A50: not included in any glyphset definition</li>
<li>U+6A51 CJK UNIFIED IDEOGRAPH-6A51: not included in any glyphset definition</li>
<li>U+6A52 CJK UNIFIED IDEOGRAPH-6A52: not included in any glyphset definition</li>
<li>U+6A5A CJK UNIFIED IDEOGRAPH-6A5A: not included in any glyphset definition</li>
<li>U+6A5B CJK UNIFIED IDEOGRAPH-6A5B: not included in any glyphset definition</li>
<li>U+6A5E CJK UNIFIED IDEOGRAPH-6A5E: not included in any glyphset definition</li>
<li>U+6A73 CJK UNIFIED IDEOGRAPH-6A73: not included in any glyphset definition</li>
<li>U+6A7D CJK UNIFIED IDEOGRAPH-6A7D: not included in any glyphset definition</li>
<li>U+6A81 CJK UNIFIED IDEOGRAPH-6A81: not included in any glyphset definition</li>
<li>U+6A87 CJK UNIFIED IDEOGRAPH-6A87: not included in any glyphset definition</li>
<li>U+6A91 CJK UNIFIED IDEOGRAPH-6A91: not included in any glyphset definition</li>
<li>U+6A9E CJK UNIFIED IDEOGRAPH-6A9E: not included in any glyphset definition</li>
<li>U+6A9F CJK UNIFIED IDEOGRAPH-6A9F: not included in any glyphset definition</li>
<li>U+6AB5 CJK UNIFIED IDEOGRAPH-6AB5: not included in any glyphset definition</li>
<li>U+6AC6 CJK UNIFIED IDEOGRAPH-6AC6: not included in any glyphset definition</li>
<li>U+6AC8 CJK UNIFIED IDEOGRAPH-6AC8: not included in any glyphset definition</li>
<li>U+6ACD CJK UNIFIED IDEOGRAPH-6ACD: not included in any glyphset definition</li>
<li>U+6ADD CJK UNIFIED IDEOGRAPH-6ADD: not included in any glyphset definition</li>
<li>U+6AE2 CJK UNIFIED IDEOGRAPH-6AE2: not included in any glyphset definition</li>
<li>U+6AE4 CJK UNIFIED IDEOGRAPH-6AE4: not included in any glyphset definition</li>
<li>U+6AE7 CJK UNIFIED IDEOGRAPH-6AE7: not included in any glyphset definition</li>
<li>U+6AEC CJK UNIFIED IDEOGRAPH-6AEC: not included in any glyphset definition</li>
<li>U+6AF1 CJK UNIFIED IDEOGRAPH-6AF1: not included in any glyphset definition</li>
<li>U+6B02 CJK UNIFIED IDEOGRAPH-6B02: not included in any glyphset definition</li>
<li>U+6B0C CJK UNIFIED IDEOGRAPH-6B0C: not included in any glyphset definition</li>
<li>U+6B13 CJK UNIFIED IDEOGRAPH-6B13: not included in any glyphset definition</li>
<li>U+6B17 CJK UNIFIED IDEOGRAPH-6B17: not included in any glyphset definition</li>
<li>U+6B1E CJK UNIFIED IDEOGRAPH-6B1E: not included in any glyphset definition</li>
<li>U+6B24 CJK UNIFIED IDEOGRAPH-6B24: not included in any glyphset definition</li>
<li>U+6B3B CJK UNIFIED IDEOGRAPH-6B3B: not included in any glyphset definition</li>
<li>U+6B45 CJK UNIFIED IDEOGRAPH-6B45: not included in any glyphset definition</li>
<li>U+6B5C CJK UNIFIED IDEOGRAPH-6B5C: not included in any glyphset definition</li>
<li>U+6B82 CJK UNIFIED IDEOGRAPH-6B82: not included in any glyphset definition</li>
<li>U+6B9B CJK UNIFIED IDEOGRAPH-6B9B: not included in any glyphset definition</li>
<li>U+6BA3 CJK UNIFIED IDEOGRAPH-6BA3: not included in any glyphset definition</li>
<li>U+6BCC CJK UNIFIED IDEOGRAPH-6BCC: not included in any glyphset definition</li>
<li>U+6BD0 CJK UNIFIED IDEOGRAPH-6BD0: not included in any glyphset definition</li>
<li>U+6BD1 CJK UNIFIED IDEOGRAPH-6BD1: not included in any glyphset definition</li>
<li>U+6BDA CJK UNIFIED IDEOGRAPH-6BDA: not included in any glyphset definition</li>
<li>U+6BF5 CJK UNIFIED IDEOGRAPH-6BF5: not included in any glyphset definition</li>
<li>U+6BF9 CJK UNIFIED IDEOGRAPH-6BF9: not included in any glyphset definition</li>
<li>U+6BFF CJK UNIFIED IDEOGRAPH-6BFF: not included in any glyphset definition</li>
<li>U+6C05 CJK UNIFIED IDEOGRAPH-6C05: not included in any glyphset definition</li>
<li>U+6C06 CJK UNIFIED IDEOGRAPH-6C06: not included in any glyphset definition</li>
<li>U+6C07 CJK UNIFIED IDEOGRAPH-6C07: not included in any glyphset definition</li>
<li>U+6C0A CJK UNIFIED IDEOGRAPH-6C0A: not included in any glyphset definition</li>
<li>U+6C0C CJK UNIFIED IDEOGRAPH-6C0C: not included in any glyphset definition</li>
<li>U+6C0D CJK UNIFIED IDEOGRAPH-6C0D: not included in any glyphset definition</li>
<li>U+6C15 CJK UNIFIED IDEOGRAPH-6C15: not included in any glyphset definition</li>
<li>U+6C1A CJK UNIFIED IDEOGRAPH-6C1A: not included in any glyphset definition</li>
<li>U+6C3F CJK UNIFIED IDEOGRAPH-6C3F: not included in any glyphset definition</li>
<li>U+6C48 CJK UNIFIED IDEOGRAPH-6C48: not included in any glyphset definition</li>
<li>U+6C4B CJK UNIFIED IDEOGRAPH-6C4B: not included in any glyphset definition</li>
<li>U+6C4D CJK UNIFIED IDEOGRAPH-6C4D: not included in any glyphset definition</li>
<li>U+6C54 CJK UNIFIED IDEOGRAPH-6C54: not included in any glyphset definition</li>
<li>U+6C67 CJK UNIFIED IDEOGRAPH-6C67: not included in any glyphset definition</li>
<li>U+6C6B CJK UNIFIED IDEOGRAPH-6C6B: not included in any glyphset definition</li>
<li>U+6C6D CJK UNIFIED IDEOGRAPH-6C6D: not included in any glyphset definition</li>
<li>U+6C6E CJK UNIFIED IDEOGRAPH-6C6E: not included in any glyphset definition</li>
<li>U+6C94 CJK UNIFIED IDEOGRAPH-6C94: not included in any glyphset definition</li>
<li>U+6C95 CJK UNIFIED IDEOGRAPH-6C95: not included in any glyphset definition</li>
<li>U+6C98 CJK UNIFIED IDEOGRAPH-6C98: not included in any glyphset definition</li>
<li>U+6CA8 CJK UNIFIED IDEOGRAPH-6CA8: not included in any glyphset definition</li>
<li>U+6CB2 CJK UNIFIED IDEOGRAPH-6CB2: not included in any glyphset definition</li>
<li>U+6CC2 CJK UNIFIED IDEOGRAPH-6CC2: not included in any glyphset definition</li>
<li>U+6CC3 CJK UNIFIED IDEOGRAPH-6CC3: not included in any glyphset definition</li>
<li>U+6CC7 CJK UNIFIED IDEOGRAPH-6CC7: not included in any glyphset definition</li>
<li>U+6CD0 CJK UNIFIED IDEOGRAPH-6CD0: not included in any glyphset definition</li>
<li>U+6CD6 CJK UNIFIED IDEOGRAPH-6CD6: not included in any glyphset definition</li>
<li>U+6CDA CJK UNIFIED IDEOGRAPH-6CDA: not included in any glyphset definition</li>
<li>U+6CDC CJK UNIFIED IDEOGRAPH-6CDC: not included in any glyphset definition</li>
<li>U+6CF6 CJK UNIFIED IDEOGRAPH-6CF6: not included in any glyphset definition</li>
<li>U+6D07 CJK UNIFIED IDEOGRAPH-6D07: not included in any glyphset definition</li>
<li>U+6D08 CJK UNIFIED IDEOGRAPH-6D08: not included in any glyphset definition</li>
<li>U+6D0E CJK UNIFIED IDEOGRAPH-6D0E: not included in any glyphset definition</li>
<li>U+6D11 CJK UNIFIED IDEOGRAPH-6D11: not included in any glyphset definition</li>
<li>U+6D13 CJK UNIFIED IDEOGRAPH-6D13: not included in any glyphset definition</li>
<li>U+6D18 CJK UNIFIED IDEOGRAPH-6D18: not included in any glyphset definition</li>
<li>U+6D1A CJK UNIFIED IDEOGRAPH-6D1A: not included in any glyphset definition</li>
<li>U+6D23 CJK UNIFIED IDEOGRAPH-6D23: not included in any glyphset definition</li>
<li>U+6D2D CJK UNIFIED IDEOGRAPH-6D2D: not included in any glyphset definition</li>
<li>U+6D34 CJK UNIFIED IDEOGRAPH-6D34: not included in any glyphset definition</li>
<li>U+6D4D CJK UNIFIED IDEOGRAPH-6D4D: not included in any glyphset definition</li>
<li>U+6D55 CJK UNIFIED IDEOGRAPH-6D55: not included in any glyphset definition</li>
<li>U+6D5E CJK UNIFIED IDEOGRAPH-6D5E: not included in any glyphset definition</li>
<li>U+6D5F CJK UNIFIED IDEOGRAPH-6D5F: not included in any glyphset definition</li>
<li>U+6D61 CJK UNIFIED IDEOGRAPH-6D61: not included in any glyphset definition</li>
<li>U+6D6D CJK UNIFIED IDEOGRAPH-6D6D: not included in any glyphset definition</li>
<li>U+6D70 CJK UNIFIED IDEOGRAPH-6D70: not included in any glyphset definition</li>
<li>U+6D72 CJK UNIFIED IDEOGRAPH-6D72: not included in any glyphset definition</li>
<li>U+6D84 CJK UNIFIED IDEOGRAPH-6D84: not included in any glyphset definition</li>
<li>U+6D8A CJK UNIFIED IDEOGRAPH-6D8A: not included in any glyphset definition</li>
<li>U+6D8D CJK UNIFIED IDEOGRAPH-6D8D: not included in any glyphset definition</li>
<li>U+6D8F CJK UNIFIED IDEOGRAPH-6D8F: not included in any glyphset definition</li>
<li>U+6D90 CJK UNIFIED IDEOGRAPH-6D90: not included in any glyphset definition</li>
<li>U+6D91 CJK UNIFIED IDEOGRAPH-6D91: not included in any glyphset definition</li>
<li>U+6DA2 CJK UNIFIED IDEOGRAPH-6DA2: not included in any glyphset definition</li>
<li>U+6DAB CJK UNIFIED IDEOGRAPH-6DAB: not included in any glyphset definition</li>
<li>U+6DAC CJK UNIFIED IDEOGRAPH-6DAC: not included in any glyphset definition</li>
<li>U+6DC3 CJK UNIFIED IDEOGRAPH-6DC3: not included in any glyphset definition</li>
<li>U+6DCD CJK UNIFIED IDEOGRAPH-6DCD: not included in any glyphset definition</li>
<li>U+6DDC CJK UNIFIED IDEOGRAPH-6DDC: not included in any glyphset definition</li>
<li>U+6DDF CJK UNIFIED IDEOGRAPH-6DDF: not included in any glyphset definition</li>
<li>U+6DE0 CJK UNIFIED IDEOGRAPH-6DE0: not included in any glyphset definition</li>
<li>U+6DF2 CJK UNIFIED IDEOGRAPH-6DF2: not included in any glyphset definition</li>
<li>U+6DF4 CJK UNIFIED IDEOGRAPH-6DF4: not included in any glyphset definition</li>
<li>U+6E16 CJK UNIFIED IDEOGRAPH-6E16: not included in any glyphset definition</li>
<li>U+6E22 CJK UNIFIED IDEOGRAPH-6E22: not included in any glyphset definition</li>
<li>U+6E27 CJK UNIFIED IDEOGRAPH-6E27: not included in any glyphset definition</li>
<li>U+6E30 CJK UNIFIED IDEOGRAPH-6E30: not included in any glyphset definition</li>
<li>U+6E3D CJK UNIFIED IDEOGRAPH-6E3D: not included in any glyphset definition</li>
<li>U+6E4B CJK UNIFIED IDEOGRAPH-6E4B: not included in any glyphset definition</li>
<li>U+6E53 CJK UNIFIED IDEOGRAPH-6E53: not included in any glyphset definition</li>
<li>U+6E54 CJK UNIFIED IDEOGRAPH-6E54: not included in any glyphset definition</li>
<li>U+6E5C CJK UNIFIED IDEOGRAPH-6E5C: not included in any glyphset definition</li>
<li>U+6E5D CJK UNIFIED IDEOGRAPH-6E5D: not included in any glyphset definition</li>
<li>U+6E5E CJK UNIFIED IDEOGRAPH-6E5E: not included in any glyphset definition</li>
<li>U+6E63 CJK UNIFIED IDEOGRAPH-6E63: not included in any glyphset definition</li>
<li>U+6E68 CJK UNIFIED IDEOGRAPH-6E68: not included in any glyphset definition</li>
<li>U+6E69 CJK UNIFIED IDEOGRAPH-6E69: not included in any glyphset definition</li>
<li>U+6E7A CJK UNIFIED IDEOGRAPH-6E7A: not included in any glyphset definition</li>
<li>U+6E81 CJK UNIFIED IDEOGRAPH-6E81: not included in any glyphset definition</li>
<li>U+6E87 CJK UNIFIED IDEOGRAPH-6E87: not included in any glyphset definition</li>
<li>U+6E88 CJK UNIFIED IDEOGRAPH-6E88: not included in any glyphset definition</li>
<li>U+6E8D CJK UNIFIED IDEOGRAPH-6E8D: not included in any glyphset definition</li>
<li>U+6E9A CJK UNIFIED IDEOGRAPH-6E9A: not included in any glyphset definition</li>
<li>U+6E9E CJK UNIFIED IDEOGRAPH-6E9E: not included in any glyphset definition</li>
<li>U+6EA0 CJK UNIFIED IDEOGRAPH-6EA0: not included in any glyphset definition</li>
<li>U+6EAE CJK UNIFIED IDEOGRAPH-6EAE: not included in any glyphset definition</li>
<li>U+6EB3 CJK UNIFIED IDEOGRAPH-6EB3: not included in any glyphset definition</li>
<li>U+6EB5 CJK UNIFIED IDEOGRAPH-6EB5: not included in any glyphset definition</li>
<li>U+6EB9 CJK UNIFIED IDEOGRAPH-6EB9: not included in any glyphset definition</li>
<li>U+6EBF CJK UNIFIED IDEOGRAPH-6EBF: not included in any glyphset definition</li>
<li>U+6ECD CJK UNIFIED IDEOGRAPH-6ECD: not included in any glyphset definition</li>
<li>U+6ECF CJK UNIFIED IDEOGRAPH-6ECF: not included in any glyphset definition</li>
<li>U+6ED7 CJK UNIFIED IDEOGRAPH-6ED7: not included in any glyphset definition</li>
<li>U+6EE0 CJK UNIFIED IDEOGRAPH-6EE0: not included in any glyphset definition</li>
<li>U+6EE7 CJK UNIFIED IDEOGRAPH-6EE7: not included in any glyphset definition</li>
<li>U+6EEA CJK UNIFIED IDEOGRAPH-6EEA: not included in any glyphset definition</li>
<li>U+6EEB CJK UNIFIED IDEOGRAPH-6EEB: not included in any glyphset definition</li>
<li>U+6EF9 CJK UNIFIED IDEOGRAPH-6EF9: not included in any glyphset definition</li>
<li>U+6EFB CJK UNIFIED IDEOGRAPH-6EFB: not included in any glyphset definition</li>
<li>U+6F08 CJK UNIFIED IDEOGRAPH-6F08: not included in any glyphset definition</li>
<li>U+6F0A CJK UNIFIED IDEOGRAPH-6F0A: not included in any glyphset definition</li>
<li>U+6F0D CJK UNIFIED IDEOGRAPH-6F0D: not included in any glyphset definition</li>
<li>U+6F26 CJK UNIFIED IDEOGRAPH-6F26: not included in any glyphset definition</li>
<li>U+6F27 CJK UNIFIED IDEOGRAPH-6F27: not included in any glyphset definition</li>
<li>U+6F2D CJK UNIFIED IDEOGRAPH-6F2D: not included in any glyphset definition</li>
<li>U+6F34 CJK UNIFIED IDEOGRAPH-6F34: not included in any glyphset definition</li>
<li>U+6F35 CJK UNIFIED IDEOGRAPH-6F35: not included in any glyphset definition</li>
<li>U+6F36 CJK UNIFIED IDEOGRAPH-6F36: not included in any glyphset definition</li>
<li>U+6F37 CJK UNIFIED IDEOGRAPH-6F37: not included in any glyphset definition</li>
<li>U+6F39 CJK UNIFIED IDEOGRAPH-6F39: not included in any glyphset definition</li>
<li>U+6F3B CJK UNIFIED IDEOGRAPH-6F3B: not included in any glyphset definition</li>
<li>U+6F3C CJK UNIFIED IDEOGRAPH-6F3C: not included in any glyphset definition</li>
<li>U+6F46 CJK UNIFIED IDEOGRAPH-6F46: not included in any glyphset definition</li>
<li>U+6F4F CJK UNIFIED IDEOGRAPH-6F4F: not included in any glyphset definition</li>
<li>U+6F55 CJK UNIFIED IDEOGRAPH-6F55: not included in any glyphset definition</li>
<li>U+6F57 CJK UNIFIED IDEOGRAPH-6F57: not included in any glyphset definition</li>
<li>U+6F59 CJK UNIFIED IDEOGRAPH-6F59: not included in any glyphset definition</li>
<li>U+6F5A CJK UNIFIED IDEOGRAPH-6F5A: not included in any glyphset definition</li>
<li>U+6F60 CJK UNIFIED IDEOGRAPH-6F60: not included in any glyphset definition</li>
<li>U+6F63 CJK UNIFIED IDEOGRAPH-6F63: not included in any glyphset definition</li>
<li>U+6F69 CJK UNIFIED IDEOGRAPH-6F69: not included in any glyphset definition</li>
<li>U+6F72 CJK UNIFIED IDEOGRAPH-6F72: not included in any glyphset definition</li>
<li>U+6F75 CJK UNIFIED IDEOGRAPH-6F75: not included in any glyphset definition</li>
<li>U+6F77 CJK UNIFIED IDEOGRAPH-6F77: not included in any glyphset definition</li>
<li>U+6F7D CJK UNIFIED IDEOGRAPH-6F7D: not included in any glyphset definition</li>
<li>U+6F7F CJK UNIFIED IDEOGRAPH-6F7F: not included in any glyphset definition</li>
<li>U+6F89 CJK UNIFIED IDEOGRAPH-6F89: not included in any glyphset definition</li>
<li>U+6F8C CJK UNIFIED IDEOGRAPH-6F8C: not included in any glyphset definition</li>
<li>U+6F9B CJK UNIFIED IDEOGRAPH-6F9B: not included in any glyphset definition</li>
<li>U+6FA5 CJK UNIFIED IDEOGRAPH-6FA5: not included in any glyphset definition</li>
<li>U+6FA6 CJK UNIFIED IDEOGRAPH-6FA6: not included in any glyphset definition</li>
<li>U+6FA9 CJK UNIFIED IDEOGRAPH-6FA9: not included in any glyphset definition</li>
<li>U+6FAB CJK UNIFIED IDEOGRAPH-6FAB: not included in any glyphset definition</li>
<li>U+6FAD CJK UNIFIED IDEOGRAPH-6FAD: not included in any glyphset definition</li>
<li>U+6FAE CJK UNIFIED IDEOGRAPH-6FAE: not included in any glyphset definition</li>
<li>U+6FAF CJK UNIFIED IDEOGRAPH-6FAF: not included in any glyphset definition</li>
<li>U+6FB4 CJK UNIFIED IDEOGRAPH-6FB4: not included in any glyphset definition</li>
<li>U+6FBC CJK UNIFIED IDEOGRAPH-6FBC: not included in any glyphset definition</li>
<li>U+6FBD CJK UNIFIED IDEOGRAPH-6FBD: not included in any glyphset definition</li>
<li>U+6FCA CJK UNIFIED IDEOGRAPH-6FCA: not included in any glyphset definition</li>
<li>U+6FDA CJK UNIFIED IDEOGRAPH-6FDA: not included in any glyphset definition</li>
<li>U+6FDC CJK UNIFIED IDEOGRAPH-6FDC: not included in any glyphset definition</li>
<li>U+6FE8 CJK UNIFIED IDEOGRAPH-6FE8: not included in any glyphset definition</li>
<li>U+6FE9 CJK UNIFIED IDEOGRAPH-6FE9: not included in any glyphset definition</li>
<li>U+6FF5 CJK UNIFIED IDEOGRAPH-6FF5: not included in any glyphset definition</li>
<li>U+6FFC CJK UNIFIED IDEOGRAPH-6FFC: not included in any glyphset definition</li>
<li>U+7002 CJK UNIFIED IDEOGRAPH-7002: not included in any glyphset definition</li>
<li>U+7007 CJK UNIFIED IDEOGRAPH-7007: not included in any glyphset definition</li>
<li>U+700C CJK UNIFIED IDEOGRAPH-700C: not included in any glyphset definition</li>
<li>U+700D CJK UNIFIED IDEOGRAPH-700D: not included in any glyphset definition</li>
<li>U+7014 CJK UNIFIED IDEOGRAPH-7014: not included in any glyphset definition</li>
<li>U+701C CJK UNIFIED IDEOGRAPH-701C: not included in any glyphset definition</li>
<li>U+7023 CJK UNIFIED IDEOGRAPH-7023: not included in any glyphset definition</li>
<li>U+702F CJK UNIFIED IDEOGRAPH-702F: not included in any glyphset definition</li>
<li>U+7031 CJK UNIFIED IDEOGRAPH-7031: not included in any glyphset definition</li>
<li>U+7037 CJK UNIFIED IDEOGRAPH-7037: not included in any glyphset definition</li>
<li>U+703C CJK UNIFIED IDEOGRAPH-703C: not included in any glyphset definition</li>
<li>U+7044 CJK UNIFIED IDEOGRAPH-7044: not included in any glyphset definition</li>
<li>U+7048 CJK UNIFIED IDEOGRAPH-7048: not included in any glyphset definition</li>
<li>U+7065 CJK UNIFIED IDEOGRAPH-7065: not included in any glyphset definition</li>
<li>U+7067 CJK UNIFIED IDEOGRAPH-7067: not included in any glyphset definition</li>
<li>U+708C CJK UNIFIED IDEOGRAPH-708C: not included in any glyphset definition</li>
<li>U+709A CJK UNIFIED IDEOGRAPH-709A: not included in any glyphset definition</li>
<li>U+709F CJK UNIFIED IDEOGRAPH-709F: not included in any glyphset definition</li>
<li>U+70A1 CJK UNIFIED IDEOGRAPH-70A1: not included in any glyphset definition</li>
<li>U+70B1 CJK UNIFIED IDEOGRAPH-70B1: not included in any glyphset definition</li>
<li>U+70BB CJK UNIFIED IDEOGRAPH-70BB: not included in any glyphset definition</li>
<li>U+70C0 CJK UNIFIED IDEOGRAPH-70C0: not included in any glyphset definition</li>
<li>U+70C7 CJK UNIFIED IDEOGRAPH-70C7: not included in any glyphset definition</li>
<li>U+70D3 CJK UNIFIED IDEOGRAPH-70D3: not included in any glyphset definition</li>
<li>U+70E0 CJK UNIFIED IDEOGRAPH-70E0: not included in any glyphset definition</li>
<li>U+70F6 CJK UNIFIED IDEOGRAPH-70F6: not included in any glyphset definition</li>
<li>U+70FA CJK UNIFIED IDEOGRAPH-70FA: not included in any glyphset definition</li>
<li>U+70FB CJK UNIFIED IDEOGRAPH-70FB: not included in any glyphset definition</li>
<li>U+7104 CJK UNIFIED IDEOGRAPH-7104: not included in any glyphset definition</li>
<li>U+7106 CJK UNIFIED IDEOGRAPH-7106: not included in any glyphset definition</li>
<li>U+710F CJK UNIFIED IDEOGRAPH-710F: not included in any glyphset definition</li>
<li>U+7110 CJK UNIFIED IDEOGRAPH-7110: not included in any glyphset definition</li>
<li>U+711E CJK UNIFIED IDEOGRAPH-711E: not included in any glyphset definition</li>
<li>U+713F CJK UNIFIED IDEOGRAPH-713F: not included in any glyphset definition</li>
<li>U+7141 CJK UNIFIED IDEOGRAPH-7141: not included in any glyphset definition</li>
<li>U+7143 CJK UNIFIED IDEOGRAPH-7143: not included in any glyphset definition</li>
<li>U+714B CJK UNIFIED IDEOGRAPH-714B: not included in any glyphset definition</li>
<li>U+7150 CJK UNIFIED IDEOGRAPH-7150: not included in any glyphset definition</li>
<li>U+7153 CJK UNIFIED IDEOGRAPH-7153: not included in any glyphset definition</li>
<li>U+715A CJK UNIFIED IDEOGRAPH-715A: not included in any glyphset definition</li>
<li>U+715F CJK UNIFIED IDEOGRAPH-715F: not included in any glyphset definition</li>
<li>U+7173 CJK UNIFIED IDEOGRAPH-7173: not included in any glyphset definition</li>
<li>U+717A CJK UNIFIED IDEOGRAPH-717A: not included in any glyphset definition</li>
<li>U+7180 CJK UNIFIED IDEOGRAPH-7180: not included in any glyphset definition</li>
<li>U+7185 CJK UNIFIED IDEOGRAPH-7185: not included in any glyphset definition</li>
<li>U+7187 CJK UNIFIED IDEOGRAPH-7187: not included in any glyphset definition</li>
<li>U+7189 CJK UNIFIED IDEOGRAPH-7189: not included in any glyphset definition</li>
<li>U+719B CJK UNIFIED IDEOGRAPH-719B: not included in any glyphset definition</li>
<li>U+719C CJK UNIFIED IDEOGRAPH-719C: not included in any glyphset definition</li>
<li>U+71A5 CJK UNIFIED IDEOGRAPH-71A5: not included in any glyphset definition</li>
<li>U+71B0 CJK UNIFIED IDEOGRAPH-71B0: not included in any glyphset definition</li>
<li>U+71B2 CJK UNIFIED IDEOGRAPH-71B2: not included in any glyphset definition</li>
<li>U+71B3 CJK UNIFIED IDEOGRAPH-71B3: not included in any glyphset definition</li>
<li>U+71C0 CJK UNIFIED IDEOGRAPH-71C0: not included in any glyphset definition</li>
<li>U+71CB CJK UNIFIED IDEOGRAPH-71CB: not included in any glyphset definition</li>
<li>U+71CF CJK UNIFIED IDEOGRAPH-71CF: not included in any glyphset definition</li>
<li>U+71D6 CJK UNIFIED IDEOGRAPH-71D6: not included in any glyphset definition</li>
<li>U+71F6 CJK UNIFIED IDEOGRAPH-71F6: not included in any glyphset definition</li>
<li>U+71F8 CJK UNIFIED IDEOGRAPH-71F8: not included in any glyphset definition</li>
<li>U+7200 CJK UNIFIED IDEOGRAPH-7200: not included in any glyphset definition</li>
<li>U+7207 CJK UNIFIED IDEOGRAPH-7207: not included in any glyphset definition</li>
<li>U+7214 CJK UNIFIED IDEOGRAPH-7214: not included in any glyphset definition</li>
<li>U+721A CJK UNIFIED IDEOGRAPH-721A: not included in any glyphset definition</li>
<li>U+721D CJK UNIFIED IDEOGRAPH-721D: not included in any glyphset definition</li>
<li>U+721F CJK UNIFIED IDEOGRAPH-721F: not included in any glyphset definition</li>
<li>U+7241 CJK UNIFIED IDEOGRAPH-7241: not included in any glyphset definition</li>
<li>U+7242 CJK UNIFIED IDEOGRAPH-7242: not included in any glyphset definition</li>
<li>U+7256 CJK UNIFIED IDEOGRAPH-7256: not included in any glyphset definition</li>
<li>U+725A CJK UNIFIED IDEOGRAPH-725A: not included in any glyphset definition</li>
<li>U+7264 CJK UNIFIED IDEOGRAPH-7264: not included in any glyphset definition</li>
<li>U+7265 CJK UNIFIED IDEOGRAPH-7265: not included in any glyphset definition</li>
<li>U+726E CJK UNIFIED IDEOGRAPH-726E: not included in any glyphset definition</li>
<li>U+727F CJK UNIFIED IDEOGRAPH-727F: not included in any glyphset definition</li>
<li>U+728B CJK UNIFIED IDEOGRAPH-728B: not included in any glyphset definition</li>
<li>U+72A1 CJK UNIFIED IDEOGRAPH-72A1: not included in any glyphset definition</li>
<li>U+72A8 CJK UNIFIED IDEOGRAPH-72A8: not included in any glyphset definition</li>
<li>U+72AD CJK UNIFIED IDEOGRAPH-72AD: not included in any glyphset definition</li>
<li>U+72B0 CJK UNIFIED IDEOGRAPH-72B0: not included in any glyphset definition</li>
<li>U+72B1 CJK UNIFIED IDEOGRAPH-72B1: not included in any glyphset definition</li>
<li>U+72B4 CJK UNIFIED IDEOGRAPH-72B4: not included in any glyphset definition</li>
<li>U+72BE CJK UNIFIED IDEOGRAPH-72BE: not included in any glyphset definition</li>
<li>U+72C1 CJK UNIFIED IDEOGRAPH-72C1: not included in any glyphset definition</li>
<li>U+72C9 CJK UNIFIED IDEOGRAPH-72C9: not included in any glyphset definition</li>
<li>U+72DD CJK UNIFIED IDEOGRAPH-72DD: not included in any glyphset definition</li>
<li>U+72E8 CJK UNIFIED IDEOGRAPH-72E8: not included in any glyphset definition</li>
<li>U+72EF CJK UNIFIED IDEOGRAPH-72EF: not included in any glyphset definition</li>
<li>U+72F3 CJK UNIFIED IDEOGRAPH-72F3: not included in any glyphset definition</li>
<li>U+72F4 CJK UNIFIED IDEOGRAPH-72F4: not included in any glyphset definition</li>
<li>U+72FA CJK UNIFIED IDEOGRAPH-72FA: not included in any glyphset definition</li>
<li>U+72FB CJK UNIFIED IDEOGRAPH-72FB: not included in any glyphset definition</li>
<li>U+7303 CJK UNIFIED IDEOGRAPH-7303: not included in any glyphset definition</li>
<li>U+7304 CJK UNIFIED IDEOGRAPH-7304: not included in any glyphset definition</li>
<li>U+7307 CJK UNIFIED IDEOGRAPH-7307: not included in any glyphset definition</li>
<li>U+7313 CJK UNIFIED IDEOGRAPH-7313: not included in any glyphset definition</li>
<li>U+7321 CJK UNIFIED IDEOGRAPH-7321: not included in any glyphset definition</li>
<li>U+7324 CJK UNIFIED IDEOGRAPH-7324: not included in any glyphset definition</li>
<li>U+7330 CJK UNIFIED IDEOGRAPH-7330: not included in any glyphset definition</li>
<li>U+7331 CJK UNIFIED IDEOGRAPH-7331: not included in any glyphset definition</li>
<li>U+733A CJK UNIFIED IDEOGRAPH-733A: not included in any glyphset definition</li>
<li>U+7341 CJK UNIFIED IDEOGRAPH-7341: not included in any glyphset definition</li>
<li>U+734D CJK UNIFIED IDEOGRAPH-734D: not included in any glyphset definition</li>
<li>U+7362 CJK UNIFIED IDEOGRAPH-7362: not included in any glyphset definition</li>
<li>U+7364 CJK UNIFIED IDEOGRAPH-7364: not included in any glyphset definition</li>
<li>U+736B CJK UNIFIED IDEOGRAPH-736B: not included in any glyphset definition</li>
<li>U+736C CJK UNIFIED IDEOGRAPH-736C: not included in any glyphset definition</li>
<li>U+736E CJK UNIFIED IDEOGRAPH-736E: not included in any glyphset definition</li>
<li>U+736F CJK UNIFIED IDEOGRAPH-736F: not included in any glyphset definition</li>
<li>U+7374 CJK UNIFIED IDEOGRAPH-7374: not included in any glyphset definition</li>
<li>U+7380 CJK UNIFIED IDEOGRAPH-7380: not included in any glyphset definition</li>
<li>U+7383 CJK UNIFIED IDEOGRAPH-7383: not included in any glyphset definition</li>
<li>U+738E CJK UNIFIED IDEOGRAPH-738E: not included in any glyphset definition</li>
<li>U+7392 CJK UNIFIED IDEOGRAPH-7392: not included in any glyphset definition</li>
<li>U+7394 CJK UNIFIED IDEOGRAPH-7394: not included in any glyphset definition</li>
<li>U+7395 CJK UNIFIED IDEOGRAPH-7395: not included in any glyphset definition</li>
<li>U+7398 CJK UNIFIED IDEOGRAPH-7398: not included in any glyphset definition</li>
<li>U+7399 CJK UNIFIED IDEOGRAPH-7399: not included in any glyphset definition</li>
<li>U+739A CJK UNIFIED IDEOGRAPH-739A: not included in any glyphset definition</li>
<li>U+73A1 CJK UNIFIED IDEOGRAPH-73A1: not included in any glyphset definition</li>
<li>U+73A2 CJK UNIFIED IDEOGRAPH-73A2: not included in any glyphset definition</li>
<li>U+73A4 CJK UNIFIED IDEOGRAPH-73A4: not included in any glyphset definition</li>
<li>U+73AD CJK UNIFIED IDEOGRAPH-73AD: not included in any glyphset definition</li>
<li>U+73B1 CJK UNIFIED IDEOGRAPH-73B1: not included in any glyphset definition</li>
<li>U+73B6 CJK UNIFIED IDEOGRAPH-73B6: not included in any glyphset definition</li>
<li>U+73BC CJK UNIFIED IDEOGRAPH-73BC: not included in any glyphset definition</li>
<li>U+73BD CJK UNIFIED IDEOGRAPH-73BD: not included in any glyphset definition</li>
<li>U+73BF CJK UNIFIED IDEOGRAPH-73BF: not included in any glyphset definition</li>
<li>U+73C7 CJK UNIFIED IDEOGRAPH-73C7: not included in any glyphset definition</li>
<li>U+73CB CJK UNIFIED IDEOGRAPH-73CB: not included in any glyphset definition</li>
<li>U+73CC CJK UNIFIED IDEOGRAPH-73CC: not included in any glyphset definition</li>
<li>U+73D2 CJK UNIFIED IDEOGRAPH-73D2: not included in any glyphset definition</li>
<li>U+73D6 CJK UNIFIED IDEOGRAPH-73D6: not included in any glyphset definition</li>
<li>U+73D7 CJK UNIFIED IDEOGRAPH-73D7: not included in any glyphset definition</li>
<li>U+73DB CJK UNIFIED IDEOGRAPH-73DB: not included in any glyphset definition</li>
<li>U+73DD CJK UNIFIED IDEOGRAPH-73DD: not included in any glyphset definition</li>
<li>U+73E6 CJK UNIFIED IDEOGRAPH-73E6: not included in any glyphset definition</li>
<li>U+73E7 CJK UNIFIED IDEOGRAPH-73E7: not included in any glyphset definition</li>
<li>U+73EB CJK UNIFIED IDEOGRAPH-73EB: not included in any glyphset definition</li>
<li>U+73F0 CJK UNIFIED IDEOGRAPH-73F0: not included in any glyphset definition</li>
<li>U+73F5 CJK UNIFIED IDEOGRAPH-73F5: not included in any glyphset definition</li>
<li>U+73F7 CJK UNIFIED IDEOGRAPH-73F7: not included in any glyphset definition</li>
<li>U+73F9 CJK UNIFIED IDEOGRAPH-73F9: not included in any glyphset definition</li>
<li>U+7400 CJK UNIFIED IDEOGRAPH-7400: not included in any glyphset definition</li>
<li>U+7408 CJK UNIFIED IDEOGRAPH-7408: not included in any glyphset definition</li>
<li>U+740E CJK UNIFIED IDEOGRAPH-740E: not included in any glyphset definition</li>
<li>U+7413 CJK UNIFIED IDEOGRAPH-7413: not included in any glyphset definition</li>
<li>U+7420 CJK UNIFIED IDEOGRAPH-7420: not included in any glyphset definition</li>
<li>U+7421 CJK UNIFIED IDEOGRAPH-7421: not included in any glyphset definition</li>
<li>U+7429 CJK UNIFIED IDEOGRAPH-7429: not included in any glyphset definition</li>
<li>U+742B CJK UNIFIED IDEOGRAPH-742B: not included in any glyphset definition</li>
<li>U+742D CJK UNIFIED IDEOGRAPH-742D: not included in any glyphset definition</li>
<li>U+7438 CJK UNIFIED IDEOGRAPH-7438: not included in any glyphset definition</li>
<li>U+7442 CJK UNIFIED IDEOGRAPH-7442: not included in any glyphset definition</li>
<li>U+7445 CJK UNIFIED IDEOGRAPH-7445: not included in any glyphset definition</li>
<li>U+7451 CJK UNIFIED IDEOGRAPH-7451: not included in any glyphset definition</li>
<li>U+7452 CJK UNIFIED IDEOGRAPH-7452: not included in any glyphset definition</li>
<li>U+7454 CJK UNIFIED IDEOGRAPH-7454: not included in any glyphset definition</li>
<li>U+745D CJK UNIFIED IDEOGRAPH-745D: not included in any glyphset definition</li>
<li>U+7465 CJK UNIFIED IDEOGRAPH-7465: not included in any glyphset definition</li>
<li>U+7468 CJK UNIFIED IDEOGRAPH-7468: not included in any glyphset definition</li>
<li>U+746C CJK UNIFIED IDEOGRAPH-746C: not included in any glyphset definition</li>
<li>U+7482 CJK UNIFIED IDEOGRAPH-7482: not included in any glyphset definition</li>
<li>U+7486 CJK UNIFIED IDEOGRAPH-7486: not included in any glyphset definition</li>
<li>U+7488 CJK UNIFIED IDEOGRAPH-7488: not included in any glyphset definition</li>
<li>U+748A CJK UNIFIED IDEOGRAPH-748A: not included in any glyphset definition</li>
<li>U+7492 CJK UNIFIED IDEOGRAPH-7492: not included in any glyphset definition</li>
<li>U+7495 CJK UNIFIED IDEOGRAPH-7495: not included in any glyphset definition</li>
<li>U+7497 CJK UNIFIED IDEOGRAPH-7497: not included in any glyphset definition</li>
<li>U+74A1 CJK UNIFIED IDEOGRAPH-74A1: not included in any glyphset definition</li>
<li>U+74A5 CJK UNIFIED IDEOGRAPH-74A5: not included in any glyphset definition</li>
<li>U+74AA CJK UNIFIED IDEOGRAPH-74AA: not included in any glyphset definition</li>
<li>U+74AB CJK UNIFIED IDEOGRAPH-74AB: not included in any glyphset definition</li>
<li>U+74AC CJK UNIFIED IDEOGRAPH-74AC: not included in any glyphset definition</li>
<li>U+74AE CJK UNIFIED IDEOGRAPH-74AE: not included in any glyphset definition</li>
<li>U+74B1 CJK UNIFIED IDEOGRAPH-74B1: not included in any glyphset definition</li>
<li>U+74B2 CJK UNIFIED IDEOGRAPH-74B2: not included in any glyphset definition</li>
<li>U+74B5 CJK UNIFIED IDEOGRAPH-74B5: not included in any glyphset definition</li>
<li>U+74B8 CJK UNIFIED IDEOGRAPH-74B8: not included in any glyphset definition</li>
<li>U+74C0 CJK UNIFIED IDEOGRAPH-74C0: not included in any glyphset definition</li>
<li>U+74C5 CJK UNIFIED IDEOGRAPH-74C5: not included in any glyphset definition</li>
<li>U+74C8 CJK UNIFIED IDEOGRAPH-74C8: not included in any glyphset definition</li>
<li>U+74D6 CJK UNIFIED IDEOGRAPH-74D6: not included in any glyphset definition</li>
<li>U+74D8 CJK UNIFIED IDEOGRAPH-74D8: not included in any glyphset definition</li>
<li>U+74DB CJK UNIFIED IDEOGRAPH-74DB: not included in any glyphset definition</li>
<li>U+74DE CJK UNIFIED IDEOGRAPH-74DE: not included in any glyphset definition</li>
<li>U+74FB CJK UNIFIED IDEOGRAPH-74FB: not included in any glyphset definition</li>
<li>U+74FF CJK UNIFIED IDEOGRAPH-74FF: not included in any glyphset definition</li>
<li>U+7501 CJK UNIFIED IDEOGRAPH-7501: not included in any glyphset definition</li>
<li>U+750F CJK UNIFIED IDEOGRAPH-750F: not included in any glyphset definition</li>
<li>U+7517 CJK UNIFIED IDEOGRAPH-7517: not included in any glyphset definition</li>
<li>U+751B CJK UNIFIED IDEOGRAPH-751B: not included in any glyphset definition</li>
<li>U+7534 CJK UNIFIED IDEOGRAPH-7534: not included in any glyphset definition</li>
<li>U+753D CJK UNIFIED IDEOGRAPH-753D: not included in any glyphset definition</li>
<li>U+754E CJK UNIFIED IDEOGRAPH-754E: not included in any glyphset definition</li>
<li>U+7556 CJK UNIFIED IDEOGRAPH-7556: not included in any glyphset definition</li>
<li>U+7575 CJK UNIFIED IDEOGRAPH-7575: not included in any glyphset definition</li>
<li>U+757A CJK UNIFIED IDEOGRAPH-757A: not included in any glyphset definition</li>
<li>U+7581 CJK UNIFIED IDEOGRAPH-7581: not included in any glyphset definition</li>
<li>U+758D CJK UNIFIED IDEOGRAPH-758D: not included in any glyphset definition</li>
<li>U+7590 CJK UNIFIED IDEOGRAPH-7590: not included in any glyphset definition</li>
<li>U+7592 CJK UNIFIED IDEOGRAPH-7592: not included in any glyphset definition</li>
<li>U+75A0 CJK UNIFIED IDEOGRAPH-75A0: not included in any glyphset definition</li>
<li>U+75A2 CJK UNIFIED IDEOGRAPH-75A2: not included in any glyphset definition</li>
<li>U+75AC CJK UNIFIED IDEOGRAPH-75AC: not included in any glyphset definition</li>
<li>U+75AD CJK UNIFIED IDEOGRAPH-75AD: not included in any glyphset definition</li>
<li>U+75B0 CJK UNIFIED IDEOGRAPH-75B0: not included in any glyphset definition</li>
<li>U+75C0 CJK UNIFIED IDEOGRAPH-75C0: not included in any glyphset definition</li>
<li>U+75C4 CJK UNIFIED IDEOGRAPH-75C4: not included in any glyphset definition</li>
<li>U+75D3 CJK UNIFIED IDEOGRAPH-75D3: not included in any glyphset definition</li>
<li>U+75D6 CJK UNIFIED IDEOGRAPH-75D6: not included in any glyphset definition</li>
<li>U+75E6 CJK UNIFIED IDEOGRAPH-75E6: not included in any glyphset definition</li>
<li>U+7602 CJK UNIFIED IDEOGRAPH-7602: not included in any glyphset definition</li>
<li>U+7603 CJK UNIFIED IDEOGRAPH-7603: not included in any glyphset definition</li>
<li>U+7605 CJK UNIFIED IDEOGRAPH-7605: not included in any glyphset definition</li>
<li>U+760C CJK UNIFIED IDEOGRAPH-760C: not included in any glyphset definition</li>
<li>U+7610 CJK UNIFIED IDEOGRAPH-7610: not included in any glyphset definition</li>
<li>U+7615 CJK UNIFIED IDEOGRAPH-7615: not included in any glyphset definition</li>
<li>U+7616 CJK UNIFIED IDEOGRAPH-7616: not included in any glyphset definition</li>
<li>U+7617 CJK UNIFIED IDEOGRAPH-7617: not included in any glyphset definition</li>
<li>U+761B CJK UNIFIED IDEOGRAPH-761B: not included in any glyphset definition</li>
<li>U+761D CJK UNIFIED IDEOGRAPH-761D: not included in any glyphset definition</li>
<li>U+761E CJK UNIFIED IDEOGRAPH-761E: not included in any glyphset definition</li>
<li>U+7625 CJK UNIFIED IDEOGRAPH-7625: not included in any glyphset definition</li>
<li>U+762D CJK UNIFIED IDEOGRAPH-762D: not included in any glyphset definition</li>
<li>U+762E CJK UNIFIED IDEOGRAPH-762E: not included in any glyphset definition</li>
<li>U+7632 CJK UNIFIED IDEOGRAPH-7632: not included in any glyphset definition</li>
<li>U+7633 CJK UNIFIED IDEOGRAPH-7633: not included in any glyphset definition</li>
<li>U+7635 CJK UNIFIED IDEOGRAPH-7635: not included in any glyphset definition</li>
<li>U+763C CJK UNIFIED IDEOGRAPH-763C: not included in any glyphset definition</li>
<li>U+7643 CJK UNIFIED IDEOGRAPH-7643: not included in any glyphset definition</li>
<li>U+7649 CJK UNIFIED IDEOGRAPH-7649: not included in any glyphset definition</li>
<li>U+764D CJK UNIFIED IDEOGRAPH-764D: not included in any glyphset definition</li>
<li>U+764E CJK UNIFIED IDEOGRAPH-764E: not included in any glyphset definition</li>
<li>U+7657 CJK UNIFIED IDEOGRAPH-7657: not included in any glyphset definition</li>
<li>U+7666 CJK UNIFIED IDEOGRAPH-7666: not included in any glyphset definition</li>
<li>U+766F CJK UNIFIED IDEOGRAPH-766F: not included in any glyphset definition</li>
<li>U+767F CJK UNIFIED IDEOGRAPH-767F: not included in any glyphset definition</li>
<li>U+7695 CJK UNIFIED IDEOGRAPH-7695: not included in any glyphset definition</li>
<li>U+769B CJK UNIFIED IDEOGRAPH-769B: not included in any glyphset definition</li>
<li>U+769C CJK UNIFIED IDEOGRAPH-769C: not included in any glyphset definition</li>
<li>U+769E CJK UNIFIED IDEOGRAPH-769E: not included in any glyphset definition</li>
<li>U+76A4 CJK UNIFIED IDEOGRAPH-76A4: not included in any glyphset definition</li>
<li>U+76A6 CJK UNIFIED IDEOGRAPH-76A6: not included in any glyphset definition</li>
<li>U+76AD CJK UNIFIED IDEOGRAPH-76AD: not included in any glyphset definition</li>
<li>U+76C9 CJK UNIFIED IDEOGRAPH-76C9: not included in any glyphset definition</li>
<li>U+76CC CJK UNIFIED IDEOGRAPH-76CC: not included in any glyphset definition</li>
<li>U+76E6 CJK UNIFIED IDEOGRAPH-76E6: not included in any glyphset definition</li>
<li>U+76EC CJK UNIFIED IDEOGRAPH-76EC: not included in any glyphset definition</li>
<li>U+76F7 CJK UNIFIED IDEOGRAPH-76F7: not included in any glyphset definition</li>
<li>U+770A CJK UNIFIED IDEOGRAPH-770A: not included in any glyphset definition</li>
<li>U+770D CJK UNIFIED IDEOGRAPH-770D: not included in any glyphset definition</li>
<li>U+771A CJK UNIFIED IDEOGRAPH-771A: not included in any glyphset definition</li>
<li>U+7722 CJK UNIFIED IDEOGRAPH-7722: not included in any glyphset definition</li>
<li>U+772C CJK UNIFIED IDEOGRAPH-772C: not included in any glyphset definition</li>
<li>U+7735 CJK UNIFIED IDEOGRAPH-7735: not included in any glyphset definition</li>
<li>U+7744 CJK UNIFIED IDEOGRAPH-7744: not included in any glyphset definition</li>
<li>U+7746 CJK UNIFIED IDEOGRAPH-7746: not included in any glyphset definition</li>
<li>U+774D CJK UNIFIED IDEOGRAPH-774D: not included in any glyphset definition</li>
<li>U+7780 CJK UNIFIED IDEOGRAPH-7780: not included in any glyphset definition</li>
<li>U+778D CJK UNIFIED IDEOGRAPH-778D: not included in any glyphset definition</li>
<li>U+7793 CJK UNIFIED IDEOGRAPH-7793: not included in any glyphset definition</li>
<li>U+77A2 CJK UNIFIED IDEOGRAPH-77A2: not included in any glyphset definition</li>
<li>U+77AB CJK UNIFIED IDEOGRAPH-77AB: not included in any glyphset definition</li>
<li>U+77B5 CJK UNIFIED IDEOGRAPH-77B5: not included in any glyphset definition</li>
<li>U+77DE CJK UNIFIED IDEOGRAPH-77DE: not included in any glyphset definition</li>
<li>U+77F0 CJK UNIFIED IDEOGRAPH-77F0: not included in any glyphset definition</li>
<li>U+77FB CJK UNIFIED IDEOGRAPH-77FB: not included in any glyphset definition</li>
<li>U+7804 CJK UNIFIED IDEOGRAPH-7804: not included in any glyphset definition</li>
<li>U+7806 CJK UNIFIED IDEOGRAPH-7806: not included in any glyphset definition</li>
<li>U+7807 CJK UNIFIED IDEOGRAPH-7807: not included in any glyphset definition</li>
<li>U+7809 CJK UNIFIED IDEOGRAPH-7809: not included in any glyphset definition</li>
<li>U+7811 CJK UNIFIED IDEOGRAPH-7811: not included in any glyphset definition</li>
<li>U+781F CJK UNIFIED IDEOGRAPH-781F: not included in any glyphset definition</li>
<li>U+7821 CJK UNIFIED IDEOGRAPH-7821: not included in any glyphset definition</li>
<li>U+7829 CJK UNIFIED IDEOGRAPH-7829: not included in any glyphset definition</li>
<li>U+782B CJK UNIFIED IDEOGRAPH-782B: not included in any glyphset definition</li>
<li>U+782C CJK UNIFIED IDEOGRAPH-782C: not included in any glyphset definition</li>
<li>U+782E CJK UNIFIED IDEOGRAPH-782E: not included in any glyphset definition</li>
<li>U+7831 CJK UNIFIED IDEOGRAPH-7831: not included in any glyphset definition</li>
<li>U+7839 CJK UNIFIED IDEOGRAPH-7839: not included in any glyphset definition</li>
<li>U+7841 CJK UNIFIED IDEOGRAPH-7841: not included in any glyphset definition</li>
<li>U+7847 CJK UNIFIED IDEOGRAPH-7847: not included in any glyphset definition</li>
<li>U+784A CJK UNIFIED IDEOGRAPH-784A: not included in any glyphset definition</li>
<li>U+784D CJK UNIFIED IDEOGRAPH-784D: not included in any glyphset definition</li>
<li>U+784E CJK UNIFIED IDEOGRAPH-784E: not included in any glyphset definition</li>
<li>U+784F CJK UNIFIED IDEOGRAPH-784F: not included in any glyphset definition</li>
<li>U+7853 CJK UNIFIED IDEOGRAPH-7853: not included in any glyphset definition</li>
<li>U+7857 CJK UNIFIED IDEOGRAPH-7857: not included in any glyphset definition</li>
<li>U+7859 CJK UNIFIED IDEOGRAPH-7859: not included in any glyphset definition</li>
<li>U+785C CJK UNIFIED IDEOGRAPH-785C: not included in any glyphset definition</li>
<li>U+7866 CJK UNIFIED IDEOGRAPH-7866: not included in any glyphset definition</li>
<li>U+786A CJK UNIFIED IDEOGRAPH-786A: not included in any glyphset definition</li>
<li>U+786D CJK UNIFIED IDEOGRAPH-786D: not included in any glyphset definition</li>
<li>U+787F CJK UNIFIED IDEOGRAPH-787F: not included in any glyphset definition</li>
<li>U+7883 CJK UNIFIED IDEOGRAPH-7883: not included in any glyphset definition</li>
<li>U+788F CJK UNIFIED IDEOGRAPH-788F: not included in any glyphset definition</li>
<li>U+7896 CJK UNIFIED IDEOGRAPH-7896: not included in any glyphset definition</li>
<li>U+78A1 CJK UNIFIED IDEOGRAPH-78A1: not included in any glyphset definition</li>
<li>U+78A5 CJK UNIFIED IDEOGRAPH-78A5: not included in any glyphset definition</li>
<li>U+78A8 CJK UNIFIED IDEOGRAPH-78A8: not included in any glyphset definition</li>
<li>U+78AD CJK UNIFIED IDEOGRAPH-78AD: not included in any glyphset definition</li>
<li>U+78B2 CJK UNIFIED IDEOGRAPH-78B2: not included in any glyphset definition</li>
<li>U+78B6 CJK UNIFIED IDEOGRAPH-78B6: not included in any glyphset definition</li>
<li>U+78B8 CJK UNIFIED IDEOGRAPH-78B8: not included in any glyphset definition</li>
<li>U+78BB CJK UNIFIED IDEOGRAPH-78BB: not included in any glyphset definition</li>
<li>U+78C9 CJK UNIFIED IDEOGRAPH-78C9: not included in any glyphset definition</li>
<li>U+78CE CJK UNIFIED IDEOGRAPH-78CE: not included in any glyphset definition</li>
<li>U+78CF CJK UNIFIED IDEOGRAPH-78CF: not included in any glyphset definition</li>
<li>U+78D9 CJK UNIFIED IDEOGRAPH-78D9: not included in any glyphset definition</li>
<li>U+78DC CJK UNIFIED IDEOGRAPH-78DC: not included in any glyphset definition</li>
<li>U+78F9 CJK UNIFIED IDEOGRAPH-78F9: not included in any glyphset definition</li>
<li>U+78FB CJK UNIFIED IDEOGRAPH-78FB: not included in any glyphset definition</li>
<li>U+78FE CJK UNIFIED IDEOGRAPH-78FE: not included in any glyphset definition</li>
<li>U+7904 CJK UNIFIED IDEOGRAPH-7904: not included in any glyphset definition</li>
<li>U+7905 CJK UNIFIED IDEOGRAPH-7905: not included in any glyphset definition</li>
<li>U+7906 CJK UNIFIED IDEOGRAPH-7906: not included in any glyphset definition</li>
<li>U+790C CJK UNIFIED IDEOGRAPH-790C: not included in any glyphset definition</li>
<li>U+7910 CJK UNIFIED IDEOGRAPH-7910: not included in any glyphset definition</li>
<li>U+7913 CJK UNIFIED IDEOGRAPH-7913: not included in any glyphset definition</li>
<li>U+7916 CJK UNIFIED IDEOGRAPH-7916: not included in any glyphset definition</li>
<li>U+791E CJK UNIFIED IDEOGRAPH-791E: not included in any glyphset definition</li>
<li>U+7924 CJK UNIFIED IDEOGRAPH-7924: not included in any glyphset definition</li>
<li>U+7930 CJK UNIFIED IDEOGRAPH-7930: not included in any glyphset definition</li>
<li>U+7931 CJK UNIFIED IDEOGRAPH-7931: not included in any glyphset definition</li>
<li>U+7935 CJK UNIFIED IDEOGRAPH-7935: not included in any glyphset definition</li>
<li>U+793B CJK UNIFIED IDEOGRAPH-793B: not included in any glyphset definition</li>
<li>U+7943 CJK UNIFIED IDEOGRAPH-7943: not included in any glyphset definition</li>
<li>U+7945 CJK UNIFIED IDEOGRAPH-7945: not included in any glyphset definition</li>
<li>U+7946 CJK UNIFIED IDEOGRAPH-7946: not included in any glyphset definition</li>
<li>U+794A CJK UNIFIED IDEOGRAPH-794A: not included in any glyphset definition</li>
<li>U+794B CJK UNIFIED IDEOGRAPH-794B: not included in any glyphset definition</li>
<li>U+794F CJK UNIFIED IDEOGRAPH-794F: not included in any glyphset definition</li>
<li>U+7967 CJK UNIFIED IDEOGRAPH-7967: not included in any glyphset definition</li>
<li>U+7972 CJK UNIFIED IDEOGRAPH-7972: not included in any glyphset definition</li>
<li>U+797E CJK UNIFIED IDEOGRAPH-797E: not included in any glyphset definition</li>
<li>U+798B CJK UNIFIED IDEOGRAPH-798B: not included in any glyphset definition</li>
<li>U+7991 CJK UNIFIED IDEOGRAPH-7991: not included in any glyphset definition</li>
<li>U+7992 CJK UNIFIED IDEOGRAPH-7992: not included in any glyphset definition</li>
<li>U+7998 CJK UNIFIED IDEOGRAPH-7998: not included in any glyphset definition</li>
<li>U+799A CJK UNIFIED IDEOGRAPH-799A: not included in any glyphset definition</li>
<li>U+79A1 CJK UNIFIED IDEOGRAPH-79A1: not included in any glyphset definition</li>
<li>U+79DE CJK UNIFIED IDEOGRAPH-79DE: not included in any glyphset definition</li>
<li>U+79EB CJK UNIFIED IDEOGRAPH-79EB: not included in any glyphset definition</li>
<li>U+79FE CJK UNIFIED IDEOGRAPH-79FE: not included in any glyphset definition</li>
<li>U+7A02 CJK UNIFIED IDEOGRAPH-7A02: not included in any glyphset definition</li>
<li>U+7A03 CJK UNIFIED IDEOGRAPH-7A03: not included in any glyphset definition</li>
<li>U+7A0C CJK UNIFIED IDEOGRAPH-7A0C: not included in any glyphset definition</li>
<li>U+7A11 CJK UNIFIED IDEOGRAPH-7A11: not included in any glyphset definition</li>
<li>U+7A36 CJK UNIFIED IDEOGRAPH-7A36: not included in any glyphset definition</li>
<li>U+7A44 CJK UNIFIED IDEOGRAPH-7A44: not included in any glyphset definition</li>
<li>U+7A47 CJK UNIFIED IDEOGRAPH-7A47: not included in any glyphset definition</li>
<li>U+7A4B CJK UNIFIED IDEOGRAPH-7A4B: not included in any glyphset definition</li>
<li>U+7A51 CJK UNIFIED IDEOGRAPH-7A51: not included in any glyphset definition</li>
<li>U+7A59 CJK UNIFIED IDEOGRAPH-7A59: not included in any glyphset definition</li>
<li>U+7A5C CJK UNIFIED IDEOGRAPH-7A5C: not included in any glyphset definition</li>
<li>U+7A5F CJK UNIFIED IDEOGRAPH-7A5F: not included in any glyphset definition</li>
<li>U+7A66 CJK UNIFIED IDEOGRAPH-7A66: not included in any glyphset definition</li>
<li>U+7A68 CJK UNIFIED IDEOGRAPH-7A68: not included in any glyphset definition</li>
<li>U+7A78 CJK UNIFIED IDEOGRAPH-7A78: not included in any glyphset definition</li>
<li>U+7A80 CJK UNIFIED IDEOGRAPH-7A80: not included in any glyphset definition</li>
<li>U+7A85 CJK UNIFIED IDEOGRAPH-7A85: not included in any glyphset definition</li>
<li>U+7A86 CJK UNIFIED IDEOGRAPH-7A86: not included in any glyphset definition</li>
<li>U+7A8A CJK UNIFIED IDEOGRAPH-7A8A: not included in any glyphset definition</li>
<li>U+7A8E CJK UNIFIED IDEOGRAPH-7A8E: not included in any glyphset definition</li>
<li>U+7AAC CJK UNIFIED IDEOGRAPH-7AAC: not included in any glyphset definition</li>
<li>U+7AAD CJK UNIFIED IDEOGRAPH-7AAD: not included in any glyphset definition</li>
<li>U+7AB5 CJK UNIFIED IDEOGRAPH-7AB5: not included in any glyphset definition</li>
<li>U+7AD7 CJK UNIFIED IDEOGRAPH-7AD7: not included in any glyphset definition</li>
<li>U+7AD8 CJK UNIFIED IDEOGRAPH-7AD8: not included in any glyphset definition</li>
<li>U+7AEB CJK UNIFIED IDEOGRAPH-7AEB: not included in any glyphset definition</li>
<li>U+7B24 CJK UNIFIED IDEOGRAPH-7B24: not included in any glyphset definition</li>
<li>U+7B2E CJK UNIFIED IDEOGRAPH-7B2E: not included in any glyphset definition</li>
<li>U+7B2F CJK UNIFIED IDEOGRAPH-7B2F: not included in any glyphset definition</li>
<li>U+7B31 CJK UNIFIED IDEOGRAPH-7B31: not included in any glyphset definition</li>
<li>U+7B38 CJK UNIFIED IDEOGRAPH-7B38: not included in any glyphset definition</li>
<li>U+7B3E CJK UNIFIED IDEOGRAPH-7B3E: not included in any glyphset definition</li>
<li>U+7B40 CJK UNIFIED IDEOGRAPH-7B40: not included in any glyphset definition</li>
<li>U+7B47 CJK UNIFIED IDEOGRAPH-7B47: not included in any glyphset definition</li>
<li>U+7B58 CJK UNIFIED IDEOGRAPH-7B58: not included in any glyphset definition</li>
<li>U+7B5C CJK UNIFIED IDEOGRAPH-7B5C: not included in any glyphset definition</li>
<li>U+7B62 CJK UNIFIED IDEOGRAPH-7B62: not included in any glyphset definition</li>
<li>U+7B64 CJK UNIFIED IDEOGRAPH-7B64: not included in any glyphset definition</li>
<li>U+7B66 CJK UNIFIED IDEOGRAPH-7B66: not included in any glyphset definition</li>
<li>U+7B69 CJK UNIFIED IDEOGRAPH-7B69: not included in any glyphset definition</li>
<li>U+7B6F CJK UNIFIED IDEOGRAPH-7B6F: not included in any glyphset definition</li>
<li>U+7B76 CJK UNIFIED IDEOGRAPH-7B76: not included in any glyphset definition</li>
<li>U+7B7C CJK UNIFIED IDEOGRAPH-7B7C: not included in any glyphset definition</li>
<li>U+7B7D CJK UNIFIED IDEOGRAPH-7B7D: not included in any glyphset definition</li>
<li>U+7B84 CJK UNIFIED IDEOGRAPH-7B84: not included in any glyphset definition</li>
<li>U+7B8E CJK UNIFIED IDEOGRAPH-7B8E: not included in any glyphset definition</li>
<li>U+7B9E CJK UNIFIED IDEOGRAPH-7B9E: not included in any glyphset definition</li>
<li>U+7BA0 CJK UNIFIED IDEOGRAPH-7BA0: not included in any glyphset definition</li>
<li>U+7BA6 CJK UNIFIED IDEOGRAPH-7BA6: not included in any glyphset definition</li>
<li>U+7BA8 CJK UNIFIED IDEOGRAPH-7BA8: not included in any glyphset definition</li>
<li>U+7BD2 CJK UNIFIED IDEOGRAPH-7BD2: not included in any glyphset definition</li>
<li>U+7BD4 CJK UNIFIED IDEOGRAPH-7BD4: not included in any glyphset definition</li>
<li>U+7BDA CJK UNIFIED IDEOGRAPH-7BDA: not included in any glyphset definition</li>
<li>U+7BDB CJK UNIFIED IDEOGRAPH-7BDB: not included in any glyphset definition</li>
<li>U+7BE2 CJK UNIFIED IDEOGRAPH-7BE2: not included in any glyphset definition</li>
<li>U+7BEF CJK UNIFIED IDEOGRAPH-7BEF: not included in any glyphset definition</li>
<li>U+7C03 CJK UNIFIED IDEOGRAPH-7C03: not included in any glyphset definition</li>
<li>U+7C09 CJK UNIFIED IDEOGRAPH-7C09: not included in any glyphset definition</li>
<li>U+7C0F CJK UNIFIED IDEOGRAPH-7C0F: not included in any glyphset definition</li>
<li>U+7C15 CJK UNIFIED IDEOGRAPH-7C15: not included in any glyphset definition</li>
<li>U+7C16 CJK UNIFIED IDEOGRAPH-7C16: not included in any glyphset definition</li>
<li>U+7C1D CJK UNIFIED IDEOGRAPH-7C1D: not included in any glyphset definition</li>
<li>U+7C20 CJK UNIFIED IDEOGRAPH-7C20: not included in any glyphset definition</li>
<li>U+7C26 CJK UNIFIED IDEOGRAPH-7C26: not included in any glyphset definition</li>
<li>U+7C30 CJK UNIFIED IDEOGRAPH-7C30: not included in any glyphset definition</li>
<li>U+7C39 CJK UNIFIED IDEOGRAPH-7C39: not included in any glyphset definition</li>
<li>U+7C53 CJK UNIFIED IDEOGRAPH-7C53: not included in any glyphset definition</li>
<li>U+7C57 CJK UNIFIED IDEOGRAPH-7C57: not included in any glyphset definition</li>
<li>U+7C5B CJK UNIFIED IDEOGRAPH-7C5B: not included in any glyphset definition</li>
<li>U+7C5C CJK UNIFIED IDEOGRAPH-7C5C: not included in any glyphset definition</li>
<li>U+7C63 CJK UNIFIED IDEOGRAPH-7C63: not included in any glyphset definition</li>
<li>U+7C69 CJK UNIFIED IDEOGRAPH-7C69: not included in any glyphset definition</li>
<li>U+7C6A CJK UNIFIED IDEOGRAPH-7C6A: not included in any glyphset definition</li>
<li>U+7C74 CJK UNIFIED IDEOGRAPH-7C74: not included in any glyphset definition</li>
<li>U+7C78 CJK UNIFIED IDEOGRAPH-7C78: not included in any glyphset definition</li>
<li>U+7C9D CJK UNIFIED IDEOGRAPH-7C9D: not included in any glyphset definition</li>
<li>U+7C9E CJK UNIFIED IDEOGRAPH-7C9E: not included in any glyphset definition</li>
<li>U+7CA9 CJK UNIFIED IDEOGRAPH-7CA9: not included in any glyphset definition</li>
<li>U+7CBA CJK UNIFIED IDEOGRAPH-7CBA: not included in any glyphset definition</li>
<li>U+7CC8 CJK UNIFIED IDEOGRAPH-7CC8: not included in any glyphset definition</li>
<li>U+7CC9 CJK UNIFIED IDEOGRAPH-7CC9: not included in any glyphset definition</li>
<li>U+7CCC CJK UNIFIED IDEOGRAPH-7CCC: not included in any glyphset definition</li>
<li>U+7CDD CJK UNIFIED IDEOGRAPH-7CDD: not included in any glyphset definition</li>
<li>U+7CE8 CJK UNIFIED IDEOGRAPH-7CE8: not included in any glyphset definition</li>
<li>U+7CF9 CJK UNIFIED IDEOGRAPH-7CF9: not included in any glyphset definition</li>
<li>U+7D03 CJK UNIFIED IDEOGRAPH-7D03: not included in any glyphset definition</li>
<li>U+7D07 CJK UNIFIED IDEOGRAPH-7D07: not included in any glyphset definition</li>
<li>U+7D16 CJK UNIFIED IDEOGRAPH-7D16: not included in any glyphset definition</li>
<li>U+7D1E CJK UNIFIED IDEOGRAPH-7D1E: not included in any glyphset definition</li>
<li>U+7D31 CJK UNIFIED IDEOGRAPH-7D31: not included in any glyphset definition</li>
<li>U+7D3C CJK UNIFIED IDEOGRAPH-7D3C: not included in any glyphset definition</li>
<li>U+7D48 CJK UNIFIED IDEOGRAPH-7D48: not included in any glyphset definition</li>
<li>U+7D53 CJK UNIFIED IDEOGRAPH-7D53: not included in any glyphset definition</li>
<li>U+7D5D CJK UNIFIED IDEOGRAPH-7D5D: not included in any glyphset definition</li>
<li>U+7D6A CJK UNIFIED IDEOGRAPH-7D6A: not included in any glyphset definition</li>
<li>U+7D70 CJK UNIFIED IDEOGRAPH-7D70: not included in any glyphset definition</li>
<li>U+7D77 CJK UNIFIED IDEOGRAPH-7D77: not included in any glyphset definition</li>
<li>U+7D7A CJK UNIFIED IDEOGRAPH-7D7A: not included in any glyphset definition</li>
<li>U+7D7F CJK UNIFIED IDEOGRAPH-7D7F: not included in any glyphset definition</li>
<li>U+7D84 CJK UNIFIED IDEOGRAPH-7D84: not included in any glyphset definition</li>
<li>U+7D86 CJK UNIFIED IDEOGRAPH-7D86: not included in any glyphset definition</li>
<li>U+7D88 CJK UNIFIED IDEOGRAPH-7D88: not included in any glyphset definition</li>
<li>U+7D8C CJK UNIFIED IDEOGRAPH-7D8C: not included in any glyphset definition</li>
<li>U+7D8E CJK UNIFIED IDEOGRAPH-7D8E: not included in any glyphset definition</li>
<li>U+7D96 CJK UNIFIED IDEOGRAPH-7D96: not included in any glyphset definition</li>
<li>U+7D9D CJK UNIFIED IDEOGRAPH-7D9D: not included in any glyphset definition</li>
<li>U+7D9E CJK UNIFIED IDEOGRAPH-7D9E: not included in any glyphset definition</li>
<li>U+7DA1 CJK UNIFIED IDEOGRAPH-7DA1: not included in any glyphset definition</li>
<li>U+7DA7 CJK UNIFIED IDEOGRAPH-7DA7: not included in any glyphset definition</li>
<li>U+7DAA CJK UNIFIED IDEOGRAPH-7DAA: not included in any glyphset definition</li>
<li>U+7DB3 CJK UNIFIED IDEOGRAPH-7DB3: not included in any glyphset definition</li>
<li>U+7DB7 CJK UNIFIED IDEOGRAPH-7DB7: not included in any glyphset definition</li>
<li>U+7DC4 CJK UNIFIED IDEOGRAPH-7DC4: not included in any glyphset definition</li>
<li>U+7DD6 CJK UNIFIED IDEOGRAPH-7DD6: not included in any glyphset definition</li>
<li>U+7DD9 CJK UNIFIED IDEOGRAPH-7DD9: not included in any glyphset definition</li>
<li>U+7DE6 CJK UNIFIED IDEOGRAPH-7DE6: not included in any glyphset definition</li>
<li>U+7DF1 CJK UNIFIED IDEOGRAPH-7DF1: not included in any glyphset definition</li>
<li>U+7DF6 CJK UNIFIED IDEOGRAPH-7DF6: not included in any glyphset definition</li>
<li>U+7E11 CJK UNIFIED IDEOGRAPH-7E11: not included in any glyphset definition</li>
<li>U+7E17 CJK UNIFIED IDEOGRAPH-7E17: not included in any glyphset definition</li>
<li>U+7E20 CJK UNIFIED IDEOGRAPH-7E20: not included in any glyphset definition</li>
<li>U+7E27 CJK UNIFIED IDEOGRAPH-7E27: not included in any glyphset definition</li>
<li>U+7E2F CJK UNIFIED IDEOGRAPH-7E2F: not included in any glyphset definition</li>
<li>U+7E33 CJK UNIFIED IDEOGRAPH-7E33: not included in any glyphset definition</li>
<li>U+7E36 CJK UNIFIED IDEOGRAPH-7E36: not included in any glyphset definition</li>
<li>U+7E3F CJK UNIFIED IDEOGRAPH-7E3F: not included in any glyphset definition</li>
<li>U+7E44 CJK UNIFIED IDEOGRAPH-7E44: not included in any glyphset definition</li>
<li>U+7E45 CJK UNIFIED IDEOGRAPH-7E45: not included in any glyphset definition</li>
<li>U+7E48 CJK UNIFIED IDEOGRAPH-7E48: not included in any glyphset definition</li>
<li>U+7E62 CJK UNIFIED IDEOGRAPH-7E62: not included in any glyphset definition</li>
<li>U+7E6E CJK UNIFIED IDEOGRAPH-7E6E: not included in any glyphset definition</li>
<li>U+7E6F CJK UNIFIED IDEOGRAPH-7E6F: not included in any glyphset definition</li>
<li>U+7E76 CJK UNIFIED IDEOGRAPH-7E76: not included in any glyphset definition</li>
<li>U+7E81 CJK UNIFIED IDEOGRAPH-7E81: not included in any glyphset definition</li>
<li>U+7E86 CJK UNIFIED IDEOGRAPH-7E86: not included in any glyphset definition</li>
<li>U+7E8A CJK UNIFIED IDEOGRAPH-7E8A: not included in any glyphset definition</li>
<li>U+7E95 CJK UNIFIED IDEOGRAPH-7E95: not included in any glyphset definition</li>
<li>U+7E98 CJK UNIFIED IDEOGRAPH-7E98: not included in any glyphset definition</li>
<li>U+7EA5 CJK UNIFIED IDEOGRAPH-7EA5: not included in any glyphset definition</li>
<li>U+7EA9 CJK UNIFIED IDEOGRAPH-7EA9: not included in any glyphset definition</li>
<li>U+7EB4 CJK UNIFIED IDEOGRAPH-7EB4: not included in any glyphset definition</li>
<li>U+7EBB CJK UNIFIED IDEOGRAPH-7EBB: not included in any glyphset definition</li>
<li>U+7EBC CJK UNIFIED IDEOGRAPH-7EBC: not included in any glyphset definition</li>
<li>U+7ED6 CJK UNIFIED IDEOGRAPH-7ED6: not included in any glyphset definition</li>
<li>U+7EE4 CJK UNIFIED IDEOGRAPH-7EE4: not included in any glyphset definition</li>
<li>U+7EE8 CJK UNIFIED IDEOGRAPH-7EE8: not included in any glyphset definition</li>
<li>U+7EF2 CJK UNIFIED IDEOGRAPH-7EF2: not included in any glyphset definition</li>
<li>U+7EF9 CJK UNIFIED IDEOGRAPH-7EF9: not included in any glyphset definition</li>
<li>U+7F0A CJK UNIFIED IDEOGRAPH-7F0A: not included in any glyphset definition</li>
<li>U+7F0B CJK UNIFIED IDEOGRAPH-7F0B: not included in any glyphset definition</li>
<li>U+7F0C CJK UNIFIED IDEOGRAPH-7F0C: not included in any glyphset definition</li>
<li>U+7F0D CJK UNIFIED IDEOGRAPH-7F0D: not included in any glyphset definition</li>
<li>U+7F0F CJK UNIFIED IDEOGRAPH-7F0F: not included in any glyphset definition</li>
<li>U+7F10 CJK UNIFIED IDEOGRAPH-7F10: not included in any glyphset definition</li>
<li>U+7F11 CJK UNIFIED IDEOGRAPH-7F11: not included in any glyphset definition</li>
<li>U+7F12 CJK UNIFIED IDEOGRAPH-7F12: not included in any glyphset definition</li>
<li>U+7F17 CJK UNIFIED IDEOGRAPH-7F17: not included in any glyphset definition</li>
<li>U+7F1E CJK UNIFIED IDEOGRAPH-7F1E: not included in any glyphset definition</li>
<li>U+7F21 CJK UNIFIED IDEOGRAPH-7F21: not included in any glyphset definition</li>
<li>U+7F23 CJK UNIFIED IDEOGRAPH-7F23: not included in any glyphset definition</li>
<li>U+7F27 CJK UNIFIED IDEOGRAPH-7F27: not included in any glyphset definition</li>
<li>U+7F2B CJK UNIFIED IDEOGRAPH-7F2B: not included in any glyphset definition</li>
<li>U+7F2F CJK UNIFIED IDEOGRAPH-7F2F: not included in any glyphset definition</li>
<li>U+7F32 CJK UNIFIED IDEOGRAPH-7F32: not included in any glyphset definition</li>
<li>U+7F33 CJK UNIFIED IDEOGRAPH-7F33: not included in any glyphset definition</li>
<li>U+7F35 CJK UNIFIED IDEOGRAPH-7F35: not included in any glyphset definition</li>
<li>U+7F43 CJK UNIFIED IDEOGRAPH-7F43: not included in any glyphset definition</li>
<li>U+7F47 CJK UNIFIED IDEOGRAPH-7F47: not included in any glyphset definition</li>
<li>U+7F74 CJK UNIFIED IDEOGRAPH-7F74: not included in any glyphset definition</li>
<li>U+7F76 CJK UNIFIED IDEOGRAPH-7F76: not included in any glyphset definition</li>
<li>U+7F7D CJK UNIFIED IDEOGRAPH-7F7D: not included in any glyphset definition</li>
<li>U+7F7E CJK UNIFIED IDEOGRAPH-7F7E: not included in any glyphset definition</li>
<li>U+7F91 CJK UNIFIED IDEOGRAPH-7F91: not included in any glyphset definition</li>
<li>U+7F93 CJK UNIFIED IDEOGRAPH-7F93: not included in any glyphset definition</li>
<li>U+7F95 CJK UNIFIED IDEOGRAPH-7F95: not included in any glyphset definition</li>
<li>U+7F96 CJK UNIFIED IDEOGRAPH-7F96: not included in any glyphset definition</li>
<li>U+7FB1 CJK UNIFIED IDEOGRAPH-7FB1: not included in any glyphset definition</li>
<li>U+7FBC CJK UNIFIED IDEOGRAPH-7FBC: not included in any glyphset definition</li>
<li>U+7FC2 CJK UNIFIED IDEOGRAPH-7FC2: not included in any glyphset definition</li>
<li>U+7FC8 CJK UNIFIED IDEOGRAPH-7FC8: not included in any glyphset definition</li>
<li>U+7FD9 CJK UNIFIED IDEOGRAPH-7FD9: not included in any glyphset definition</li>
<li>U+7FDA CJK UNIFIED IDEOGRAPH-7FDA: not included in any glyphset definition</li>
<li>U+7FDB CJK UNIFIED IDEOGRAPH-7FDB: not included in any glyphset definition</li>
<li>U+7FEC CJK UNIFIED IDEOGRAPH-7FEC: not included in any glyphset definition</li>
<li>U+7FEE CJK UNIFIED IDEOGRAPH-7FEE: not included in any glyphset definition</li>
<li>U+7FEF CJK UNIFIED IDEOGRAPH-7FEF: not included in any glyphset definition</li>
<li>U+7FF7 CJK UNIFIED IDEOGRAPH-7FF7: not included in any glyphset definition</li>
<li>U+7FFA CJK UNIFIED IDEOGRAPH-7FFA: not included in any glyphset definition</li>
<li>U+7FFD CJK UNIFIED IDEOGRAPH-7FFD: not included in any glyphset definition</li>
<li>U+7FFE CJK UNIFIED IDEOGRAPH-7FFE: not included in any glyphset definition</li>
<li>U+8007 CJK UNIFIED IDEOGRAPH-8007: not included in any glyphset definition</li>
<li>U+8009 CJK UNIFIED IDEOGRAPH-8009: not included in any glyphset definition</li>
<li>U+800F CJK UNIFIED IDEOGRAPH-800F: not included in any glyphset definition</li>
<li>U+8011 CJK UNIFIED IDEOGRAPH-8011: not included in any glyphset definition</li>
<li>U+8014 CJK UNIFIED IDEOGRAPH-8014: not included in any glyphset definition</li>
<li>U+8016 CJK UNIFIED IDEOGRAPH-8016: not included in any glyphset definition</li>
<li>U+8022 CJK UNIFIED IDEOGRAPH-8022: not included in any glyphset definition</li>
<li>U+8024 CJK UNIFIED IDEOGRAPH-8024: not included in any glyphset definition</li>
<li>U+8027 CJK UNIFIED IDEOGRAPH-8027: not included in any glyphset definition</li>
<li>U+8029 CJK UNIFIED IDEOGRAPH-8029: not included in any glyphset definition</li>
<li>U+802A CJK UNIFIED IDEOGRAPH-802A: not included in any glyphset definition</li>
<li>U+802C CJK UNIFIED IDEOGRAPH-802C: not included in any glyphset definition</li>
<li>U+802D CJK UNIFIED IDEOGRAPH-802D: not included in any glyphset definition</li>
<li>U+8030 CJK UNIFIED IDEOGRAPH-8030: not included in any glyphset definition</li>
<li>U+8032 CJK UNIFIED IDEOGRAPH-8032: not included in any glyphset definition</li>
<li>U+8035 CJK UNIFIED IDEOGRAPH-8035: not included in any glyphset definition</li>
<li>U+8043 CJK UNIFIED IDEOGRAPH-8043: not included in any glyphset definition</li>
<li>U+804D CJK UNIFIED IDEOGRAPH-804D: not included in any glyphset definition</li>
<li>U+8071 CJK UNIFIED IDEOGRAPH-8071: not included in any glyphset definition</li>
<li>U+809C CJK UNIFIED IDEOGRAPH-809C: not included in any glyphset definition</li>
<li>U+80AB CJK UNIFIED IDEOGRAPH-80AB: not included in any glyphset definition</li>
<li>U+80B8 CJK UNIFIED IDEOGRAPH-80B8: not included in any glyphset definition</li>
<li>U+80C2 CJK UNIFIED IDEOGRAPH-80C2: not included in any glyphset definition</li>
<li>U+80C7 CJK UNIFIED IDEOGRAPH-80C7: not included in any glyphset definition</li>
<li>U+80C8 CJK UNIFIED IDEOGRAPH-80C8: not included in any glyphset definition</li>
<li>U+80E0 CJK UNIFIED IDEOGRAPH-80E0: not included in any glyphset definition</li>
<li>U+80E3 CJK UNIFIED IDEOGRAPH-80E3: not included in any glyphset definition</li>
<li>U+80E8 CJK UNIFIED IDEOGRAPH-80E8: not included in any glyphset definition</li>
<li>U+80EC CJK UNIFIED IDEOGRAPH-80EC: not included in any glyphset definition</li>
<li>U+80F2 CJK UNIFIED IDEOGRAPH-80F2: not included in any glyphset definition</li>
<li>U+8112 CJK UNIFIED IDEOGRAPH-8112: not included in any glyphset definition</li>
<li>U+8117 CJK UNIFIED IDEOGRAPH-8117: not included in any glyphset definition</li>
<li>U+811D CJK UNIFIED IDEOGRAPH-811D: not included in any glyphset definition</li>
<li>U+811E CJK UNIFIED IDEOGRAPH-811E: not included in any glyphset definition</li>
<li>U+811F CJK UNIFIED IDEOGRAPH-811F: not included in any glyphset definition</li>
<li>U+8124 CJK UNIFIED IDEOGRAPH-8124: not included in any glyphset definition</li>
<li>U+812C CJK UNIFIED IDEOGRAPH-812C: not included in any glyphset definition</li>
<li>U+8130 CJK UNIFIED IDEOGRAPH-8130: not included in any glyphset definition</li>
<li>U+8136 CJK UNIFIED IDEOGRAPH-8136: not included in any glyphset definition</li>
<li>U+8137 CJK UNIFIED IDEOGRAPH-8137: not included in any glyphset definition</li>
<li>U+813F CJK UNIFIED IDEOGRAPH-813F: not included in any glyphset definition</li>
<li>U+8152 CJK UNIFIED IDEOGRAPH-8152: not included in any glyphset definition</li>
<li>U+8156 CJK UNIFIED IDEOGRAPH-8156: not included in any glyphset definition</li>
<li>U+8160 CJK UNIFIED IDEOGRAPH-8160: not included in any glyphset definition</li>
<li>U+8161 CJK UNIFIED IDEOGRAPH-8161: not included in any glyphset definition</li>
<li>U+8168 CJK UNIFIED IDEOGRAPH-8168: not included in any glyphset definition</li>
<li>U+816F CJK UNIFIED IDEOGRAPH-816F: not included in any glyphset definition</li>
<li>U+8199 CJK UNIFIED IDEOGRAPH-8199: not included in any glyphset definition</li>
<li>U+819E CJK UNIFIED IDEOGRAPH-819E: not included in any glyphset definition</li>
<li>U+81A2 CJK UNIFIED IDEOGRAPH-81A2: not included in any glyphset definition</li>
<li>U+81B6 CJK UNIFIED IDEOGRAPH-81B6: not included in any glyphset definition</li>
<li>U+81CC CJK UNIFIED IDEOGRAPH-81CC: not included in any glyphset definition</li>
<li>U+81DC CJK UNIFIED IDEOGRAPH-81DC: not included in any glyphset definition</li>
<li>U+81E2 CJK UNIFIED IDEOGRAPH-81E2: not included in any glyphset definition</li>
<li>U+8204 CJK UNIFIED IDEOGRAPH-8204: not included in any glyphset definition</li>
<li>U+8220 CJK UNIFIED IDEOGRAPH-8220: not included in any glyphset definition</li>
<li>U+8221 CJK UNIFIED IDEOGRAPH-8221: not included in any glyphset definition</li>
<li>U+8223 CJK UNIFIED IDEOGRAPH-8223: not included in any glyphset definition</li>
<li>U+8225 CJK UNIFIED IDEOGRAPH-8225: not included in any glyphset definition</li>
<li>U+822F CJK UNIFIED IDEOGRAPH-822F: not included in any glyphset definition</li>
<li>U+8232 CJK UNIFIED IDEOGRAPH-8232: not included in any glyphset definition</li>
<li>U+8234 CJK UNIFIED IDEOGRAPH-8234: not included in any glyphset definition</li>
<li>U+823B CJK UNIFIED IDEOGRAPH-823B: not included in any glyphset definition</li>
<li>U+823E CJK UNIFIED IDEOGRAPH-823E: not included in any glyphset definition</li>
<li>U+8244 CJK UNIFIED IDEOGRAPH-8244: not included in any glyphset definition</li>
<li>U+8245 CJK UNIFIED IDEOGRAPH-8245: not included in any glyphset definition</li>
<li>U+824E CJK UNIFIED IDEOGRAPH-824E: not included in any glyphset definition</li>
<li>U+824F CJK UNIFIED IDEOGRAPH-824F: not included in any glyphset definition</li>
<li>U+8274 CJK UNIFIED IDEOGRAPH-8274: not included in any glyphset definition</li>
<li>U+827D CJK UNIFIED IDEOGRAPH-827D: not included in any glyphset definition</li>
<li>U+8284 CJK UNIFIED IDEOGRAPH-8284: not included in any glyphset definition</li>
<li>U+828F CJK UNIFIED IDEOGRAPH-828F: not included in any glyphset definition</li>
<li>U+8291 CJK UNIFIED IDEOGRAPH-8291: not included in any glyphset definition</li>
<li>U+829A CJK UNIFIED IDEOGRAPH-829A: not included in any glyphset definition</li>
<li>U+829B CJK UNIFIED IDEOGRAPH-829B: not included in any glyphset definition</li>
<li>U+82A0 CJK UNIFIED IDEOGRAPH-82A0: not included in any glyphset definition</li>
<li>U+82A3 CJK UNIFIED IDEOGRAPH-82A3: not included in any glyphset definition</li>
<li>U+82A4 CJK UNIFIED IDEOGRAPH-82A4: not included in any glyphset definition</li>
<li>U+82A7 CJK UNIFIED IDEOGRAPH-82A7: not included in any glyphset definition</li>
<li>U+82B0 CJK UNIFIED IDEOGRAPH-82B0: not included in any glyphset definition</li>
<li>U+82B5 CJK UNIFIED IDEOGRAPH-82B5: not included in any glyphset definition</li>
<li>U+82BC CJK UNIFIED IDEOGRAPH-82BC: not included in any glyphset definition</li>
<li>U+82C8 CJK UNIFIED IDEOGRAPH-82C8: not included in any glyphset definition</li>
<li>U+82C9 CJK UNIFIED IDEOGRAPH-82C9: not included in any glyphset definition</li>
<li>U+82D6 CJK UNIFIED IDEOGRAPH-82D6: not included in any glyphset definition</li>
<li>U+82E0 CJK UNIFIED IDEOGRAPH-82E0: not included in any glyphset definition</li>
<li>U+82E4 CJK UNIFIED IDEOGRAPH-82E4: not included in any glyphset definition</li>
<li>U+8300 CJK UNIFIED IDEOGRAPH-8300: not included in any glyphset definition</li>
<li>U+8307 CJK UNIFIED IDEOGRAPH-8307: not included in any glyphset definition</li>
<li>U+830B CJK UNIFIED IDEOGRAPH-830B: not included in any glyphset definition</li>
<li>U+8311 CJK UNIFIED IDEOGRAPH-8311: not included in any glyphset definition</li>
<li>U+8313 CJK UNIFIED IDEOGRAPH-8313: not included in any glyphset definition</li>
<li>U+831A CJK UNIFIED IDEOGRAPH-831A: not included in any glyphset definition</li>
<li>U+831D CJK UNIFIED IDEOGRAPH-831D: not included in any glyphset definition</li>
<li>U+8333 CJK UNIFIED IDEOGRAPH-8333: not included in any glyphset definition</li>
<li>U+833A CJK UNIFIED IDEOGRAPH-833A: not included in any glyphset definition</li>
<li>U+8341 CJK UNIFIED IDEOGRAPH-8341: not included in any glyphset definition</li>
<li>U+8344 CJK UNIFIED IDEOGRAPH-8344: not included in any glyphset definition</li>
<li>U+8351 CJK UNIFIED IDEOGRAPH-8351: not included in any glyphset definition</li>
<li>U+8353 CJK UNIFIED IDEOGRAPH-8353: not included in any glyphset definition</li>
<li>U+8359 CJK UNIFIED IDEOGRAPH-8359: not included in any glyphset definition</li>
<li>U+835B CJK UNIFIED IDEOGRAPH-835B: not included in any glyphset definition</li>
<li>U+835C CJK UNIFIED IDEOGRAPH-835C: not included in any glyphset definition</li>
<li>U+8369 CJK UNIFIED IDEOGRAPH-8369: not included in any glyphset definition</li>
<li>U+836C CJK UNIFIED IDEOGRAPH-836C: not included in any glyphset definition</li>
<li>U+836E CJK UNIFIED IDEOGRAPH-836E: not included in any glyphset definition</li>
<li>U+837A CJK UNIFIED IDEOGRAPH-837A: not included in any glyphset definition</li>
<li>U+837F CJK UNIFIED IDEOGRAPH-837F: not included in any glyphset definition</li>
<li>U+8395 CJK UNIFIED IDEOGRAPH-8395: not included in any glyphset definition</li>
<li>U+8399 CJK UNIFIED IDEOGRAPH-8399: not included in any glyphset definition</li>
<li>U+839D CJK UNIFIED IDEOGRAPH-839D: not included in any glyphset definition</li>
<li>U+83A9 CJK UNIFIED IDEOGRAPH-83A9: not included in any glyphset definition</li>
<li>U+83B0 CJK UNIFIED IDEOGRAPH-83B0: not included in any glyphset definition</li>
<li>U+83B6 CJK UNIFIED IDEOGRAPH-83B6: not included in any glyphset definition</li>
<li>U+83B8 CJK UNIFIED IDEOGRAPH-83B8: not included in any glyphset definition</li>
<li>U+83C2 CJK UNIFIED IDEOGRAPH-83C2: not included in any glyphset definition</li>
<li>U+83D1 CJK UNIFIED IDEOGRAPH-83D1: not included in any glyphset definition</li>
<li>U+83E5 CJK UNIFIED IDEOGRAPH-83E5: not included in any glyphset definition</li>
<li>U+83EA CJK UNIFIED IDEOGRAPH-83EA: not included in any glyphset definition</li>
<li>U+83F6 CJK UNIFIED IDEOGRAPH-83F6: not included in any glyphset definition</li>
<li>U+83F9 CJK UNIFIED IDEOGRAPH-83F9: not included in any glyphset definition</li>
<li>U+83FC CJK UNIFIED IDEOGRAPH-83FC: not included in any glyphset definition</li>
<li>U+8406 CJK UNIFIED IDEOGRAPH-8406: not included in any glyphset definition</li>
<li>U+840F CJK UNIFIED IDEOGRAPH-840F: not included in any glyphset definition</li>
<li>U+8411 CJK UNIFIED IDEOGRAPH-8411: not included in any glyphset definition</li>
<li>U+841A CJK UNIFIED IDEOGRAPH-841A: not included in any glyphset definition</li>
<li>U+8433 CJK UNIFIED IDEOGRAPH-8433: not included in any glyphset definition</li>
<li>U+8439 CJK UNIFIED IDEOGRAPH-8439: not included in any glyphset definition</li>
<li>U+8456 CJK UNIFIED IDEOGRAPH-8456: not included in any glyphset definition</li>
<li>U+8459 CJK UNIFIED IDEOGRAPH-8459: not included in any glyphset definition</li>
<li>U+845C CJK UNIFIED IDEOGRAPH-845C: not included in any glyphset definition</li>
<li>U+8470 CJK UNIFIED IDEOGRAPH-8470: not included in any glyphset definition</li>
<li>U+8474 CJK UNIFIED IDEOGRAPH-8474: not included in any glyphset definition</li>
<li>U+8478 CJK UNIFIED IDEOGRAPH-8478: not included in any glyphset definition</li>
<li>U+8487 CJK UNIFIED IDEOGRAPH-8487: not included in any glyphset definition</li>
<li>U+8489 CJK UNIFIED IDEOGRAPH-8489: not included in any glyphset definition</li>
<li>U+848D CJK UNIFIED IDEOGRAPH-848D: not included in any glyphset definition</li>
<li>U+848E CJK UNIFIED IDEOGRAPH-848E: not included in any glyphset definition</li>
<li>U+8493 CJK UNIFIED IDEOGRAPH-8493: not included in any glyphset definition</li>
<li>U+849D CJK UNIFIED IDEOGRAPH-849D: not included in any glyphset definition</li>
<li>U+84B1 CJK UNIFIED IDEOGRAPH-84B1: not included in any glyphset definition</li>
<li>U+84C2 CJK UNIFIED IDEOGRAPH-84C2: not included in any glyphset definition</li>
<li>U+84C7 CJK UNIFIED IDEOGRAPH-84C7: not included in any glyphset definition</li>
<li>U+84CF CJK UNIFIED IDEOGRAPH-84CF: not included in any glyphset definition</li>
<li>U+84DC CJK UNIFIED IDEOGRAPH-84DC: not included in any glyphset definition</li>
<li>U+84E0 CJK UNIFIED IDEOGRAPH-84E0: not included in any glyphset definition</li>
<li>U+84E2 CJK UNIFIED IDEOGRAPH-84E2: not included in any glyphset definition</li>
<li>U+84E3 CJK UNIFIED IDEOGRAPH-84E3: not included in any glyphset definition</li>
<li>U+84EA CJK UNIFIED IDEOGRAPH-84EA: not included in any glyphset definition</li>
<li>U+84F0 CJK UNIFIED IDEOGRAPH-84F0: not included in any glyphset definition</li>
<li>U+84F3 CJK UNIFIED IDEOGRAPH-84F3: not included in any glyphset definition</li>
<li>U+8508 CJK UNIFIED IDEOGRAPH-8508: not included in any glyphset definition</li>
<li>U+850A CJK UNIFIED IDEOGRAPH-850A: not included in any glyphset definition</li>
<li>U+850C CJK UNIFIED IDEOGRAPH-850C: not included in any glyphset definition</li>
<li>U+852F CJK UNIFIED IDEOGRAPH-852F: not included in any glyphset definition</li>
<li>U+8534 CJK UNIFIED IDEOGRAPH-8534: not included in any glyphset definition</li>
<li>U+8538 CJK UNIFIED IDEOGRAPH-8538: not included in any glyphset definition</li>
<li>U+8539 CJK UNIFIED IDEOGRAPH-8539: not included in any glyphset definition</li>
<li>U+853F CJK UNIFIED IDEOGRAPH-853F: not included in any glyphset definition</li>
<li>U+8546 CJK UNIFIED IDEOGRAPH-8546: not included in any glyphset definition</li>
<li>U+8552 CJK UNIFIED IDEOGRAPH-8552: not included in any glyphset definition</li>
<li>U+8562 CJK UNIFIED IDEOGRAPH-8562: not included in any glyphset definition</li>
<li>U+856B CJK UNIFIED IDEOGRAPH-856B: not included in any glyphset definition</li>
<li>U+8579 CJK UNIFIED IDEOGRAPH-8579: not included in any glyphset definition</li>
<li>U+857A CJK UNIFIED IDEOGRAPH-857A: not included in any glyphset definition</li>
<li>U+8581 CJK UNIFIED IDEOGRAPH-8581: not included in any glyphset definition</li>
<li>U+8598 CJK UNIFIED IDEOGRAPH-8598: not included in any glyphset definition</li>
<li>U+859F CJK UNIFIED IDEOGRAPH-859F: not included in any glyphset definition</li>
<li>U+85A2 CJK UNIFIED IDEOGRAPH-85A2: not included in any glyphset definition</li>
<li>U+85B3 CJK UNIFIED IDEOGRAPH-85B3: not included in any glyphset definition</li>
<li>U+85B4 CJK UNIFIED IDEOGRAPH-85B4: not included in any glyphset definition</li>
<li>U+85B6 CJK UNIFIED IDEOGRAPH-85B6: not included in any glyphset definition</li>
<li>U+85B7 CJK UNIFIED IDEOGRAPH-85B7: not included in any glyphset definition</li>
<li>U+85B8 CJK UNIFIED IDEOGRAPH-85B8: not included in any glyphset definition</li>
<li>U+85BF CJK UNIFIED IDEOGRAPH-85BF: not included in any glyphset definition</li>
<li>U+85CE CJK UNIFIED IDEOGRAPH-85CE: not included in any glyphset definition</li>
<li>U+85DF CJK UNIFIED IDEOGRAPH-85DF: not included in any glyphset definition</li>
<li>U+85E0 CJK UNIFIED IDEOGRAPH-85E0: not included in any glyphset definition</li>
<li>U+85E8 CJK UNIFIED IDEOGRAPH-85E8: not included in any glyphset definition</li>
<li>U+85ED CJK UNIFIED IDEOGRAPH-85ED: not included in any glyphset definition</li>
<li>U+85F4 CJK UNIFIED IDEOGRAPH-85F4: not included in any glyphset definition</li>
<li>U+85F6 CJK UNIFIED IDEOGRAPH-85F6: not included in any glyphset definition</li>
<li>U+8600 CJK UNIFIED IDEOGRAPH-8600: not included in any glyphset definition</li>
<li>U+8612 CJK UNIFIED IDEOGRAPH-8612: not included in any glyphset definition</li>
<li>U+8618 CJK UNIFIED IDEOGRAPH-8618: not included in any glyphset definition</li>
<li>U+861E CJK UNIFIED IDEOGRAPH-861E: not included in any glyphset definition</li>
<li>U+8626 CJK UNIFIED IDEOGRAPH-8626: not included in any glyphset definition</li>
<li>U+8627 CJK UNIFIED IDEOGRAPH-8627: not included in any glyphset definition</li>
<li>U+8629 CJK UNIFIED IDEOGRAPH-8629: not included in any glyphset definition</li>
<li>U+863A CJK UNIFIED IDEOGRAPH-863A: not included in any glyphset definition</li>
<li>U+8649 CJK UNIFIED IDEOGRAPH-8649: not included in any glyphset definition</li>
<li>U+8652 CJK UNIFIED IDEOGRAPH-8652: not included in any glyphset definition</li>
<li>U+8653 CJK UNIFIED IDEOGRAPH-8653: not included in any glyphset definition</li>
<li>U+8664 CJK UNIFIED IDEOGRAPH-8664: not included in any glyphset definition</li>
<li>U+866E CJK UNIFIED IDEOGRAPH-866E: not included in any glyphset definition</li>
<li>U+8677 CJK UNIFIED IDEOGRAPH-8677: not included in any glyphset definition</li>
<li>U+8678 CJK UNIFIED IDEOGRAPH-8678: not included in any glyphset definition</li>
<li>U+867A CJK UNIFIED IDEOGRAPH-867A: not included in any glyphset definition</li>
<li>U+867C CJK UNIFIED IDEOGRAPH-867C: not included in any glyphset definition</li>
<li>U+867F CJK UNIFIED IDEOGRAPH-867F: not included in any glyphset definition</li>
<li>U+8684 CJK UNIFIED IDEOGRAPH-8684: not included in any glyphset definition</li>
<li>U+8686 CJK UNIFIED IDEOGRAPH-8686: not included in any glyphset definition</li>
<li>U+868D CJK UNIFIED IDEOGRAPH-868D: not included in any glyphset definition</li>
<li>U+86A8 CJK UNIFIED IDEOGRAPH-86A8: not included in any glyphset definition</li>
<li>U+86B4 CJK UNIFIED IDEOGRAPH-86B4: not included in any glyphset definition</li>
<li>U+86C3 CJK UNIFIED IDEOGRAPH-86C3: not included in any glyphset definition</li>
<li>U+86D1 CJK UNIFIED IDEOGRAPH-86D1: not included in any glyphset definition</li>
<li>U+86D8 CJK UNIFIED IDEOGRAPH-86D8: not included in any glyphset definition</li>
<li>U+86F1 CJK UNIFIED IDEOGRAPH-86F1: not included in any glyphset definition</li>
<li>U+86F2 CJK UNIFIED IDEOGRAPH-86F2: not included in any glyphset definition</li>
<li>U+86F4 CJK UNIFIED IDEOGRAPH-86F4: not included in any glyphset definition</li>
<li>U+870E CJK UNIFIED IDEOGRAPH-870E: not included in any glyphset definition</li>
<li>U+8710 CJK UNIFIED IDEOGRAPH-8710: not included in any glyphset definition</li>
<li>U+871E CJK UNIFIED IDEOGRAPH-871E: not included in any glyphset definition</li>
<li>U+8723 CJK UNIFIED IDEOGRAPH-8723: not included in any glyphset definition</li>
<li>U+872E CJK UNIFIED IDEOGRAPH-872E: not included in any glyphset definition</li>
<li>U+873E CJK UNIFIED IDEOGRAPH-873E: not included in any glyphset definition</li>
<li>U+8740 CJK UNIFIED IDEOGRAPH-8740: not included in any glyphset definition</li>
<li>U+8758 CJK UNIFIED IDEOGRAPH-8758: not included in any glyphset definition</li>
<li>U+8764 CJK UNIFIED IDEOGRAPH-8764: not included in any glyphset definition</li>
<li>U+8765 CJK UNIFIED IDEOGRAPH-8765: not included in any glyphset definition</li>
<li>U+8772 CJK UNIFIED IDEOGRAPH-8772: not included in any glyphset definition</li>
<li>U+877B CJK UNIFIED IDEOGRAPH-877B: not included in any glyphset definition</li>
<li>U+877D CJK UNIFIED IDEOGRAPH-877D: not included in any glyphset definition</li>
<li>U+8785 CJK UNIFIED IDEOGRAPH-8785: not included in any glyphset definition</li>
<li>U+878B CJK UNIFIED IDEOGRAPH-878B: not included in any glyphset definition</li>
<li>U+8793 CJK UNIFIED IDEOGRAPH-8793: not included in any glyphset definition</li>
<li>U+8797 CJK UNIFIED IDEOGRAPH-8797: not included in any glyphset definition</li>
<li>U+87A0 CJK UNIFIED IDEOGRAPH-87A0: not included in any glyphset definition</li>
<li>U+87A3 CJK UNIFIED IDEOGRAPH-87A3: not included in any glyphset definition</li>
<li>U+87AC CJK UNIFIED IDEOGRAPH-87AC: not included in any glyphset definition</li>
<li>U+87AE CJK UNIFIED IDEOGRAPH-87AE: not included in any glyphset definition</li>
<li>U+87B5 CJK UNIFIED IDEOGRAPH-87B5: not included in any glyphset definition</li>
<li>U+87CA CJK UNIFIED IDEOGRAPH-87CA: not included in any glyphset definition</li>
<li>U+87CE CJK UNIFIED IDEOGRAPH-87CE: not included in any glyphset definition</li>
<li>U+87CF CJK UNIFIED IDEOGRAPH-87CF: not included in any glyphset definition</li>
<li>U+87D3 CJK UNIFIED IDEOGRAPH-87D3: not included in any glyphset definition</li>
<li>U+87DB CJK UNIFIED IDEOGRAPH-87DB: not included in any glyphset definition</li>
<li>U+87E3 CJK UNIFIED IDEOGRAPH-87E3: not included in any glyphset definition</li>
<li>U+87E5 CJK UNIFIED IDEOGRAPH-87E5: not included in any glyphset definition</li>
<li>U+87E7 CJK UNIFIED IDEOGRAPH-87E7: not included in any glyphset definition</li>
<li>U+87EA CJK UNIFIED IDEOGRAPH-87EA: not included in any glyphset definition</li>
<li>U+87EB CJK UNIFIED IDEOGRAPH-87EB: not included in any glyphset definition</li>
<li>U+87EE CJK UNIFIED IDEOGRAPH-87EE: not included in any glyphset definition</li>
<li>U+8803 CJK UNIFIED IDEOGRAPH-8803: not included in any glyphset definition</li>
<li>U+8804 CJK UNIFIED IDEOGRAPH-8804: not included in any glyphset definition</li>
<li>U+8806 CJK UNIFIED IDEOGRAPH-8806: not included in any glyphset definition</li>
<li>U+8807 CJK UNIFIED IDEOGRAPH-8807: not included in any glyphset definition</li>
<li>U+880B CJK UNIFIED IDEOGRAPH-880B: not included in any glyphset definition</li>
<li>U+8810 CJK UNIFIED IDEOGRAPH-8810: not included in any glyphset definition</li>
<li>U+8813 CJK UNIFIED IDEOGRAPH-8813: not included in any glyphset definition</li>
<li>U+8828 CJK UNIFIED IDEOGRAPH-8828: not included in any glyphset definition</li>
<li>U+8832 CJK UNIFIED IDEOGRAPH-8832: not included in any glyphset definition</li>
<li>U+883C CJK UNIFIED IDEOGRAPH-883C: not included in any glyphset definition</li>
<li>U+8843 CJK UNIFIED IDEOGRAPH-8843: not included in any glyphset definition</li>
<li>U+884E CJK UNIFIED IDEOGRAPH-884E: not included in any glyphset definition</li>
<li>U+8864 CJK UNIFIED IDEOGRAPH-8864: not included in any glyphset definition</li>
<li>U+8886 CJK UNIFIED IDEOGRAPH-8886: not included in any glyphset definition</li>
<li>U+88AF CJK UNIFIED IDEOGRAPH-88AF: not included in any glyphset definition</li>
<li>U+88BC CJK UNIFIED IDEOGRAPH-88BC: not included in any glyphset definition</li>
<li>U+88C7 CJK UNIFIED IDEOGRAPH-88C7: not included in any glyphset definition</li>
<li>U+88C8 CJK UNIFIED IDEOGRAPH-88C8: not included in any glyphset definition</li>
<li>U+88C9 CJK UNIFIED IDEOGRAPH-88C9: not included in any glyphset definition</li>
<li>U+88CE CJK UNIFIED IDEOGRAPH-88CE: not included in any glyphset definition</li>
<li>U+88D2 CJK UNIFIED IDEOGRAPH-88D2: not included in any glyphset definition</li>
<li>U+88DB CJK UNIFIED IDEOGRAPH-88DB: not included in any glyphset definition</li>
<li>U+88E2 CJK UNIFIED IDEOGRAPH-88E2: not included in any glyphset definition</li>
<li>U+88E3 CJK UNIFIED IDEOGRAPH-88E3: not included in any glyphset definition</li>
<li>U+88E5 CJK UNIFIED IDEOGRAPH-88E5: not included in any glyphset definition</li>
<li>U+88EF CJK UNIFIED IDEOGRAPH-88EF: not included in any glyphset definition</li>
<li>U+88F0 CJK UNIFIED IDEOGRAPH-88F0: not included in any glyphset definition</li>
<li>U+88F5 CJK UNIFIED IDEOGRAPH-88F5: not included in any glyphset definition</li>
<li>U+8915 CJK UNIFIED IDEOGRAPH-8915: not included in any glyphset definition</li>
<li>U+8918 CJK UNIFIED IDEOGRAPH-8918: not included in any glyphset definition</li>
<li>U+891C CJK UNIFIED IDEOGRAPH-891C: not included in any glyphset definition</li>
<li>U+891F CJK UNIFIED IDEOGRAPH-891F: not included in any glyphset definition</li>
<li>U+892F CJK UNIFIED IDEOGRAPH-892F: not included in any glyphset definition</li>
<li>U+8933 CJK UNIFIED IDEOGRAPH-8933: not included in any glyphset definition</li>
<li>U+8935 CJK UNIFIED IDEOGRAPH-8935: not included in any glyphset definition</li>
<li>U+893D CJK UNIFIED IDEOGRAPH-893D: not included in any glyphset definition</li>
<li>U+8940 CJK UNIFIED IDEOGRAPH-8940: not included in any glyphset definition</li>
<li>U+8947 CJK UNIFIED IDEOGRAPH-8947: not included in any glyphset definition</li>
<li>U+894F CJK UNIFIED IDEOGRAPH-894F: not included in any glyphset definition</li>
<li>U+8955 CJK UNIFIED IDEOGRAPH-8955: not included in any glyphset definition</li>
<li>U+895A CJK UNIFIED IDEOGRAPH-895A: not included in any glyphset definition</li>
<li>U+895C CJK UNIFIED IDEOGRAPH-895C: not included in any glyphset definition</li>
<li>U+895D CJK UNIFIED IDEOGRAPH-895D: not included in any glyphset definition</li>
<li>U+896B CJK UNIFIED IDEOGRAPH-896B: not included in any glyphset definition</li>
<li>U+897B CJK UNIFIED IDEOGRAPH-897B: not included in any glyphset definition</li>
<li>U+898E CJK UNIFIED IDEOGRAPH-898E: not included in any glyphset definition</li>
<li>U+899C CJK UNIFIED IDEOGRAPH-899C: not included in any glyphset definition</li>
<li>U+89A4 CJK UNIFIED IDEOGRAPH-89A4: not included in any glyphset definition</li>
<li>U+89C3 CJK UNIFIED IDEOGRAPH-89C3: not included in any glyphset definition</li>
<li>U+89C7 CJK UNIFIED IDEOGRAPH-89C7: not included in any glyphset definition</li>
<li>U+89CB CJK UNIFIED IDEOGRAPH-89CB: not included in any glyphset definition</li>
<li>U+89CC CJK UNIFIED IDEOGRAPH-89CC: not included in any glyphset definition</li>
<li>U+89CF CJK UNIFIED IDEOGRAPH-89CF: not included in any glyphset definition</li>
<li>U+89D4 CJK UNIFIED IDEOGRAPH-89D4: not included in any glyphset definition</li>
<li>U+89D6 CJK UNIFIED IDEOGRAPH-89D6: not included in any glyphset definition</li>
<li>U+89DF CJK UNIFIED IDEOGRAPH-89DF: not included in any glyphset definition</li>
<li>U+89EB CJK UNIFIED IDEOGRAPH-89EB: not included in any glyphset definition</li>
<li>U+89ED CJK UNIFIED IDEOGRAPH-89ED: not included in any glyphset definition</li>
<li>U+89EF CJK UNIFIED IDEOGRAPH-89EF: not included in any glyphset definition</li>
<li>U+89F1 CJK UNIFIED IDEOGRAPH-89F1: not included in any glyphset definition</li>
<li>U+89F3 CJK UNIFIED IDEOGRAPH-89F3: not included in any glyphset definition</li>
<li>U+89F6 CJK UNIFIED IDEOGRAPH-89F6: not included in any glyphset definition</li>
<li>U+89FC CJK UNIFIED IDEOGRAPH-89FC: not included in any glyphset definition</li>
<li>U+89FF CJK UNIFIED IDEOGRAPH-89FF: not included in any glyphset definition</li>
<li>U+8A01 CJK UNIFIED IDEOGRAPH-8A01: not included in any glyphset definition</li>
<li>U+8A04 CJK UNIFIED IDEOGRAPH-8A04: not included in any glyphset definition</li>
<li>U+8A07 CJK UNIFIED IDEOGRAPH-8A07: not included in any glyphset definition</li>
<li>U+8A0F CJK UNIFIED IDEOGRAPH-8A0F: not included in any glyphset definition</li>
<li>U+8A11 CJK UNIFIED IDEOGRAPH-8A11: not included in any glyphset definition</li>
<li>U+8A12 CJK UNIFIED IDEOGRAPH-8A12: not included in any glyphset definition</li>
<li>U+8A1A CJK UNIFIED IDEOGRAPH-8A1A: not included in any glyphset definition</li>
<li>U+8A37 CJK UNIFIED IDEOGRAPH-8A37: not included in any glyphset definition</li>
<li>U+8A56 CJK UNIFIED IDEOGRAPH-8A56: not included in any glyphset definition</li>
<li>U+8A57 CJK UNIFIED IDEOGRAPH-8A57: not included in any glyphset definition</li>
<li>U+8A58 CJK UNIFIED IDEOGRAPH-8A58: not included in any glyphset definition</li>
<li>U+8A5D CJK UNIFIED IDEOGRAPH-8A5D: not included in any glyphset definition</li>
<li>U+8A5F CJK UNIFIED IDEOGRAPH-8A5F: not included in any glyphset definition</li>
<li>U+8A68 CJK UNIFIED IDEOGRAPH-8A68: not included in any glyphset definition</li>
<li>U+8A6A CJK UNIFIED IDEOGRAPH-8A6A: not included in any glyphset definition</li>
<li>U+8A75 CJK UNIFIED IDEOGRAPH-8A75: not included in any glyphset definition</li>
<li>U+8A77 CJK UNIFIED IDEOGRAPH-8A77: not included in any glyphset definition</li>
<li>U+8A7B CJK UNIFIED IDEOGRAPH-8A7B: not included in any glyphset definition</li>
<li>U+8A7F CJK UNIFIED IDEOGRAPH-8A7F: not included in any glyphset definition</li>
<li>U+8AA7 CJK UNIFIED IDEOGRAPH-8AA7: not included in any glyphset definition</li>
<li>U+8AB6 CJK UNIFIED IDEOGRAPH-8AB6: not included in any glyphset definition</li>
<li>U+8AD1 CJK UNIFIED IDEOGRAPH-8AD1: not included in any glyphset definition</li>
<li>U+8AD3 CJK UNIFIED IDEOGRAPH-8AD3: not included in any glyphset definition</li>
<li>U+8ADD CJK UNIFIED IDEOGRAPH-8ADD: not included in any glyphset definition</li>
<li>U+8ADF CJK UNIFIED IDEOGRAPH-8ADF: not included in any glyphset definition</li>
<li>U+8AEA CJK UNIFIED IDEOGRAPH-8AEA: not included in any glyphset definition</li>
<li>U+8AF2 CJK UNIFIED IDEOGRAPH-8AF2: not included in any glyphset definition</li>
<li>U+8AF4 CJK UNIFIED IDEOGRAPH-8AF4: not included in any glyphset definition</li>
<li>U+8B0F CJK UNIFIED IDEOGRAPH-8B0F: not included in any glyphset definition</li>
<li>U+8B2E CJK UNIFIED IDEOGRAPH-8B2E: not included in any glyphset definition</li>
<li>U+8B46 CJK UNIFIED IDEOGRAPH-8B46: not included in any glyphset definition</li>
<li>U+8B4A CJK UNIFIED IDEOGRAPH-8B4A: not included in any glyphset definition</li>
<li>U+8B53 CJK UNIFIED IDEOGRAPH-8B53: not included in any glyphset definition</li>
<li>U+8B5E CJK UNIFIED IDEOGRAPH-8B5E: not included in any glyphset definition</li>
<li>U+8B60 CJK UNIFIED IDEOGRAPH-8B60: not included in any glyphset definition</li>
<li>U+8B6A CJK UNIFIED IDEOGRAPH-8B6A: not included in any glyphset definition</li>
<li>U+8B7F CJK UNIFIED IDEOGRAPH-8B7F: not included in any glyphset definition</li>
<li>U+8B8B CJK UNIFIED IDEOGRAPH-8B8B: not included in any glyphset definition</li>
<li>U+8B95 CJK UNIFIED IDEOGRAPH-8B95: not included in any glyphset definition</li>
<li>U+8B9C CJK UNIFIED IDEOGRAPH-8B9C: not included in any glyphset definition</li>
<li>U+8BB1 CJK UNIFIED IDEOGRAPH-8BB1: not included in any glyphset definition</li>
<li>U+8BB5 CJK UNIFIED IDEOGRAPH-8BB5: not included in any glyphset definition</li>
<li>U+8BBB CJK UNIFIED IDEOGRAPH-8BBB: not included in any glyphset definition</li>
<li>U+8BC7 CJK UNIFIED IDEOGRAPH-8BC7: not included in any glyphset definition</li>
<li>U+8BCE CJK UNIFIED IDEOGRAPH-8BCE: not included in any glyphset definition</li>
<li>U+8BD0 CJK UNIFIED IDEOGRAPH-8BD0: not included in any glyphset definition</li>
<li>U+8BD4 CJK UNIFIED IDEOGRAPH-8BD4: not included in any glyphset definition</li>
<li>U+8BD6 CJK UNIFIED IDEOGRAPH-8BD6: not included in any glyphset definition</li>
<li>U+8BDC CJK UNIFIED IDEOGRAPH-8BDC: not included in any glyphset definition</li>
<li>U+8BEE CJK UNIFIED IDEOGRAPH-8BEE: not included in any glyphset definition</li>
<li>U+8BFC CJK UNIFIED IDEOGRAPH-8BFC: not included in any glyphset definition</li>
<li>U+8C07 CJK UNIFIED IDEOGRAPH-8C07: not included in any glyphset definition</li>
<li>U+8C16 CJK UNIFIED IDEOGRAPH-8C16: not included in any glyphset definition</li>
<li>U+8C1D CJK UNIFIED IDEOGRAPH-8C1D: not included in any glyphset definition</li>
<li>U+8C1E CJK UNIFIED IDEOGRAPH-8C1E: not included in any glyphset definition</li>
<li>U+8C20 CJK UNIFIED IDEOGRAPH-8C20: not included in any glyphset definition</li>
<li>U+8C2B CJK UNIFIED IDEOGRAPH-8C2B: not included in any glyphset definition</li>
<li>U+8C2E CJK UNIFIED IDEOGRAPH-8C2E: not included in any glyphset definition</li>
<li>U+8C30 CJK UNIFIED IDEOGRAPH-8C30: not included in any glyphset definition</li>
<li>U+8C33 CJK UNIFIED IDEOGRAPH-8C33: not included in any glyphset definition</li>
<li>U+8C35 CJK UNIFIED IDEOGRAPH-8C35: not included in any glyphset definition</li>
<li>U+8C3C CJK UNIFIED IDEOGRAPH-8C3C: not included in any glyphset definition</li>
<li>U+8C68 CJK UNIFIED IDEOGRAPH-8C68: not included in any glyphset definition</li>
<li>U+8C6D CJK UNIFIED IDEOGRAPH-8C6D: not included in any glyphset definition</li>
<li>U+8C6E CJK UNIFIED IDEOGRAPH-8C6E: not included in any glyphset definition</li>
<li>U+8C73 CJK UNIFIED IDEOGRAPH-8C73: not included in any glyphset definition</li>
<li>U+8C76 CJK UNIFIED IDEOGRAPH-8C76: not included in any glyphset definition</li>
<li>U+8C86 CJK UNIFIED IDEOGRAPH-8C86: not included in any glyphset definition</li>
<li>U+8C99 CJK UNIFIED IDEOGRAPH-8C99: not included in any glyphset definition</li>
<li>U+8CBA CJK UNIFIED IDEOGRAPH-8CBA: not included in any glyphset definition</li>
<li>U+8CD5 CJK UNIFIED IDEOGRAPH-8CD5: not included in any glyphset definition</li>
<li>U+8CD9 CJK UNIFIED IDEOGRAPH-8CD9: not included in any glyphset definition</li>
<li>U+8CE7 CJK UNIFIED IDEOGRAPH-8CE7: not included in any glyphset definition</li>
<li>U+8CEB CJK UNIFIED IDEOGRAPH-8CEB: not included in any glyphset definition</li>
<li>U+8CF0 CJK UNIFIED IDEOGRAPH-8CF0: not included in any glyphset definition</li>
<li>U+8CF1 CJK UNIFIED IDEOGRAPH-8CF1: not included in any glyphset definition</li>
<li>U+8CF5 CJK UNIFIED IDEOGRAPH-8CF5: not included in any glyphset definition</li>
<li>U+8CFE CJK UNIFIED IDEOGRAPH-8CFE: not included in any glyphset definition</li>
<li>U+8D12 CJK UNIFIED IDEOGRAPH-8D12: not included in any glyphset definition</li>
<li>U+8D1C CJK UNIFIED IDEOGRAPH-8D1C: not included in any glyphset definition</li>
<li>U+8D33 CJK UNIFIED IDEOGRAPH-8D33: not included in any glyphset definition</li>
<li>U+8D36 CJK UNIFIED IDEOGRAPH-8D36: not included in any glyphset definition</li>
<li>U+8D40 CJK UNIFIED IDEOGRAPH-8D40: not included in any glyphset definition</li>
<li>U+8D46 CJK UNIFIED IDEOGRAPH-8D46: not included in any glyphset definition</li>
<li>U+8D47 CJK UNIFIED IDEOGRAPH-8D47: not included in any glyphset definition</li>
<li>U+8D4D CJK UNIFIED IDEOGRAPH-8D4D: not included in any glyphset definition</li>
<li>U+8D51 CJK UNIFIED IDEOGRAPH-8D51: not included in any glyphset definition</li>
<li>U+8D52 CJK UNIFIED IDEOGRAPH-8D52: not included in any glyphset definition</li>
<li>U+8D55 CJK UNIFIED IDEOGRAPH-8D55: not included in any glyphset definition</li>
<li>U+8D57 CJK UNIFIED IDEOGRAPH-8D57: not included in any glyphset definition</li>
<li>U+8D59 CJK UNIFIED IDEOGRAPH-8D59: not included in any glyphset definition</li>
<li>U+8D5C CJK UNIFIED IDEOGRAPH-8D5C: not included in any glyphset definition</li>
<li>U+8D6A CJK UNIFIED IDEOGRAPH-8D6A: not included in any glyphset definition</li>
<li>U+8D6C CJK UNIFIED IDEOGRAPH-8D6C: not included in any glyphset definition</li>
<li>U+8D91 CJK UNIFIED IDEOGRAPH-8D91: not included in any glyphset definition</li>
<li>U+8D94 CJK UNIFIED IDEOGRAPH-8D94: not included in any glyphset definition</li>
<li>U+8D96 CJK UNIFIED IDEOGRAPH-8D96: not included in any glyphset definition</li>
<li>U+8DAF CJK UNIFIED IDEOGRAPH-8DAF: not included in any glyphset definition</li>
<li>U+8DB1 CJK UNIFIED IDEOGRAPH-8DB1: not included in any glyphset definition</li>
<li>U+8DB2 CJK UNIFIED IDEOGRAPH-8DB2: not included in any glyphset definition</li>
<li>U+8DBC CJK UNIFIED IDEOGRAPH-8DBC: not included in any glyphset definition</li>
<li>U+8DBF CJK UNIFIED IDEOGRAPH-8DBF: not included in any glyphset definition</li>
<li>U+8DD0 CJK UNIFIED IDEOGRAPH-8DD0: not included in any glyphset definition</li>
<li>U+8DDE CJK UNIFIED IDEOGRAPH-8DDE: not included in any glyphset definition</li>
<li>U+8DE6 CJK UNIFIED IDEOGRAPH-8DE6: not included in any glyphset definition</li>
<li>U+8DF1 CJK UNIFIED IDEOGRAPH-8DF1: not included in any glyphset definition</li>
<li>U+8DF8 CJK UNIFIED IDEOGRAPH-8DF8: not included in any glyphset definition</li>
<li>U+8DFD CJK UNIFIED IDEOGRAPH-8DFD: not included in any glyphset definition</li>
<li>U+8E05 CJK UNIFIED IDEOGRAPH-8E05: not included in any glyphset definition</li>
<li>U+8E0E CJK UNIFIED IDEOGRAPH-8E0E: not included in any glyphset definition</li>
<li>U+8E12 CJK UNIFIED IDEOGRAPH-8E12: not included in any glyphset definition</li>
<li>U+8E14 CJK UNIFIED IDEOGRAPH-8E14: not included in any glyphset definition</li>
<li>U+8E1C CJK UNIFIED IDEOGRAPH-8E1C: not included in any glyphset definition</li>
<li>U+8E21 CJK UNIFIED IDEOGRAPH-8E21: not included in any glyphset definition</li>
<li>U+8E23 CJK UNIFIED IDEOGRAPH-8E23: not included in any glyphset definition</li>
<li>U+8E26 CJK UNIFIED IDEOGRAPH-8E26: not included in any glyphset definition</li>
<li>U+8E2C CJK UNIFIED IDEOGRAPH-8E2C: not included in any glyphset definition</li>
<li>U+8E2D CJK UNIFIED IDEOGRAPH-8E2D: not included in any glyphset definition</li>
<li>U+8E2F CJK UNIFIED IDEOGRAPH-8E2F: not included in any glyphset definition</li>
<li>U+8E36 CJK UNIFIED IDEOGRAPH-8E36: not included in any glyphset definition</li>
<li>U+8E3D CJK UNIFIED IDEOGRAPH-8E3D: not included in any glyphset definition</li>
<li>U+8E40 CJK UNIFIED IDEOGRAPH-8E40: not included in any glyphset definition</li>
<li>U+8E41 CJK UNIFIED IDEOGRAPH-8E41: not included in any glyphset definition</li>
<li>U+8E45 CJK UNIFIED IDEOGRAPH-8E45: not included in any glyphset definition</li>
<li>U+8E54 CJK UNIFIED IDEOGRAPH-8E54: not included in any glyphset definition</li>
<li>U+8E5A CJK UNIFIED IDEOGRAPH-8E5A: not included in any glyphset definition</li>
<li>U+8E5C CJK UNIFIED IDEOGRAPH-8E5C: not included in any glyphset definition</li>
<li>U+8E62 CJK UNIFIED IDEOGRAPH-8E62: not included in any glyphset definition</li>
<li>U+8E67 CJK UNIFIED IDEOGRAPH-8E67: not included in any glyphset definition</li>
<li>U+8E6F CJK UNIFIED IDEOGRAPH-8E6F: not included in any glyphset definition</li>
<li>U+8E70 CJK UNIFIED IDEOGRAPH-8E70: not included in any glyphset definition</li>
<li>U+8E7B CJK UNIFIED IDEOGRAPH-8E7B: not included in any glyphset definition</li>
<li>U+8E7D CJK UNIFIED IDEOGRAPH-8E7D: not included in any glyphset definition</li>
<li>U+8E90 CJK UNIFIED IDEOGRAPH-8E90: not included in any glyphset definition</li>
<li>U+8E92 CJK UNIFIED IDEOGRAPH-8E92: not included in any glyphset definition</li>
<li>U+8E95 CJK UNIFIED IDEOGRAPH-8E95: not included in any glyphset definition</li>
<li>U+8E9A CJK UNIFIED IDEOGRAPH-8E9A: not included in any glyphset definition</li>
<li>U+8E9C CJK UNIFIED IDEOGRAPH-8E9C: not included in any glyphset definition</li>
<li>U+8E9E CJK UNIFIED IDEOGRAPH-8E9E: not included in any glyphset definition</li>
<li>U+8EA6 CJK UNIFIED IDEOGRAPH-8EA6: not included in any glyphset definition</li>
<li>U+8EAD CJK UNIFIED IDEOGRAPH-8EAD: not included in any glyphset definition</li>
<li>U+8ECF CJK UNIFIED IDEOGRAPH-8ECF: not included in any glyphset definition</li>
<li>U+8ED1 CJK UNIFIED IDEOGRAPH-8ED1: not included in any glyphset definition</li>
<li>U+8EDA CJK UNIFIED IDEOGRAPH-8EDA: not included in any glyphset definition</li>
<li>U+8EDD CJK UNIFIED IDEOGRAPH-8EDD: not included in any glyphset definition</li>
<li>U+8EF2 CJK UNIFIED IDEOGRAPH-8EF2: not included in any glyphset definition</li>
<li>U+8EF9 CJK UNIFIED IDEOGRAPH-8EF9: not included in any glyphset definition</li>
<li>U+8EFA CJK UNIFIED IDEOGRAPH-8EFA: not included in any glyphset definition</li>
<li>U+8F04 CJK UNIFIED IDEOGRAPH-8F04: not included in any glyphset definition</li>
<li>U+8F07 CJK UNIFIED IDEOGRAPH-8F07: not included in any glyphset definition</li>
<li>U+8F08 CJK UNIFIED IDEOGRAPH-8F08: not included in any glyphset definition</li>
<li>U+8F17 CJK UNIFIED IDEOGRAPH-8F17: not included in any glyphset definition</li>
<li>U+8F1E CJK UNIFIED IDEOGRAPH-8F1E: not included in any glyphset definition</li>
<li>U+8F27 CJK UNIFIED IDEOGRAPH-8F27: not included in any glyphset definition</li>
<li>U+8F2C CJK UNIFIED IDEOGRAPH-8F2C: not included in any glyphset definition</li>
<li>U+8F2D CJK UNIFIED IDEOGRAPH-8F2D: not included in any glyphset definition</li>
<li>U+8F2E CJK UNIFIED IDEOGRAPH-8F2E: not included in any glyphset definition</li>
<li>U+8F36 CJK UNIFIED IDEOGRAPH-8F36: not included in any glyphset definition</li>
<li>U+8F40 CJK UNIFIED IDEOGRAPH-8F40: not included in any glyphset definition</li>
<li>U+8F54 CJK UNIFIED IDEOGRAPH-8F54: not included in any glyphset definition</li>
<li>U+8F5D CJK UNIFIED IDEOGRAPH-8F5D: not included in any glyphset definition</li>
<li>U+8F6A CJK UNIFIED IDEOGRAPH-8F6A: not included in any glyphset definition</li>
<li>U+8F73 CJK UNIFIED IDEOGRAPH-8F73: not included in any glyphset definition</li>
<li>U+8F75 CJK UNIFIED IDEOGRAPH-8F75: not included in any glyphset definition</li>
<li>U+8F77 CJK UNIFIED IDEOGRAPH-8F77: not included in any glyphset definition</li>
<li>U+8F79 CJK UNIFIED IDEOGRAPH-8F79: not included in any glyphset definition</li>
<li>U+8F7A CJK UNIFIED IDEOGRAPH-8F7A: not included in any glyphset definition</li>
<li>U+8F7E CJK UNIFIED IDEOGRAPH-8F7E: not included in any glyphset definition</li>
<li>U+8F80 CJK UNIFIED IDEOGRAPH-8F80: not included in any glyphset definition</li>
<li>U+8F81 CJK UNIFIED IDEOGRAPH-8F81: not included in any glyphset definition</li>
<li>U+8F82 CJK UNIFIED IDEOGRAPH-8F82: not included in any glyphset definition</li>
<li>U+8F8C CJK UNIFIED IDEOGRAPH-8F8C: not included in any glyphset definition</li>
<li>U+8F8E CJK UNIFIED IDEOGRAPH-8F8E: not included in any glyphset definition</li>
<li>U+8F8F CJK UNIFIED IDEOGRAPH-8F8F: not included in any glyphset definition</li>
<li>U+8F92 CJK UNIFIED IDEOGRAPH-8F92: not included in any glyphset definition</li>
<li>U+8F9A CJK UNIFIED IDEOGRAPH-8F9A: not included in any glyphset definition</li>
<li>U+8FB5 CJK UNIFIED IDEOGRAPH-8FB5: not included in any glyphset definition</li>
<li>U+8FB6 CJK UNIFIED IDEOGRAPH-8FB6: not included in any glyphset definition</li>
<li>U+8FC6 CJK UNIFIED IDEOGRAPH-8FC6: not included in any glyphset definition</li>
<li>U+8FD5 CJK UNIFIED IDEOGRAPH-8FD5: not included in any glyphset definition</li>
<li>U+8FEE CJK UNIFIED IDEOGRAPH-8FEE: not included in any glyphset definition</li>
<li>U+8FF2 CJK UNIFIED IDEOGRAPH-8FF2: not included in any glyphset definition</li>
<li>U+9008 CJK UNIFIED IDEOGRAPH-9008: not included in any glyphset definition</li>
<li>U+902D CJK UNIFIED IDEOGRAPH-902D: not included in any glyphset definition</li>
<li>U+9034 CJK UNIFIED IDEOGRAPH-9034: not included in any glyphset definition</li>
<li>U+9044 CJK UNIFIED IDEOGRAPH-9044: not included in any glyphset definition</li>
<li>U+905D CJK UNIFIED IDEOGRAPH-905D: not included in any glyphset definition</li>
<li>U+9067 CJK UNIFIED IDEOGRAPH-9067: not included in any glyphset definition</li>
<li>U+9079 CJK UNIFIED IDEOGRAPH-9079: not included in any glyphset definition</li>
<li>U+9098 CJK UNIFIED IDEOGRAPH-9098: not included in any glyphset definition</li>
<li>U+90A0 CJK UNIFIED IDEOGRAPH-90A0: not included in any glyphset definition</li>
<li>U+90B2 CJK UNIFIED IDEOGRAPH-90B2: not included in any glyphset definition</li>
<li>U+90B4 CJK UNIFIED IDEOGRAPH-90B4: not included in any glyphset definition</li>
<li>U+90B6 CJK UNIFIED IDEOGRAPH-90B6: not included in any glyphset definition</li>
<li>U+90BD CJK UNIFIED IDEOGRAPH-90BD: not included in any glyphset definition</li>
<li>U+90BE CJK UNIFIED IDEOGRAPH-90BE: not included in any glyphset definition</li>
<li>U+90BF CJK UNIFIED IDEOGRAPH-90BF: not included in any glyphset definition</li>
<li>U+90C8 CJK UNIFIED IDEOGRAPH-90C8: not included in any glyphset definition</li>
<li>U+90D0 CJK UNIFIED IDEOGRAPH-90D0: not included in any glyphset definition</li>
<li>U+90DA CJK UNIFIED IDEOGRAPH-90DA: not included in any glyphset definition</li>
<li>U+90DF CJK UNIFIED IDEOGRAPH-90DF: not included in any glyphset definition</li>
<li>U+90EA CJK UNIFIED IDEOGRAPH-90EA: not included in any glyphset definition</li>
<li>U+90FF CJK UNIFIED IDEOGRAPH-90FF: not included in any glyphset definition</li>
<li>U+9100 CJK UNIFIED IDEOGRAPH-9100: not included in any glyphset definition</li>
<li>U+9103 CJK UNIFIED IDEOGRAPH-9103: not included in any glyphset definition</li>
<li>U+9105 CJK UNIFIED IDEOGRAPH-9105: not included in any glyphset definition</li>
<li>U+9106 CJK UNIFIED IDEOGRAPH-9106: not included in any glyphset definition</li>
<li>U+910C CJK UNIFIED IDEOGRAPH-910C: not included in any glyphset definition</li>
<li>U+9111 CJK UNIFIED IDEOGRAPH-9111: not included in any glyphset definition</li>
<li>U+9115 CJK UNIFIED IDEOGRAPH-9115: not included in any glyphset definition</li>
<li>U+9116 CJK UNIFIED IDEOGRAPH-9116: not included in any glyphset definition</li>
<li>U+9117 CJK UNIFIED IDEOGRAPH-9117: not included in any glyphset definition</li>
<li>U+9118 CJK UNIFIED IDEOGRAPH-9118: not included in any glyphset definition</li>
<li>U+911A CJK UNIFIED IDEOGRAPH-911A: not included in any glyphset definition</li>
<li>U+911C CJK UNIFIED IDEOGRAPH-911C: not included in any glyphset definition</li>
<li>U+9123 CJK UNIFIED IDEOGRAPH-9123: not included in any glyphset definition</li>
<li>U+9129 CJK UNIFIED IDEOGRAPH-9129: not included in any glyphset definition</li>
<li>U+912B CJK UNIFIED IDEOGRAPH-912B: not included in any glyphset definition</li>
<li>U+9133 CJK UNIFIED IDEOGRAPH-9133: not included in any glyphset definition</li>
<li>U+9136 CJK UNIFIED IDEOGRAPH-9136: not included in any glyphset definition</li>
<li>U+9139 CJK UNIFIED IDEOGRAPH-9139: not included in any glyphset definition</li>
<li>U+9142 CJK UNIFIED IDEOGRAPH-9142: not included in any glyphset definition</li>
<li>U+9143 CJK UNIFIED IDEOGRAPH-9143: not included in any glyphset definition</li>
<li>U+9145 CJK UNIFIED IDEOGRAPH-9145: not included in any glyphset definition</li>
<li>U+9147 CJK UNIFIED IDEOGRAPH-9147: not included in any glyphset definition</li>
<li>U+914F CJK UNIFIED IDEOGRAPH-914F: not included in any glyphset definition</li>
<li>U+9161 CJK UNIFIED IDEOGRAPH-9161: not included in any glyphset definition</li>
<li>U+9164 CJK UNIFIED IDEOGRAPH-9164: not included in any glyphset definition</li>
<li>U+9166 CJK UNIFIED IDEOGRAPH-9166: not included in any glyphset definition</li>
<li>U+9174 CJK UNIFIED IDEOGRAPH-9174: not included in any glyphset definition</li>
<li>U+9179 CJK UNIFIED IDEOGRAPH-9179: not included in any glyphset definition</li>
<li>U+917A CJK UNIFIED IDEOGRAPH-917A: not included in any glyphset definition</li>
<li>U+917D CJK UNIFIED IDEOGRAPH-917D: not included in any glyphset definition</li>
<li>U+917E CJK UNIFIED IDEOGRAPH-917E: not included in any glyphset definition</li>
<li>U+9185 CJK UNIFIED IDEOGRAPH-9185: not included in any glyphset definition</li>
<li>U+9191 CJK UNIFIED IDEOGRAPH-9191: not included in any glyphset definition</li>
<li>U+9196 CJK UNIFIED IDEOGRAPH-9196: not included in any glyphset definition</li>
<li>U+91A8 CJK UNIFIED IDEOGRAPH-91A8: not included in any glyphset definition</li>
<li>U+91AD CJK UNIFIED IDEOGRAPH-91AD: not included in any glyphset definition</li>
<li>U+91B2 CJK UNIFIED IDEOGRAPH-91B2: not included in any glyphset definition</li>
<li>U+91BE CJK UNIFIED IDEOGRAPH-91BE: not included in any glyphset definition</li>
<li>U+91C3 CJK UNIFIED IDEOGRAPH-91C3: not included in any glyphset definition</li>
<li>U+91C5 CJK UNIFIED IDEOGRAPH-91C5: not included in any glyphset definition</li>
<li>U+91D2 CJK UNIFIED IDEOGRAPH-91D2: not included in any glyphset definition</li>
<li>U+91D3 CJK UNIFIED IDEOGRAPH-91D3: not included in any glyphset definition</li>
<li>U+91D5 CJK UNIFIED IDEOGRAPH-91D5: not included in any glyphset definition</li>
<li>U+91D9 CJK UNIFIED IDEOGRAPH-91D9: not included in any glyphset definition</li>
<li>U+91DA CJK UNIFIED IDEOGRAPH-91DA: not included in any glyphset definition</li>
<li>U+91DE CJK UNIFIED IDEOGRAPH-91DE: not included in any glyphset definition</li>
<li>U+91EA CJK UNIFIED IDEOGRAPH-91EA: not included in any glyphset definition</li>
<li>U+91ED CJK UNIFIED IDEOGRAPH-91ED: not included in any glyphset definition</li>
<li>U+91EE CJK UNIFIED IDEOGRAPH-91EE: not included in any glyphset definition</li>
<li>U+91F4 CJK UNIFIED IDEOGRAPH-91F4: not included in any glyphset definition</li>
<li>U+91FA CJK UNIFIED IDEOGRAPH-91FA: not included in any glyphset definition</li>
<li>U+9201 CJK UNIFIED IDEOGRAPH-9201: not included in any glyphset definition</li>
<li>U+9203 CJK UNIFIED IDEOGRAPH-9203: not included in any glyphset definition</li>
<li>U+9204 CJK UNIFIED IDEOGRAPH-9204: not included in any glyphset definition</li>
<li>U+9206 CJK UNIFIED IDEOGRAPH-9206: not included in any glyphset definition</li>
<li>U+9207 CJK UNIFIED IDEOGRAPH-9207: not included in any glyphset definition</li>
<li>U+9208 CJK UNIFIED IDEOGRAPH-9208: not included in any glyphset definition</li>
<li>U+9212 CJK UNIFIED IDEOGRAPH-9212: not included in any glyphset definition</li>
<li>U+9217 CJK UNIFIED IDEOGRAPH-9217: not included in any glyphset definition</li>
<li>U+9227 CJK UNIFIED IDEOGRAPH-9227: not included in any glyphset definition</li>
<li>U+922A CJK UNIFIED IDEOGRAPH-922A: not included in any glyphset definition</li>
<li>U+9230 CJK UNIFIED IDEOGRAPH-9230: not included in any glyphset definition</li>
<li>U+9233 CJK UNIFIED IDEOGRAPH-9233: not included in any glyphset definition</li>
<li>U+923D CJK UNIFIED IDEOGRAPH-923D: not included in any glyphset definition</li>
<li>U+924A CJK UNIFIED IDEOGRAPH-924A: not included in any glyphset definition</li>
<li>U+924D CJK UNIFIED IDEOGRAPH-924D: not included in any glyphset definition</li>
<li>U+924E CJK UNIFIED IDEOGRAPH-924E: not included in any glyphset definition</li>
<li>U+9259 CJK UNIFIED IDEOGRAPH-9259: not included in any glyphset definition</li>
<li>U+925D CJK UNIFIED IDEOGRAPH-925D: not included in any glyphset definition</li>
<li>U+9265 CJK UNIFIED IDEOGRAPH-9265: not included in any glyphset definition</li>
<li>U+9267 CJK UNIFIED IDEOGRAPH-9267: not included in any glyphset definition</li>
<li>U+9268 CJK UNIFIED IDEOGRAPH-9268: not included in any glyphset definition</li>
<li>U+9272 CJK UNIFIED IDEOGRAPH-9272: not included in any glyphset definition</li>
<li>U+9273 CJK UNIFIED IDEOGRAPH-9273: not included in any glyphset definition</li>
<li>U+9276 CJK UNIFIED IDEOGRAPH-9276: not included in any glyphset definition</li>
<li>U+927A CJK UNIFIED IDEOGRAPH-927A: not included in any glyphset definition</li>
<li>U+927C CJK UNIFIED IDEOGRAPH-927C: not included in any glyphset definition</li>
<li>U+927F CJK UNIFIED IDEOGRAPH-927F: not included in any glyphset definition</li>
<li>U+9288 CJK UNIFIED IDEOGRAPH-9288: not included in any glyphset definition</li>
<li>U+928A CJK UNIFIED IDEOGRAPH-928A: not included in any glyphset definition</li>
<li>U+928D CJK UNIFIED IDEOGRAPH-928D: not included in any glyphset definition</li>
<li>U+928E CJK UNIFIED IDEOGRAPH-928E: not included in any glyphset definition</li>
<li>U+92A9 CJK UNIFIED IDEOGRAPH-92A9: not included in any glyphset definition</li>
<li>U+92AA CJK UNIFIED IDEOGRAPH-92AA: not included in any glyphset definition</li>
<li>U+92AB CJK UNIFIED IDEOGRAPH-92AB: not included in any glyphset definition</li>
<li>U+92B6 CJK UNIFIED IDEOGRAPH-92B6: not included in any glyphset definition</li>
<li>U+92C2 CJK UNIFIED IDEOGRAPH-92C2: not included in any glyphset definition</li>
<li>U+92C8 CJK UNIFIED IDEOGRAPH-92C8: not included in any glyphset definition</li>
<li>U+92C9 CJK UNIFIED IDEOGRAPH-92C9: not included in any glyphset definition</li>
<li>U+92D3 CJK UNIFIED IDEOGRAPH-92D3: not included in any glyphset definition</li>
<li>U+92D7 CJK UNIFIED IDEOGRAPH-92D7: not included in any glyphset definition</li>
<li>U+92D9 CJK UNIFIED IDEOGRAPH-92D9: not included in any glyphset definition</li>
<li>U+92DD CJK UNIFIED IDEOGRAPH-92DD: not included in any glyphset definition</li>
<li>U+92DF CJK UNIFIED IDEOGRAPH-92DF: not included in any glyphset definition</li>
<li>U+92E0 CJK UNIFIED IDEOGRAPH-92E0: not included in any glyphset definition</li>
<li>U+92E5 CJK UNIFIED IDEOGRAPH-92E5: not included in any glyphset definition</li>
<li>U+92E6 CJK UNIFIED IDEOGRAPH-92E6: not included in any glyphset definition</li>
<li>U+92E7 CJK UNIFIED IDEOGRAPH-92E7: not included in any glyphset definition</li>
<li>U+92E8 CJK UNIFIED IDEOGRAPH-92E8: not included in any glyphset definition</li>
<li>U+92F1 CJK UNIFIED IDEOGRAPH-92F1: not included in any glyphset definition</li>
<li>U+92F6 CJK UNIFIED IDEOGRAPH-92F6: not included in any glyphset definition</li>
<li>U+92F9 CJK UNIFIED IDEOGRAPH-92F9: not included in any glyphset definition</li>
<li>U+92FB CJK UNIFIED IDEOGRAPH-92FB: not included in any glyphset definition</li>
<li>U+92FF CJK UNIFIED IDEOGRAPH-92FF: not included in any glyphset definition</li>
<li>U+9300 CJK UNIFIED IDEOGRAPH-9300: not included in any glyphset definition</li>
<li>U+9301 CJK UNIFIED IDEOGRAPH-9301: not included in any glyphset definition</li>
<li>U+9302 CJK UNIFIED IDEOGRAPH-9302: not included in any glyphset definition</li>
<li>U+9308 CJK UNIFIED IDEOGRAPH-9308: not included in any glyphset definition</li>
<li>U+931B CJK UNIFIED IDEOGRAPH-931B: not included in any glyphset definition</li>
<li>U+931D CJK UNIFIED IDEOGRAPH-931D: not included in any glyphset definition</li>
<li>U+931F CJK UNIFIED IDEOGRAPH-931F: not included in any glyphset definition</li>
<li>U+9325 CJK UNIFIED IDEOGRAPH-9325: not included in any glyphset definition</li>
<li>U+9327 CJK UNIFIED IDEOGRAPH-9327: not included in any glyphset definition</li>
<li>U+933C CJK UNIFIED IDEOGRAPH-933C: not included in any glyphset definition</li>
<li>U+9340 CJK UNIFIED IDEOGRAPH-9340: not included in any glyphset definition</li>
<li>U+9341 CJK UNIFIED IDEOGRAPH-9341: not included in any glyphset definition</li>
<li>U+9345 CJK UNIFIED IDEOGRAPH-9345: not included in any glyphset definition</li>
<li>U+9346 CJK UNIFIED IDEOGRAPH-9346: not included in any glyphset definition</li>
<li>U+9348 CJK UNIFIED IDEOGRAPH-9348: not included in any glyphset definition</li>
<li>U+9364 CJK UNIFIED IDEOGRAPH-9364: not included in any glyphset definition</li>
<li>U+936A CJK UNIFIED IDEOGRAPH-936A: not included in any glyphset definition</li>
<li>U+936D CJK UNIFIED IDEOGRAPH-936D: not included in any glyphset definition</li>
<li>U+9387 CJK UNIFIED IDEOGRAPH-9387: not included in any glyphset definition</li>
<li>U+9393 CJK UNIFIED IDEOGRAPH-9393: not included in any glyphset definition</li>
<li>U+939B CJK UNIFIED IDEOGRAPH-939B: not included in any glyphset definition</li>
<li>U+939D CJK UNIFIED IDEOGRAPH-939D: not included in any glyphset definition</li>
<li>U+93A1 CJK UNIFIED IDEOGRAPH-93A1: not included in any glyphset definition</li>
<li>U+93A3 CJK UNIFIED IDEOGRAPH-93A3: not included in any glyphset definition</li>
<li>U+93A4 CJK UNIFIED IDEOGRAPH-93A4: not included in any glyphset definition</li>
<li>U+93A6 CJK UNIFIED IDEOGRAPH-93A6: not included in any glyphset definition</li>
<li>U+93AA CJK UNIFIED IDEOGRAPH-93AA: not included in any glyphset definition</li>
<li>U+93B2 CJK UNIFIED IDEOGRAPH-93B2: not included in any glyphset definition</li>
<li>U+93CA CJK UNIFIED IDEOGRAPH-93CA: not included in any glyphset definition</li>
<li>U+93CF CJK UNIFIED IDEOGRAPH-93CF: not included in any glyphset definition</li>
<li>U+93F0 CJK UNIFIED IDEOGRAPH-93F0: not included in any glyphset definition</li>
<li>U+93F6 CJK UNIFIED IDEOGRAPH-93F6: not included in any glyphset definition</li>
<li>U+93F7 CJK UNIFIED IDEOGRAPH-93F7: not included in any glyphset definition</li>
<li>U+93F8 CJK UNIFIED IDEOGRAPH-93F8: not included in any glyphset definition</li>
<li>U+93FA CJK UNIFIED IDEOGRAPH-93FA: not included in any glyphset definition</li>
<li>U+93FB CJK UNIFIED IDEOGRAPH-93FB: not included in any glyphset definition</li>
<li>U+940B CJK UNIFIED IDEOGRAPH-940B: not included in any glyphset definition</li>
<li>U+940D CJK UNIFIED IDEOGRAPH-940D: not included in any glyphset definition</li>
<li>U+940F CJK UNIFIED IDEOGRAPH-940F: not included in any glyphset definition</li>
<li>U+9412 CJK UNIFIED IDEOGRAPH-9412: not included in any glyphset definition</li>
<li>U+9420 CJK UNIFIED IDEOGRAPH-9420: not included in any glyphset definition</li>
<li>U+9425 CJK UNIFIED IDEOGRAPH-9425: not included in any glyphset definition</li>
<li>U+9431 CJK UNIFIED IDEOGRAPH-9431: not included in any glyphset definition</li>
<li>U+943D CJK UNIFIED IDEOGRAPH-943D: not included in any glyphset definition</li>
<li>U+9440 CJK UNIFIED IDEOGRAPH-9440: not included in any glyphset definition</li>
<li>U+9445 CJK UNIFIED IDEOGRAPH-9445: not included in any glyphset definition</li>
<li>U+9448 CJK UNIFIED IDEOGRAPH-9448: not included in any glyphset definition</li>
<li>U+9454 CJK UNIFIED IDEOGRAPH-9454: not included in any glyphset definition</li>
<li>U+9455 CJK UNIFIED IDEOGRAPH-9455: not included in any glyphset definition</li>
<li>U+9464 CJK UNIFIED IDEOGRAPH-9464: not included in any glyphset definition</li>
<li>U+9482 CJK UNIFIED IDEOGRAPH-9482: not included in any glyphset definition</li>
<li>U+9486 CJK UNIFIED IDEOGRAPH-9486: not included in any glyphset definition</li>
<li>U+948B CJK UNIFIED IDEOGRAPH-948B: not included in any glyphset definition</li>
<li>U+948C CJK UNIFIED IDEOGRAPH-948C: not included in any glyphset definition</li>
<li>U+948D CJK UNIFIED IDEOGRAPH-948D: not included in any glyphset definition</li>
<li>U+9490 CJK UNIFIED IDEOGRAPH-9490: not included in any glyphset definition</li>
<li>U+9494 CJK UNIFIED IDEOGRAPH-9494: not included in any glyphset definition</li>
<li>U+9496 CJK UNIFIED IDEOGRAPH-9496: not included in any glyphset definition</li>
<li>U+9498 CJK UNIFIED IDEOGRAPH-9498: not included in any glyphset definition</li>
<li>U+949A CJK UNIFIED IDEOGRAPH-949A: not included in any glyphset definition</li>
<li>U+94AA CJK UNIFIED IDEOGRAPH-94AA: not included in any glyphset definition</li>
<li>U+94AB CJK UNIFIED IDEOGRAPH-94AB: not included in any glyphset definition</li>
<li>U+94AD CJK UNIFIED IDEOGRAPH-94AD: not included in any glyphset definition</li>
<li>U+94B2 CJK UNIFIED IDEOGRAPH-94B2: not included in any glyphset definition</li>
<li>U+94B6 CJK UNIFIED IDEOGRAPH-94B6: not included in any glyphset definition</li>
<li>U+94B7 CJK UNIFIED IDEOGRAPH-94B7: not included in any glyphset definition</li>
<li>U+94B8 CJK UNIFIED IDEOGRAPH-94B8: not included in any glyphset definition</li>
<li>U+94CA CJK UNIFIED IDEOGRAPH-94CA: not included in any glyphset definition</li>
<li>U+94CF CJK UNIFIED IDEOGRAPH-94CF: not included in any glyphset definition</li>
<li>U+94D2 CJK UNIFIED IDEOGRAPH-94D2: not included in any glyphset definition</li>
<li>U+94D3 CJK UNIFIED IDEOGRAPH-94D3: not included in any glyphset definition</li>
<li>U+94D5 CJK UNIFIED IDEOGRAPH-94D5: not included in any glyphset definition</li>
<li>U+94D7 CJK UNIFIED IDEOGRAPH-94D7: not included in any glyphset definition</li>
<li>U+94D8 CJK UNIFIED IDEOGRAPH-94D8: not included in any glyphset definition</li>
<li>U+94D9 CJK UNIFIED IDEOGRAPH-94D9: not included in any glyphset definition</li>
<li>U+94DA CJK UNIFIED IDEOGRAPH-94DA: not included in any glyphset definition</li>
<li>U+94DE CJK UNIFIED IDEOGRAPH-94DE: not included in any glyphset definition</li>
<li>U+94E5 CJK UNIFIED IDEOGRAPH-94E5: not included in any glyphset definition</li>
<li>U+94EA CJK UNIFIED IDEOGRAPH-94EA: not included in any glyphset definition</li>
<li>U+94EB CJK UNIFIED IDEOGRAPH-94EB: not included in any glyphset definition</li>
<li>U+94F4 CJK UNIFIED IDEOGRAPH-94F4: not included in any glyphset definition</li>
<li>U+94F7 CJK UNIFIED IDEOGRAPH-94F7: not included in any glyphset definition</li>
<li>U+94F9 CJK UNIFIED IDEOGRAPH-94F9: not included in any glyphset definition</li>
<li>U+94FB CJK UNIFIED IDEOGRAPH-94FB: not included in any glyphset definition</li>
<li>U+94FC CJK UNIFIED IDEOGRAPH-94FC: not included in any glyphset definition</li>
<li>U+94FD CJK UNIFIED IDEOGRAPH-94FD: not included in any glyphset definition</li>
<li>U+9507 CJK UNIFIED IDEOGRAPH-9507: not included in any glyphset definition</li>
<li>U+950A CJK UNIFIED IDEOGRAPH-950A: not included in any glyphset definition</li>
<li>U+950D CJK UNIFIED IDEOGRAPH-950D: not included in any glyphset definition</li>
<li>U+950E CJK UNIFIED IDEOGRAPH-950E: not included in any glyphset definition</li>
<li>U+9513 CJK UNIFIED IDEOGRAPH-9513: not included in any glyphset definition</li>
<li>U+9514 CJK UNIFIED IDEOGRAPH-9514: not included in any glyphset definition</li>
<li>U+9515 CJK UNIFIED IDEOGRAPH-9515: not included in any glyphset definition</li>
<li>U+9516 CJK UNIFIED IDEOGRAPH-9516: not included in any glyphset definition</li>
<li>U+951C CJK UNIFIED IDEOGRAPH-951C: not included in any glyphset definition</li>
<li>U+951E CJK UNIFIED IDEOGRAPH-951E: not included in any glyphset definition</li>
<li>U+9527 CJK UNIFIED IDEOGRAPH-9527: not included in any glyphset definition</li>
<li>U+9528 CJK UNIFIED IDEOGRAPH-9528: not included in any glyphset definition</li>
<li>U+9529 CJK UNIFIED IDEOGRAPH-9529: not included in any glyphset definition</li>
<li>U+952A CJK UNIFIED IDEOGRAPH-952A: not included in any glyphset definition</li>
<li>U+952B CJK UNIFIED IDEOGRAPH-952B: not included in any glyphset definition</li>
<li>U+952C CJK UNIFIED IDEOGRAPH-952C: not included in any glyphset definition</li>
<li>U+9531 CJK UNIFIED IDEOGRAPH-9531: not included in any glyphset definition</li>
<li>U+9533 CJK UNIFIED IDEOGRAPH-9533: not included in any glyphset definition</li>
<li>U+9538 CJK UNIFIED IDEOGRAPH-9538: not included in any glyphset definition</li>
<li>U+953C CJK UNIFIED IDEOGRAPH-953C: not included in any glyphset definition</li>
<li>U+953D CJK UNIFIED IDEOGRAPH-953D: not included in any glyphset definition</li>
<li>U+953E CJK UNIFIED IDEOGRAPH-953E: not included in any glyphset definition</li>
<li>U+953F CJK UNIFIED IDEOGRAPH-953F: not included in any glyphset definition</li>
<li>U+9543 CJK UNIFIED IDEOGRAPH-9543: not included in any glyphset definition</li>
<li>U+9544 CJK UNIFIED IDEOGRAPH-9544: not included in any glyphset definition</li>
<li>U+9545 CJK UNIFIED IDEOGRAPH-9545: not included in any glyphset definition</li>
<li>U+9546 CJK UNIFIED IDEOGRAPH-9546: not included in any glyphset definition</li>
<li>U+9548 CJK UNIFIED IDEOGRAPH-9548: not included in any glyphset definition</li>
<li>U+954B CJK UNIFIED IDEOGRAPH-954B: not included in any glyphset definition</li>
<li>U+954E CJK UNIFIED IDEOGRAPH-954E: not included in any glyphset definition</li>
<li>U+954F CJK UNIFIED IDEOGRAPH-954F: not included in any glyphset definition</li>
<li>U+9558 CJK UNIFIED IDEOGRAPH-9558: not included in any glyphset definition</li>
<li>U+9559 CJK UNIFIED IDEOGRAPH-9559: not included in any glyphset definition</li>
<li>U+955A CJK UNIFIED IDEOGRAPH-955A: not included in any glyphset definition</li>
<li>U+955E CJK UNIFIED IDEOGRAPH-955E: not included in any glyphset definition</li>
<li>U+955F CJK UNIFIED IDEOGRAPH-955F: not included in any glyphset definition</li>
<li>U+9560 CJK UNIFIED IDEOGRAPH-9560: not included in any glyphset definition</li>
<li>U+9561 CJK UNIFIED IDEOGRAPH-9561: not included in any glyphset definition</li>
<li>U+9562 CJK UNIFIED IDEOGRAPH-9562: not included in any glyphset definition</li>
<li>U+9564 CJK UNIFIED IDEOGRAPH-9564: not included in any glyphset definition</li>
<li>U+9565 CJK UNIFIED IDEOGRAPH-9565: not included in any glyphset definition</li>
<li>U+9568 CJK UNIFIED IDEOGRAPH-9568: not included in any glyphset definition</li>
<li>U+9569 CJK UNIFIED IDEOGRAPH-9569: not included in any glyphset definition</li>
<li>U+956A CJK UNIFIED IDEOGRAPH-956A: not included in any glyphset definition</li>
<li>U+956E CJK UNIFIED IDEOGRAPH-956E: not included in any glyphset definition</li>
<li>U+9571 CJK UNIFIED IDEOGRAPH-9571: not included in any glyphset definition</li>
<li>U+9572 CJK UNIFIED IDEOGRAPH-9572: not included in any glyphset definition</li>
<li>U+9574 CJK UNIFIED IDEOGRAPH-9574: not included in any glyphset definition</li>
<li>U+9575 CJK UNIFIED IDEOGRAPH-9575: not included in any glyphset definition</li>
<li>U+958C CJK UNIFIED IDEOGRAPH-958C: not included in any glyphset definition</li>
<li>U+95AA CJK UNIFIED IDEOGRAPH-95AA: not included in any glyphset definition</li>
<li>U+95B6 CJK UNIFIED IDEOGRAPH-95B6: not included in any glyphset definition</li>
<li>U+95BD CJK UNIFIED IDEOGRAPH-95BD: not included in any glyphset definition</li>
<li>U+95C9 CJK UNIFIED IDEOGRAPH-95C9: not included in any glyphset definition</li>
<li>U+95D1 CJK UNIFIED IDEOGRAPH-95D1: not included in any glyphset definition</li>
<li>U+95D2 CJK UNIFIED IDEOGRAPH-95D2: not included in any glyphset definition</li>
<li>U+95D3 CJK UNIFIED IDEOGRAPH-95D3: not included in any glyphset definition</li>
<li>U+95F6 CJK UNIFIED IDEOGRAPH-95F6: not included in any glyphset definition</li>
<li>U+95FC CJK UNIFIED IDEOGRAPH-95FC: not included in any glyphset definition</li>
<li>U+95FF CJK UNIFIED IDEOGRAPH-95FF: not included in any glyphset definition</li>
<li>U+9603 CJK UNIFIED IDEOGRAPH-9603: not included in any glyphset definition</li>
<li>U+9604 CJK UNIFIED IDEOGRAPH-9604: not included in any glyphset definition</li>
<li>U+9607 CJK UNIFIED IDEOGRAPH-9607: not included in any glyphset definition</li>
<li>U+960B CJK UNIFIED IDEOGRAPH-960B: not included in any glyphset definition</li>
<li>U+960C CJK UNIFIED IDEOGRAPH-960C: not included in any glyphset definition</li>
<li>U+960D CJK UNIFIED IDEOGRAPH-960D: not included in any glyphset definition</li>
<li>U+960F CJK UNIFIED IDEOGRAPH-960F: not included in any glyphset definition</li>
<li>U+9612 CJK UNIFIED IDEOGRAPH-9612: not included in any glyphset definition</li>
<li>U+9618 CJK UNIFIED IDEOGRAPH-9618: not included in any glyphset definition</li>
<li>U+961D CJK UNIFIED IDEOGRAPH-961D: not included in any glyphset definition</li>
<li>U+9622 CJK UNIFIED IDEOGRAPH-9622: not included in any glyphset definition</li>
<li>U+962C CJK UNIFIED IDEOGRAPH-962C: not included in any glyphset definition</li>
<li>U+962D CJK UNIFIED IDEOGRAPH-962D: not included in any glyphset definition</li>
<li>U+963C CJK UNIFIED IDEOGRAPH-963C: not included in any glyphset definition</li>
<li>U+963D CJK UNIFIED IDEOGRAPH-963D: not included in any glyphset definition</li>
<li>U+964E CJK UNIFIED IDEOGRAPH-964E: not included in any glyphset definition</li>
<li>U+9651 CJK UNIFIED IDEOGRAPH-9651: not included in any glyphset definition</li>
<li>U+9658 CJK UNIFIED IDEOGRAPH-9658: not included in any glyphset definition</li>
<li>U+9667 CJK UNIFIED IDEOGRAPH-9667: not included in any glyphset definition</li>
<li>U+9674 CJK UNIFIED IDEOGRAPH-9674: not included in any glyphset definition</li>
<li>U+9683 CJK UNIFIED IDEOGRAPH-9683: not included in any glyphset definition</li>
<li>U+9689 CJK UNIFIED IDEOGRAPH-9689: not included in any glyphset definition</li>
<li>U+9691 CJK UNIFIED IDEOGRAPH-9691: not included in any glyphset definition</li>
<li>U+969D CJK UNIFIED IDEOGRAPH-969D: not included in any glyphset definition</li>
<li>U+96A4 CJK UNIFIED IDEOGRAPH-96A4: not included in any glyphset definition</li>
<li>U+96A9 CJK UNIFIED IDEOGRAPH-96A9: not included in any glyphset definition</li>
<li>U+96AE CJK UNIFIED IDEOGRAPH-96AE: not included in any glyphset definition</li>
<li>U+96AF CJK UNIFIED IDEOGRAPH-96AF: not included in any glyphset definition</li>
<li>U+96B3 CJK UNIFIED IDEOGRAPH-96B3: not included in any glyphset definition</li>
<li>U+96BA CJK UNIFIED IDEOGRAPH-96BA: not included in any glyphset definition</li>
<li>U+96C3 CJK UNIFIED IDEOGRAPH-96C3: not included in any glyphset definition</li>
<li>U+96CA CJK UNIFIED IDEOGRAPH-96CA: not included in any glyphset definition</li>
<li>U+96E0 CJK UNIFIED IDEOGRAPH-96E0: not included in any glyphset definition</li>
<li>U+96F1 CJK UNIFIED IDEOGRAPH-96F1: not included in any glyphset definition</li>
<li>U+9702 CJK UNIFIED IDEOGRAPH-9702: not included in any glyphset definition</li>
<li>U+9705 CJK UNIFIED IDEOGRAPH-9705: not included in any glyphset definition</li>
<li>U+9726 CJK UNIFIED IDEOGRAPH-9726: not included in any glyphset definition</li>
<li>U+9728 CJK UNIFIED IDEOGRAPH-9728: not included in any glyphset definition</li>
<li>U+9733 CJK UNIFIED IDEOGRAPH-9733: not included in any glyphset definition</li>
<li>U+973B CJK UNIFIED IDEOGRAPH-973B: not included in any glyphset definition</li>
<li>U+9743 CJK UNIFIED IDEOGRAPH-9743: not included in any glyphset definition</li>
<li>U+974D CJK UNIFIED IDEOGRAPH-974D: not included in any glyphset definition</li>
<li>U+974F CJK UNIFIED IDEOGRAPH-974F: not included in any glyphset definition</li>
<li>U+976C CJK UNIFIED IDEOGRAPH-976C: not included in any glyphset definition</li>
<li>U+9770 CJK UNIFIED IDEOGRAPH-9770: not included in any glyphset definition</li>
<li>U+9777 CJK UNIFIED IDEOGRAPH-9777: not included in any glyphset definition</li>
<li>U+9778 CJK UNIFIED IDEOGRAPH-9778: not included in any glyphset definition</li>
<li>U+977D CJK UNIFIED IDEOGRAPH-977D: not included in any glyphset definition</li>
<li>U+977F CJK UNIFIED IDEOGRAPH-977F: not included in any glyphset definition</li>
<li>U+9780 CJK UNIFIED IDEOGRAPH-9780: not included in any glyphset definition</li>
<li>U+9792 CJK UNIFIED IDEOGRAPH-9792: not included in any glyphset definition</li>
<li>U+9794 CJK UNIFIED IDEOGRAPH-9794: not included in any glyphset definition</li>
<li>U+97A1 CJK UNIFIED IDEOGRAPH-97A1: not included in any glyphset definition</li>
<li>U+97A7 CJK UNIFIED IDEOGRAPH-97A7: not included in any glyphset definition</li>
<li>U+97AC CJK UNIFIED IDEOGRAPH-97AC: not included in any glyphset definition</li>
<li>U+97AE CJK UNIFIED IDEOGRAPH-97AE: not included in any glyphset definition</li>
<li>U+97AF CJK UNIFIED IDEOGRAPH-97AF: not included in any glyphset definition</li>
<li>U+97C9 CJK UNIFIED IDEOGRAPH-97C9: not included in any glyphset definition</li>
<li>U+97CD CJK UNIFIED IDEOGRAPH-97CD: not included in any glyphset definition</li>
<li>U+97D9 CJK UNIFIED IDEOGRAPH-97D9: not included in any glyphset definition</li>
<li>U+97E8 CJK UNIFIED IDEOGRAPH-97E8: not included in any glyphset definition</li>
<li>U+97F1 CJK UNIFIED IDEOGRAPH-97F1: not included in any glyphset definition</li>
<li>U+97F9 CJK UNIFIED IDEOGRAPH-97F9: not included in any glyphset definition</li>
<li>U+97FE CJK UNIFIED IDEOGRAPH-97FE: not included in any glyphset definition</li>
<li>U+9800 CJK UNIFIED IDEOGRAPH-9800: not included in any glyphset definition</li>
<li>U+9807 CJK UNIFIED IDEOGRAPH-9807: not included in any glyphset definition</li>
<li>U+980D CJK UNIFIED IDEOGRAPH-980D: not included in any glyphset definition</li>
<li>U+9820 CJK UNIFIED IDEOGRAPH-9820: not included in any glyphset definition</li>
<li>U+9832 CJK UNIFIED IDEOGRAPH-9832: not included in any glyphset definition</li>
<li>U+9835 CJK UNIFIED IDEOGRAPH-9835: not included in any glyphset definition</li>
<li>U+9852 CJK UNIFIED IDEOGRAPH-9852: not included in any glyphset definition</li>
<li>U+9859 CJK UNIFIED IDEOGRAPH-9859: not included in any glyphset definition</li>
<li>U+985A CJK UNIFIED IDEOGRAPH-985A: not included in any glyphset definition</li>
<li>U+9862 CJK UNIFIED IDEOGRAPH-9862: not included in any glyphset definition</li>
<li>U+9878 CJK UNIFIED IDEOGRAPH-9878: not included in any glyphset definition</li>
<li>U+9883 CJK UNIFIED IDEOGRAPH-9883: not included in any glyphset definition</li>
<li>U+988B CJK UNIFIED IDEOGRAPH-988B: not included in any glyphset definition</li>
<li>U+988E CJK UNIFIED IDEOGRAPH-988E: not included in any glyphset definition</li>
<li>U+9899 CJK UNIFIED IDEOGRAPH-9899: not included in any glyphset definition</li>
<li>U+989F CJK UNIFIED IDEOGRAPH-989F: not included in any glyphset definition</li>
<li>U+98A5 CJK UNIFIED IDEOGRAPH-98A5: not included in any glyphset definition</li>
<li>U+98AD CJK UNIFIED IDEOGRAPH-98AD: not included in any glyphset definition</li>
<li>U+98AE CJK UNIFIED IDEOGRAPH-98AE: not included in any glyphset definition</li>
<li>U+98B8 CJK UNIFIED IDEOGRAPH-98B8: not included in any glyphset definition</li>
<li>U+98C0 CJK UNIFIED IDEOGRAPH-98C0: not included in any glyphset definition</li>
<li>U+98C7 CJK UNIFIED IDEOGRAPH-98C7: not included in any glyphset definition</li>
<li>U+98C8 CJK UNIFIED IDEOGRAPH-98C8: not included in any glyphset definition</li>
<li>U+98D0 CJK UNIFIED IDEOGRAPH-98D0: not included in any glyphset definition</li>
<li>U+98D1 CJK UNIFIED IDEOGRAPH-98D1: not included in any glyphset definition</li>
<li>U+98D4 CJK UNIFIED IDEOGRAPH-98D4: not included in any glyphset definition</li>
<li>U+98D7 CJK UNIFIED IDEOGRAPH-98D7: not included in any glyphset definition</li>
<li>U+98E0 CJK UNIFIED IDEOGRAPH-98E0: not included in any glyphset definition</li>
<li>U+98E1 CJK UNIFIED IDEOGRAPH-98E1: not included in any glyphset definition</li>
<li>U+98E3 CJK UNIFIED IDEOGRAPH-98E3: not included in any glyphset definition</li>
<li>U+98FF CJK UNIFIED IDEOGRAPH-98FF: not included in any glyphset definition</li>
<li>U+9904 CJK UNIFIED IDEOGRAPH-9904: not included in any glyphset definition</li>
<li>U+990F CJK UNIFIED IDEOGRAPH-990F: not included in any glyphset definition</li>
<li>U+9916 CJK UNIFIED IDEOGRAPH-9916: not included in any glyphset definition</li>
<li>U+9917 CJK UNIFIED IDEOGRAPH-9917: not included in any glyphset definition</li>
<li>U+991C CJK UNIFIED IDEOGRAPH-991C: not included in any glyphset definition</li>
<li>U+9927 CJK UNIFIED IDEOGRAPH-9927: not included in any glyphset definition</li>
<li>U+9931 CJK UNIFIED IDEOGRAPH-9931: not included in any glyphset definition</li>
<li>U+9933 CJK UNIFIED IDEOGRAPH-9933: not included in any glyphset definition</li>
<li>U+9936 CJK UNIFIED IDEOGRAPH-9936: not included in any glyphset definition</li>
<li>U+9938 CJK UNIFIED IDEOGRAPH-9938: not included in any glyphset definition</li>
<li>U+993C CJK UNIFIED IDEOGRAPH-993C: not included in any glyphset definition</li>
<li>U+9941 CJK UNIFIED IDEOGRAPH-9941: not included in any glyphset definition</li>
<li>U+994A CJK UNIFIED IDEOGRAPH-994A: not included in any glyphset definition</li>
<li>U+994D CJK UNIFIED IDEOGRAPH-994D: not included in any glyphset definition</li>
<li>U+9954 CJK UNIFIED IDEOGRAPH-9954: not included in any glyphset definition</li>
<li>U+9958 CJK UNIFIED IDEOGRAPH-9958: not included in any glyphset definition</li>
<li>U+9962 CJK UNIFIED IDEOGRAPH-9962: not included in any glyphset definition</li>
<li>U+9964 CJK UNIFIED IDEOGRAPH-9964: not included in any glyphset definition</li>
<li>U+9969 CJK UNIFIED IDEOGRAPH-9969: not included in any glyphset definition</li>
<li>U+996B CJK UNIFIED IDEOGRAPH-996B: not included in any glyphset definition</li>
<li>U+9973 CJK UNIFIED IDEOGRAPH-9973: not included in any glyphset definition</li>
<li>U+9978 CJK UNIFIED IDEOGRAPH-9978: not included in any glyphset definition</li>
<li>U+9979 CJK UNIFIED IDEOGRAPH-9979: not included in any glyphset definition</li>
<li>U+997B CJK UNIFIED IDEOGRAPH-997B: not included in any glyphset definition</li>
<li>U+997E CJK UNIFIED IDEOGRAPH-997E: not included in any glyphset definition</li>
<li>U+9983 CJK UNIFIED IDEOGRAPH-9983: not included in any glyphset definition</li>
<li>U+9987 CJK UNIFIED IDEOGRAPH-9987: not included in any glyphset definition</li>
<li>U+9989 CJK UNIFIED IDEOGRAPH-9989: not included in any glyphset definition</li>
<li>U+998C CJK UNIFIED IDEOGRAPH-998C: not included in any glyphset definition</li>
<li>U+9991 CJK UNIFIED IDEOGRAPH-9991: not included in any glyphset definition</li>
<li>U+9993 CJK UNIFIED IDEOGRAPH-9993: not included in any glyphset definition</li>
<li>U+999D CJK UNIFIED IDEOGRAPH-999D: not included in any glyphset definition</li>
<li>U+999E CJK UNIFIED IDEOGRAPH-999E: not included in any glyphset definition</li>
<li>U+99A7 CJK UNIFIED IDEOGRAPH-99A7: not included in any glyphset definition</li>
<li>U+99B9 CJK UNIFIED IDEOGRAPH-99B9: not included in any glyphset definition</li>
<li>U+99C3 CJK UNIFIED IDEOGRAPH-99C3: not included in any glyphset definition</li>
<li>U+99C9 CJK UNIFIED IDEOGRAPH-99C9: not included in any glyphset definition</li>
<li>U+99D3 CJK UNIFIED IDEOGRAPH-99D3: not included in any glyphset definition</li>
<li>U+99D4 CJK UNIFIED IDEOGRAPH-99D4: not included in any glyphset definition</li>
<li>U+99EA CJK UNIFIED IDEOGRAPH-99EA: not included in any glyphset definition</li>
<li>U+99F0 CJK UNIFIED IDEOGRAPH-99F0: not included in any glyphset definition</li>
<li>U+99FC CJK UNIFIED IDEOGRAPH-99FC: not included in any glyphset definition</li>
<li>U+9A02 CJK UNIFIED IDEOGRAPH-9A02: not included in any glyphset definition</li>
<li>U+9A04 CJK UNIFIED IDEOGRAPH-9A04: not included in any glyphset definition</li>
<li>U+9A08 CJK UNIFIED IDEOGRAPH-9A08: not included in any glyphset definition</li>
<li>U+9A0A CJK UNIFIED IDEOGRAPH-9A0A: not included in any glyphset definition</li>
<li>U+9A0D CJK UNIFIED IDEOGRAPH-9A0D: not included in any glyphset definition</li>
<li>U+9A11 CJK UNIFIED IDEOGRAPH-9A11: not included in any glyphset definition</li>
<li>U+9A1E CJK UNIFIED IDEOGRAPH-9A1E: not included in any glyphset definition</li>
<li>U+9A20 CJK UNIFIED IDEOGRAPH-9A20: not included in any glyphset definition</li>
<li>U+9A24 CJK UNIFIED IDEOGRAPH-9A24: not included in any glyphset definition</li>
<li>U+9A31 CJK UNIFIED IDEOGRAPH-9A31: not included in any glyphset definition</li>
<li>U+9A35 CJK UNIFIED IDEOGRAPH-9A35: not included in any glyphset definition</li>
<li>U+9A36 CJK UNIFIED IDEOGRAPH-9A36: not included in any glyphset definition</li>
<li>U+9A38 CJK UNIFIED IDEOGRAPH-9A38: not included in any glyphset definition</li>
<li>U+9A4C CJK UNIFIED IDEOGRAPH-9A4C: not included in any glyphset definition</li>
<li>U+9A4E CJK UNIFIED IDEOGRAPH-9A4E: not included in any glyphset definition</li>
<li>U+9A4F CJK UNIFIED IDEOGRAPH-9A4F: not included in any glyphset definition</li>
<li>U+9A66 CJK UNIFIED IDEOGRAPH-9A66: not included in any glyphset definition</li>
<li>U+9A72 CJK UNIFIED IDEOGRAPH-9A72: not included in any glyphset definition</li>
<li>U+9A75 CJK UNIFIED IDEOGRAPH-9A75: not included in any glyphset definition</li>
<li>U+9A7A CJK UNIFIED IDEOGRAPH-9A7A: not included in any glyphset definition</li>
<li>U+9A80 CJK UNIFIED IDEOGRAPH-9A80: not included in any glyphset definition</li>
<li>U+9A83 CJK UNIFIED IDEOGRAPH-9A83: not included in any glyphset definition</li>
<li>U+9A89 CJK UNIFIED IDEOGRAPH-9A89: not included in any glyphset definition</li>
<li>U+9A8D CJK UNIFIED IDEOGRAPH-9A8D: not included in any glyphset definition</li>
<li>U+9A8E CJK UNIFIED IDEOGRAPH-9A8E: not included in any glyphset definition</li>
<li>U+9A92 CJK UNIFIED IDEOGRAPH-9A92: not included in any glyphset definition</li>
<li>U+9A93 CJK UNIFIED IDEOGRAPH-9A93: not included in any glyphset definition</li>
<li>U+9A95 CJK UNIFIED IDEOGRAPH-9A95: not included in any glyphset definition</li>
<li>U+9A96 CJK UNIFIED IDEOGRAPH-9A96: not included in any glyphset definition</li>
<li>U+9A98 CJK UNIFIED IDEOGRAPH-9A98: not included in any glyphset definition</li>
<li>U+9A99 CJK UNIFIED IDEOGRAPH-9A99: not included in any glyphset definition</li>
<li>U+9A9F CJK UNIFIED IDEOGRAPH-9A9F: not included in any glyphset definition</li>
<li>U+9AA3 CJK UNIFIED IDEOGRAPH-9AA3: not included in any glyphset definition</li>
<li>U+9AA6 CJK UNIFIED IDEOGRAPH-9AA6: not included in any glyphset definition</li>
<li>U+9AB1 CJK UNIFIED IDEOGRAPH-9AB1: not included in any glyphset definition</li>
<li>U+9ABA CJK UNIFIED IDEOGRAPH-9ABA: not included in any glyphset definition</li>
<li>U+9ABE CJK UNIFIED IDEOGRAPH-9ABE: not included in any glyphset definition</li>
<li>U+9AC3 CJK UNIFIED IDEOGRAPH-9AC3: not included in any glyphset definition</li>
<li>U+9ACE CJK UNIFIED IDEOGRAPH-9ACE: not included in any glyphset definition</li>
<li>U+9ADC CJK UNIFIED IDEOGRAPH-9ADC: not included in any glyphset definition</li>
<li>U+9AE1 CJK UNIFIED IDEOGRAPH-9AE1: not included in any glyphset definition</li>
<li>U+9AE5 CJK UNIFIED IDEOGRAPH-9AE5: not included in any glyphset definition</li>
<li>U+9AFD CJK UNIFIED IDEOGRAPH-9AFD: not included in any glyphset definition</li>
<li>U+9B12 CJK UNIFIED IDEOGRAPH-9B12: not included in any glyphset definition</li>
<li>U+9B36 CJK UNIFIED IDEOGRAPH-9B36: not included in any glyphset definition</li>
<li>U+9B37 CJK UNIFIED IDEOGRAPH-9B37: not included in any glyphset definition</li>
<li>U+9B46 CJK UNIFIED IDEOGRAPH-9B46: not included in any glyphset definition</li>
<li>U+9B48 CJK UNIFIED IDEOGRAPH-9B48: not included in any glyphset definition</li>
<li>U+9B4B CJK UNIFIED IDEOGRAPH-9B4B: not included in any glyphset definition</li>
<li>U+9B5B CJK UNIFIED IDEOGRAPH-9B5B: not included in any glyphset definition</li>
<li>U+9B62 CJK UNIFIED IDEOGRAPH-9B62: not included in any glyphset definition</li>
<li>U+9B68 CJK UNIFIED IDEOGRAPH-9B68: not included in any glyphset definition</li>
<li>U+9B69 CJK UNIFIED IDEOGRAPH-9B69: not included in any glyphset definition</li>
<li>U+9B72 CJK UNIFIED IDEOGRAPH-9B72: not included in any glyphset definition</li>
<li>U+9B75 CJK UNIFIED IDEOGRAPH-9B75: not included in any glyphset definition</li>
<li>U+9B7D CJK UNIFIED IDEOGRAPH-9B7D: not included in any glyphset definition</li>
<li>U+9B80 CJK UNIFIED IDEOGRAPH-9B80: not included in any glyphset definition</li>
<li>U+9B81 CJK UNIFIED IDEOGRAPH-9B81: not included in any glyphset definition</li>
<li>U+9B86 CJK UNIFIED IDEOGRAPH-9B86: not included in any glyphset definition</li>
<li>U+9B88 CJK UNIFIED IDEOGRAPH-9B88: not included in any glyphset definition</li>
<li>U+9B8A CJK UNIFIED IDEOGRAPH-9B8A: not included in any glyphset definition</li>
<li>U+9B8B CJK UNIFIED IDEOGRAPH-9B8B: not included in any glyphset definition</li>
<li>U+9B8D CJK UNIFIED IDEOGRAPH-9B8D: not included in any glyphset definition</li>
<li>U+9B90 CJK UNIFIED IDEOGRAPH-9B90: not included in any glyphset definition</li>
<li>U+9B95 CJK UNIFIED IDEOGRAPH-9B95: not included in any glyphset definition</li>
<li>U+9B98 CJK UNIFIED IDEOGRAPH-9B98: not included in any glyphset definition</li>
<li>U+9B9A CJK UNIFIED IDEOGRAPH-9B9A: not included in any glyphset definition</li>
<li>U+9B9C CJK UNIFIED IDEOGRAPH-9B9C: not included in any glyphset definition</li>
<li>U+9B9E CJK UNIFIED IDEOGRAPH-9B9E: not included in any glyphset definition</li>
<li>U+9BA1 CJK UNIFIED IDEOGRAPH-9BA1: not included in any glyphset definition</li>
<li>U+9BA3 CJK UNIFIED IDEOGRAPH-9BA3: not included in any glyphset definition</li>
<li>U+9BA6 CJK UNIFIED IDEOGRAPH-9BA6: not included in any glyphset definition</li>
<li>U+9BB1 CJK UNIFIED IDEOGRAPH-9BB1: not included in any glyphset definition</li>
<li>U+9BB6 CJK UNIFIED IDEOGRAPH-9BB6: not included in any glyphset definition</li>
<li>U+9BB8 CJK UNIFIED IDEOGRAPH-9BB8: not included in any glyphset definition</li>
<li>U+9BBA CJK UNIFIED IDEOGRAPH-9BBA: not included in any glyphset definition</li>
<li>U+9BBB CJK UNIFIED IDEOGRAPH-9BBB: not included in any glyphset definition</li>
<li>U+9BC8 CJK UNIFIED IDEOGRAPH-9BC8: not included in any glyphset definition</li>
<li>U+9BD5 CJK UNIFIED IDEOGRAPH-9BD5: not included in any glyphset definition</li>
<li>U+9BD7 CJK UNIFIED IDEOGRAPH-9BD7: not included in any glyphset definition</li>
<li>U+9BD9 CJK UNIFIED IDEOGRAPH-9BD9: not included in any glyphset definition</li>
<li>U+9BDD CJK UNIFIED IDEOGRAPH-9BDD: not included in any glyphset definition</li>
<li>U+9BEB CJK UNIFIED IDEOGRAPH-9BEB: not included in any glyphset definition</li>
<li>U+9BED CJK UNIFIED IDEOGRAPH-9BED: not included in any glyphset definition</li>
<li>U+9BFB CJK UNIFIED IDEOGRAPH-9BFB: not included in any glyphset definition</li>
<li>U+9BFF CJK UNIFIED IDEOGRAPH-9BFF: not included in any glyphset definition</li>
<li>U+9C00 CJK UNIFIED IDEOGRAPH-9C00: not included in any glyphset definition</li>
<li>U+9C01 CJK UNIFIED IDEOGRAPH-9C01: not included in any glyphset definition</li>
<li>U+9C02 CJK UNIFIED IDEOGRAPH-9C02: not included in any glyphset definition</li>
<li>U+9C03 CJK UNIFIED IDEOGRAPH-9C03: not included in any glyphset definition</li>
<li>U+9C0F CJK UNIFIED IDEOGRAPH-9C0F: not included in any glyphset definition</li>
<li>U+9C1C CJK UNIFIED IDEOGRAPH-9C1C: not included in any glyphset definition</li>
<li>U+9C1F CJK UNIFIED IDEOGRAPH-9C1F: not included in any glyphset definition</li>
<li>U+9C23 CJK UNIFIED IDEOGRAPH-9C23: not included in any glyphset definition</li>
<li>U+9C27 CJK UNIFIED IDEOGRAPH-9C27: not included in any glyphset definition</li>
<li>U+9C28 CJK UNIFIED IDEOGRAPH-9C28: not included in any glyphset definition</li>
<li>U+9C33 CJK UNIFIED IDEOGRAPH-9C33: not included in any glyphset definition</li>
<li>U+9C35 CJK UNIFIED IDEOGRAPH-9C35: not included in any glyphset definition</li>
<li>U+9C36 CJK UNIFIED IDEOGRAPH-9C36: not included in any glyphset definition</li>
<li>U+9C37 CJK UNIFIED IDEOGRAPH-9C37: not included in any glyphset definition</li>
<li>U+9C3C CJK UNIFIED IDEOGRAPH-9C3C: not included in any glyphset definition</li>
<li>U+9C40 CJK UNIFIED IDEOGRAPH-9C40: not included in any glyphset definition</li>
<li>U+9C42 CJK UNIFIED IDEOGRAPH-9C42: not included in any glyphset definition</li>
<li>U+9C45 CJK UNIFIED IDEOGRAPH-9C45: not included in any glyphset definition</li>
<li>U+9C56 CJK UNIFIED IDEOGRAPH-9C56: not included in any glyphset definition</li>
<li>U+9C59 CJK UNIFIED IDEOGRAPH-9C59: not included in any glyphset definition</li>
<li>U+9C5D CJK UNIFIED IDEOGRAPH-9C5D: not included in any glyphset definition</li>
<li>U+9C63 CJK UNIFIED IDEOGRAPH-9C63: not included in any glyphset definition</li>
<li>U+9C64 CJK UNIFIED IDEOGRAPH-9C64: not included in any glyphset definition</li>
<li>U+9C68 CJK UNIFIED IDEOGRAPH-9C68: not included in any glyphset definition</li>
<li>U+9C6D CJK UNIFIED IDEOGRAPH-9C6D: not included in any glyphset definition</li>
<li>U+9C6F CJK UNIFIED IDEOGRAPH-9C6F: not included in any glyphset definition</li>
<li>U+9C72 CJK UNIFIED IDEOGRAPH-9C72: not included in any glyphset definition</li>
<li>U+9C7D CJK UNIFIED IDEOGRAPH-9C7D: not included in any glyphset definition</li>
<li>U+9C7E CJK UNIFIED IDEOGRAPH-9C7E: not included in any glyphset definition</li>
<li>U+9C80 CJK UNIFIED IDEOGRAPH-9C80: not included in any glyphset definition</li>
<li>U+9C82 CJK UNIFIED IDEOGRAPH-9C82: not included in any glyphset definition</li>
<li>U+9C83 CJK UNIFIED IDEOGRAPH-9C83: not included in any glyphset definition</li>
<li>U+9C86 CJK UNIFIED IDEOGRAPH-9C86: not included in any glyphset definition</li>
<li>U+9C89 CJK UNIFIED IDEOGRAPH-9C89: not included in any glyphset definition</li>
<li>U+9C8A CJK UNIFIED IDEOGRAPH-9C8A: not included in any glyphset definition</li>
<li>U+9C8B CJK UNIFIED IDEOGRAPH-9C8B: not included in any glyphset definition</li>
<li>U+9C8C CJK UNIFIED IDEOGRAPH-9C8C: not included in any glyphset definition</li>
<li>U+9C8E CJK UNIFIED IDEOGRAPH-9C8E: not included in any glyphset definition</li>
<li>U+9C8F CJK UNIFIED IDEOGRAPH-9C8F: not included in any glyphset definition</li>
<li>U+9C90 CJK UNIFIED IDEOGRAPH-9C90: not included in any glyphset definition</li>
<li>U+9C92 CJK UNIFIED IDEOGRAPH-9C92: not included in any glyphset definition</li>
<li>U+9C95 CJK UNIFIED IDEOGRAPH-9C95: not included in any glyphset definition</li>
<li>U+9C96 CJK UNIFIED IDEOGRAPH-9C96: not included in any glyphset definition</li>
<li>U+9C97 CJK UNIFIED IDEOGRAPH-9C97: not included in any glyphset definition</li>
<li>U+9C98 CJK UNIFIED IDEOGRAPH-9C98: not included in any glyphset definition</li>
<li>U+9C99 CJK UNIFIED IDEOGRAPH-9C99: not included in any glyphset definition</li>
<li>U+9C9A CJK UNIFIED IDEOGRAPH-9C9A: not included in any glyphset definition</li>
<li>U+9C9D CJK UNIFIED IDEOGRAPH-9C9D: not included in any glyphset definition</li>
<li>U+9C9E CJK UNIFIED IDEOGRAPH-9C9E: not included in any glyphset definition</li>
<li>U+9CA1 CJK UNIFIED IDEOGRAPH-9CA1: not included in any glyphset definition</li>
<li>U+9CA5 CJK UNIFIED IDEOGRAPH-9CA5: not included in any glyphset definition</li>
<li>U+9CA6 CJK UNIFIED IDEOGRAPH-9CA6: not included in any glyphset definition</li>
<li>U+9CA7 CJK UNIFIED IDEOGRAPH-9CA7: not included in any glyphset definition</li>
<li>U+9CA9 CJK UNIFIED IDEOGRAPH-9CA9: not included in any glyphset definition</li>
<li>U+9CAA CJK UNIFIED IDEOGRAPH-9CAA: not included in any glyphset definition</li>
<li>U+9CAC CJK UNIFIED IDEOGRAPH-9CAC: not included in any glyphset definition</li>
<li>U+9CAF CJK UNIFIED IDEOGRAPH-9CAF: not included in any glyphset definition</li>
<li>U+9CB0 CJK UNIFIED IDEOGRAPH-9CB0: not included in any glyphset definition</li>
<li>U+9CB4 CJK UNIFIED IDEOGRAPH-9CB4: not included in any glyphset definition</li>
<li>U+9CB9 CJK UNIFIED IDEOGRAPH-9CB9: not included in any glyphset definition</li>
<li>U+9CBA CJK UNIFIED IDEOGRAPH-9CBA: not included in any glyphset definition</li>
<li>U+9CBB CJK UNIFIED IDEOGRAPH-9CBB: not included in any glyphset definition</li>
<li>U+9CBC CJK UNIFIED IDEOGRAPH-9CBC: not included in any glyphset definition</li>
<li>U+9CBE CJK UNIFIED IDEOGRAPH-9CBE: not included in any glyphset definition</li>
<li>U+9CBF CJK UNIFIED IDEOGRAPH-9CBF: not included in any glyphset definition</li>
<li>U+9CC0 CJK UNIFIED IDEOGRAPH-9CC0: not included in any glyphset definition</li>
<li>U+9CC1 CJK UNIFIED IDEOGRAPH-9CC1: not included in any glyphset definition</li>
<li>U+9CC2 CJK UNIFIED IDEOGRAPH-9CC2: not included in any glyphset definition</li>
<li>U+9CC6 CJK UNIFIED IDEOGRAPH-9CC6: not included in any glyphset definition</li>
<li>U+9CC7 CJK UNIFIED IDEOGRAPH-9CC7: not included in any glyphset definition</li>
<li>U+9CC8 CJK UNIFIED IDEOGRAPH-9CC8: not included in any glyphset definition</li>
<li>U+9CC9 CJK UNIFIED IDEOGRAPH-9CC9: not included in any glyphset definition</li>
<li>U+9CCB CJK UNIFIED IDEOGRAPH-9CCB: not included in any glyphset definition</li>
<li>U+9CCE CJK UNIFIED IDEOGRAPH-9CCE: not included in any glyphset definition</li>
<li>U+9CD1 CJK UNIFIED IDEOGRAPH-9CD1: not included in any glyphset definition</li>
<li>U+9CD2 CJK UNIFIED IDEOGRAPH-9CD2: not included in any glyphset definition</li>
<li>U+9CD3 CJK UNIFIED IDEOGRAPH-9CD3: not included in any glyphset definition</li>
<li>U+9CD8 CJK UNIFIED IDEOGRAPH-9CD8: not included in any glyphset definition</li>
<li>U+9CDA CJK UNIFIED IDEOGRAPH-9CDA: not included in any glyphset definition</li>
<li>U+9CDB CJK UNIFIED IDEOGRAPH-9CDB: not included in any glyphset definition</li>
<li>U+9CE0 CJK UNIFIED IDEOGRAPH-9CE0: not included in any glyphset definition</li>
<li>U+9CE1 CJK UNIFIED IDEOGRAPH-9CE1: not included in any glyphset definition</li>
<li>U+9CE2 CJK UNIFIED IDEOGRAPH-9CE2: not included in any glyphset definition</li>
<li>U+9CE3 CJK UNIFIED IDEOGRAPH-9CE3: not included in any glyphset definition</li>
<li>U+9CE4 CJK UNIFIED IDEOGRAPH-9CE4: not included in any glyphset definition</li>
<li>U+9CF2 CJK UNIFIED IDEOGRAPH-9CF2: not included in any glyphset definition</li>
<li>U+9CFE CJK UNIFIED IDEOGRAPH-9CFE: not included in any glyphset definition</li>
<li>U+9D30 CJK UNIFIED IDEOGRAPH-9D30: not included in any glyphset definition</li>
<li>U+9D34 CJK UNIFIED IDEOGRAPH-9D34: not included in any glyphset definition</li>
<li>U+9D37 CJK UNIFIED IDEOGRAPH-9D37: not included in any glyphset definition</li>
<li>U+9D3D CJK UNIFIED IDEOGRAPH-9D3D: not included in any glyphset definition</li>
<li>U+9D42 CJK UNIFIED IDEOGRAPH-9D42: not included in any glyphset definition</li>
<li>U+9D43 CJK UNIFIED IDEOGRAPH-9D43: not included in any glyphset definition</li>
<li>U+9D4F CJK UNIFIED IDEOGRAPH-9D4F: not included in any glyphset definition</li>
<li>U+9D52 CJK UNIFIED IDEOGRAPH-9D52: not included in any glyphset definition</li>
<li>U+9D53 CJK UNIFIED IDEOGRAPH-9D53: not included in any glyphset definition</li>
<li>U+9D6B CJK UNIFIED IDEOGRAPH-9D6B: not included in any glyphset definition</li>
<li>U+9D7E CJK UNIFIED IDEOGRAPH-9D7E: not included in any glyphset definition</li>
<li>U+9D84 CJK UNIFIED IDEOGRAPH-9D84: not included in any glyphset definition</li>
<li>U+9D86 CJK UNIFIED IDEOGRAPH-9D86: not included in any glyphset definition</li>
<li>U+9D8A CJK UNIFIED IDEOGRAPH-9D8A: not included in any glyphset definition</li>
<li>U+9D93 CJK UNIFIED IDEOGRAPH-9D93: not included in any glyphset definition</li>
<li>U+9D96 CJK UNIFIED IDEOGRAPH-9D96: not included in any glyphset definition</li>
<li>U+9DA0 CJK UNIFIED IDEOGRAPH-9DA0: not included in any glyphset definition</li>
<li>U+9DA1 CJK UNIFIED IDEOGRAPH-9DA1: not included in any glyphset definition</li>
<li>U+9DA5 CJK UNIFIED IDEOGRAPH-9DA5: not included in any glyphset definition</li>
<li>U+9DAA CJK UNIFIED IDEOGRAPH-9DAA: not included in any glyphset definition</li>
<li>U+9DAC CJK UNIFIED IDEOGRAPH-9DAC: not included in any glyphset definition</li>
<li>U+9DB1 CJK UNIFIED IDEOGRAPH-9DB1: not included in any glyphset definition</li>
<li>U+9DB9 CJK UNIFIED IDEOGRAPH-9DB9: not included in any glyphset definition</li>
<li>U+9DC0 CJK UNIFIED IDEOGRAPH-9DC0: not included in any glyphset definition</li>
<li>U+9DC8 CJK UNIFIED IDEOGRAPH-9DC8: not included in any glyphset definition</li>
<li>U+9DC9 CJK UNIFIED IDEOGRAPH-9DC9: not included in any glyphset definition</li>
<li>U+9DCA CJK UNIFIED IDEOGRAPH-9DCA: not included in any glyphset definition</li>
<li>U+9DDA CJK UNIFIED IDEOGRAPH-9DDA: not included in any glyphset definition</li>
<li>U+9DDF CJK UNIFIED IDEOGRAPH-9DDF: not included in any glyphset definition</li>
<li>U+9DEB CJK UNIFIED IDEOGRAPH-9DEB: not included in any glyphset definition</li>
<li>U+9DF3 CJK UNIFIED IDEOGRAPH-9DF3: not included in any glyphset definition</li>
<li>U+9DFF CJK UNIFIED IDEOGRAPH-9DFF: not included in any glyphset definition</li>
<li>U+9E07 CJK UNIFIED IDEOGRAPH-9E07: not included in any glyphset definition</li>
<li>U+9E0A CJK UNIFIED IDEOGRAPH-9E0A: not included in any glyphset definition</li>
<li>U+9E0F CJK UNIFIED IDEOGRAPH-9E0F: not included in any glyphset definition</li>
<li>U+9E11 CJK UNIFIED IDEOGRAPH-9E11: not included in any glyphset definition</li>
<li>U+9E18 CJK UNIFIED IDEOGRAPH-9E18: not included in any glyphset definition</li>
<li>U+9E19 CJK UNIFIED IDEOGRAPH-9E19: not included in any glyphset definition</li>
<li>U+9E24 CJK UNIFIED IDEOGRAPH-9E24: not included in any glyphset definition</li>
<li>U+9E27 CJK UNIFIED IDEOGRAPH-9E27: not included in any glyphset definition</li>
<li>U+9E32 CJK UNIFIED IDEOGRAPH-9E32: not included in any glyphset definition</li>
<li>U+9E38 CJK UNIFIED IDEOGRAPH-9E38: not included in any glyphset definition</li>
<li>U+9E39 CJK UNIFIED IDEOGRAPH-9E39: not included in any glyphset definition</li>
<li>U+9E3A CJK UNIFIED IDEOGRAPH-9E3A: not included in any glyphset definition</li>
<li>U+9E3B CJK UNIFIED IDEOGRAPH-9E3B: not included in any glyphset definition</li>
<li>U+9E3C CJK UNIFIED IDEOGRAPH-9E3C: not included in any glyphset definition</li>
<li>U+9E40 CJK UNIFIED IDEOGRAPH-9E40: not included in any glyphset definition</li>
<li>U+9E41 CJK UNIFIED IDEOGRAPH-9E41: not included in any glyphset definition</li>
<li>U+9E46 CJK UNIFIED IDEOGRAPH-9E46: not included in any glyphset definition</li>
<li>U+9E47 CJK UNIFIED IDEOGRAPH-9E47: not included in any glyphset definition</li>
<li>U+9E4B CJK UNIFIED IDEOGRAPH-9E4B: not included in any glyphset definition</li>
<li>U+9E4D CJK UNIFIED IDEOGRAPH-9E4D: not included in any glyphset definition</li>
<li>U+9E4E CJK UNIFIED IDEOGRAPH-9E4E: not included in any glyphset definition</li>
<li>U+9E50 CJK UNIFIED IDEOGRAPH-9E50: not included in any glyphset definition</li>
<li>U+9E52 CJK UNIFIED IDEOGRAPH-9E52: not included in any glyphset definition</li>
<li>U+9E54 CJK UNIFIED IDEOGRAPH-9E54: not included in any glyphset definition</li>
<li>U+9E56 CJK UNIFIED IDEOGRAPH-9E56: not included in any glyphset definition</li>
<li>U+9E59 CJK UNIFIED IDEOGRAPH-9E59: not included in any glyphset definition</li>
<li>U+9E5B CJK UNIFIED IDEOGRAPH-9E5B: not included in any glyphset definition</li>
<li>U+9E5D CJK UNIFIED IDEOGRAPH-9E5D: not included in any glyphset definition</li>
<li>U+9E5F CJK UNIFIED IDEOGRAPH-9E5F: not included in any glyphset definition</li>
<li>U+9E60 CJK UNIFIED IDEOGRAPH-9E60: not included in any glyphset definition</li>
<li>U+9E61 CJK UNIFIED IDEOGRAPH-9E61: not included in any glyphset definition</li>
<li>U+9E62 CJK UNIFIED IDEOGRAPH-9E62: not included in any glyphset definition</li>
<li>U+9E63 CJK UNIFIED IDEOGRAPH-9E63: not included in any glyphset definition</li>
<li>U+9E68 CJK UNIFIED IDEOGRAPH-9E68: not included in any glyphset definition</li>
<li>U+9E6A CJK UNIFIED IDEOGRAPH-9E6A: not included in any glyphset definition</li>
<li>U+9E6F CJK UNIFIED IDEOGRAPH-9E6F: not included in any glyphset definition</li>
<li>U+9E71 CJK UNIFIED IDEOGRAPH-9E71: not included in any glyphset definition</li>
<li>U+9E72 CJK UNIFIED IDEOGRAPH-9E72: not included in any glyphset definition</li>
<li>U+9E74 CJK UNIFIED IDEOGRAPH-9E74: not included in any glyphset definition</li>
<li>U+9E7A CJK UNIFIED IDEOGRAPH-9E7A: not included in any glyphset definition</li>
<li>U+9E7E CJK UNIFIED IDEOGRAPH-9E7E: not included in any glyphset definition</li>
<li>U+9E80 CJK UNIFIED IDEOGRAPH-9E80: not included in any glyphset definition</li>
<li>U+9E87 CJK UNIFIED IDEOGRAPH-9E87: not included in any glyphset definition</li>
<li>U+9E96 CJK UNIFIED IDEOGRAPH-9E96: not included in any glyphset definition</li>
<li>U+9EAF CJK UNIFIED IDEOGRAPH-9EAF: not included in any glyphset definition</li>
<li>U+9EE1 CJK UNIFIED IDEOGRAPH-9EE1: not included in any glyphset definition</li>
<li>U+9EE2 CJK UNIFIED IDEOGRAPH-9EE2: not included in any glyphset definition</li>
<li>U+9EE7 CJK UNIFIED IDEOGRAPH-9EE7: not included in any glyphset definition</li>
<li>U+9EE9 CJK UNIFIED IDEOGRAPH-9EE9: not included in any glyphset definition</li>
<li>U+9EEA CJK UNIFIED IDEOGRAPH-9EEA: not included in any glyphset definition</li>
<li>U+9EF2 CJK UNIFIED IDEOGRAPH-9EF2: not included in any glyphset definition</li>
<li>U+9F09 CJK UNIFIED IDEOGRAPH-9F09: not included in any glyphset definition</li>
<li>U+9F0D CJK UNIFIED IDEOGRAPH-9F0D: not included in any glyphset definition</li>
<li>U+9F12 CJK UNIFIED IDEOGRAPH-9F12: not included in any glyphset definition</li>
<li>U+9F19 CJK UNIFIED IDEOGRAPH-9F19: not included in any glyphset definition</li>
<li>U+9F22 CJK UNIFIED IDEOGRAPH-9F22: not included in any glyphset definition</li>
<li>U+9F29 CJK UNIFIED IDEOGRAPH-9F29: not included in any glyphset definition</li>
<li>U+9F2B CJK UNIFIED IDEOGRAPH-9F2B: not included in any glyphset definition</li>
<li>U+9F31 CJK UNIFIED IDEOGRAPH-9F31: not included in any glyphset definition</li>
<li>U+9F37 CJK UNIFIED IDEOGRAPH-9F37: not included in any glyphset definition</li>
<li>U+9F3D CJK UNIFIED IDEOGRAPH-9F3D: not included in any glyphset definition</li>
<li>U+9F47 CJK UNIFIED IDEOGRAPH-9F47: not included in any glyphset definition</li>
<li>U+9F49 CJK UNIFIED IDEOGRAPH-9F49: not included in any glyphset definition</li>
<li>U+9F51 CJK UNIFIED IDEOGRAPH-9F51: not included in any glyphset definition</li>
<li>U+9F55 CJK UNIFIED IDEOGRAPH-9F55: not included in any glyphset definition</li>
<li>U+9F57 CJK UNIFIED IDEOGRAPH-9F57: not included in any glyphset definition</li>
<li>U+9F58 CJK UNIFIED IDEOGRAPH-9F58: not included in any glyphset definition</li>
<li>U+9F6E CJK UNIFIED IDEOGRAPH-9F6E: not included in any glyphset definition</li>
<li>U+9F6F CJK UNIFIED IDEOGRAPH-9F6F: not included in any glyphset definition</li>
<li>U+9F7C CJK UNIFIED IDEOGRAPH-9F7C: not included in any glyphset definition</li>
<li>U+9F80 CJK UNIFIED IDEOGRAPH-9F80: not included in any glyphset definition</li>
<li>U+9F81 CJK UNIFIED IDEOGRAPH-9F81: not included in any glyphset definition</li>
<li>U+9F82 CJK UNIFIED IDEOGRAPH-9F82: not included in any glyphset definition</li>
<li>U+9F83 CJK UNIFIED IDEOGRAPH-9F83: not included in any glyphset definition</li>
<li>U+9F86 CJK UNIFIED IDEOGRAPH-9F86: not included in any glyphset definition</li>
<li>U+9F89 CJK UNIFIED IDEOGRAPH-9F89: not included in any glyphset definition</li>
<li>U+9F91 CJK UNIFIED IDEOGRAPH-9F91: not included in any glyphset definition</li>
<li>U+9FCD CJK UNIFIED IDEOGRAPH-9FCD: not included in any glyphset definition</li>
<li>U+9FCE CJK UNIFIED IDEOGRAPH-9FCE: not included in any glyphset definition</li>
<li>U+9FCF CJK UNIFIED IDEOGRAPH-9FCF: not included in any glyphset definition</li>
<li>U+9FD4 CJK UNIFIED IDEOGRAPH-9FD4: not included in any glyphset definition</li>
<li>U+9FEB CJK UNIFIED IDEOGRAPH-9FEB: not included in any glyphset definition</li>
<li>U+9FEC CJK UNIFIED IDEOGRAPH-9FEC: not included in any glyphset definition</li>
<li>U+9FED CJK UNIFIED IDEOGRAPH-9FED: not included in any glyphset definition</li>
<li>U+E114 : not included in any glyphset definition</li>
<li>U+F929 CJK COMPATIBILITY IDEOGRAPH-F929: not included in any glyphset definition</li>
<li>U+F9DC CJK COMPATIBILITY IDEOGRAPH-F9DC: not included in any glyphset definition</li>
<li>U+FA0E CJK COMPATIBILITY IDEOGRAPH-FA0E: not included in any glyphset definition</li>
<li>U+FA0F CJK COMPATIBILITY IDEOGRAPH-FA0F: not included in any glyphset definition</li>
<li>U+FA10 CJK COMPATIBILITY IDEOGRAPH-FA10: not included in any glyphset definition</li>
<li>U+FA11 CJK COMPATIBILITY IDEOGRAPH-FA11: not included in any glyphset definition</li>
<li>U+FA12 CJK COMPATIBILITY IDEOGRAPH-FA12: not included in any glyphset definition</li>
<li>U+FA13 CJK COMPATIBILITY IDEOGRAPH-FA13: not included in any glyphset definition</li>
<li>U+FA14 CJK COMPATIBILITY IDEOGRAPH-FA14: not included in any glyphset definition</li>
<li>U+FA15 CJK COMPATIBILITY IDEOGRAPH-FA15: not included in any glyphset definition</li>
<li>U+FA16 CJK COMPATIBILITY IDEOGRAPH-FA16: not included in any glyphset definition</li>
<li>U+FA17 CJK COMPATIBILITY IDEOGRAPH-FA17: not included in any glyphset definition</li>
<li>U+FA18 CJK COMPATIBILITY IDEOGRAPH-FA18: not included in any glyphset definition</li>
<li>U+FA19 CJK COMPATIBILITY IDEOGRAPH-FA19: not included in any glyphset definition</li>
<li>U+FA1A CJK COMPATIBILITY IDEOGRAPH-FA1A: not included in any glyphset definition</li>
<li>U+FA1B CJK COMPATIBILITY IDEOGRAPH-FA1B: not included in any glyphset definition</li>
<li>U+FA1C CJK COMPATIBILITY IDEOGRAPH-FA1C: not included in any glyphset definition</li>
<li>U+FA1D CJK COMPATIBILITY IDEOGRAPH-FA1D: not included in any glyphset definition</li>
<li>U+FA1E CJK COMPATIBILITY IDEOGRAPH-FA1E: not included in any glyphset definition</li>
<li>U+FA1F CJK COMPATIBILITY IDEOGRAPH-FA1F: not included in any glyphset definition</li>
<li>U+FA20 CJK COMPATIBILITY IDEOGRAPH-FA20: not included in any glyphset definition</li>
<li>U+FA21 CJK COMPATIBILITY IDEOGRAPH-FA21: not included in any glyphset definition</li>
<li>U+FA22 CJK COMPATIBILITY IDEOGRAPH-FA22: not included in any glyphset definition</li>
<li>U+FA23 CJK COMPATIBILITY IDEOGRAPH-FA23: not included in any glyphset definition</li>
<li>U+FA24 CJK COMPATIBILITY IDEOGRAPH-FA24: not included in any glyphset definition</li>
<li>U+FA25 CJK COMPATIBILITY IDEOGRAPH-FA25: not included in any glyphset definition</li>
<li>U+FA26 CJK COMPATIBILITY IDEOGRAPH-FA26: not included in any glyphset definition</li>
<li>U+FA27 CJK COMPATIBILITY IDEOGRAPH-FA27: not included in any glyphset definition</li>
<li>U+FA28 CJK COMPATIBILITY IDEOGRAPH-FA28: not included in any glyphset definition</li>
<li>U+FA29 CJK COMPATIBILITY IDEOGRAPH-FA29: not included in any glyphset definition</li>
<li>U+FA2A CJK COMPATIBILITY IDEOGRAPH-FA2A: not included in any glyphset definition</li>
<li>U+FA2B CJK COMPATIBILITY IDEOGRAPH-FA2B: not included in any glyphset definition</li>
<li>U+FA2C CJK COMPATIBILITY IDEOGRAPH-FA2C: not included in any glyphset definition</li>
<li>U+FA2D CJK COMPATIBILITY IDEOGRAPH-FA2D: not included in any glyphset definition</li>
<li>U+FE10 PRESENTATION FORM FOR VERTICAL COMMA: not included in any glyphset definition</li>
<li>U+FE11 PRESENTATION FORM FOR VERTICAL IDEOGRAPHIC COMMA: not included in any glyphset definition</li>
<li>U+FE12 PRESENTATION FORM FOR VERTICAL IDEOGRAPHIC FULL STOP: try adding nushu</li>
<li>U+FE13 PRESENTATION FORM FOR VERTICAL COLON: not included in any glyphset definition</li>
<li>U+FE14 PRESENTATION FORM FOR VERTICAL SEMICOLON: not included in any glyphset definition</li>
<li>U+FE15 PRESENTATION FORM FOR VERTICAL EXCLAMATION MARK: not included in any glyphset definition</li>
<li>U+FE16 PRESENTATION FORM FOR VERTICAL QUESTION MARK: not included in any glyphset definition</li>
<li>U+FE17 PRESENTATION FORM FOR VERTICAL LEFT WHITE LENTICULAR BRACKET: not included in any glyphset definition</li>
<li>U+FE18 PRESENTATION FORM FOR VERTICAL RIGHT WHITE LENTICULAR BRAKCET: not included in any glyphset definition</li>
<li>U+FE19 PRESENTATION FORM FOR VERTICAL HORIZONTAL ELLIPSIS: not included in any glyphset definition</li>
<li>U+FE33 PRESENTATION FORM FOR VERTICAL LOW LINE: not included in any glyphset definition</li>
<li>U+FE37 PRESENTATION FORM FOR VERTICAL LEFT CURLY BRACKET: not included in any glyphset definition</li>
<li>U+FE38 PRESENTATION FORM FOR VERTICAL RIGHT CURLY BRACKET: not included in any glyphset definition</li>
<li>U+FE3A PRESENTATION FORM FOR VERTICAL RIGHT TORTOISE SHELL BRACKET: not included in any glyphset definition</li>
<li>U+FE3B PRESENTATION FORM FOR VERTICAL LEFT BLACK LENTICULAR BRACKET: not included in any glyphset definition</li>
<li>U+FE3C PRESENTATION FORM FOR VERTICAL RIGHT BLACK LENTICULAR BRACKET: not included in any glyphset definition</li>
<li>U+FE42 PRESENTATION FORM FOR VERTICAL RIGHT CORNER BRACKET: try adding mongolian</li>
<li>U+FE44 PRESENTATION FORM FOR VERTICAL RIGHT WHITE CORNER BRACKET: try adding mongolian</li>
<li>U+FE47 PRESENTATION FORM FOR VERTICAL LEFT SQUARE BRACKET: not included in any glyphset definition</li>
<li>U+FE48 PRESENTATION FORM FOR VERTICAL RIGHT SQUARE BRACKET: not included in any glyphset definition</li>
<li>U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP: try adding yi</li>
<li>U+FF62 HALFWIDTH LEFT CORNER BRACKET: try adding yi</li>
<li>U+FF63 HALFWIDTH RIGHT CORNER BRACKET: try adding yi</li>
<li>U+FF64 HALFWIDTH IDEOGRAPHIC COMMA: try adding yi</li>
<li>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT: try adding yi</li>
<li>U+FF66 HALFWIDTH KATAKANA LETTER WO: not included in any glyphset definition</li>
<li>U+FF67 HALFWIDTH KATAKANA LETTER SMALL A: not included in any glyphset definition</li>
<li>U+FF68 HALFWIDTH KATAKANA LETTER SMALL I: not included in any glyphset definition</li>
<li>U+FF69 HALFWIDTH KATAKANA LETTER SMALL U: not included in any glyphset definition</li>
<li>U+FF6A HALFWIDTH KATAKANA LETTER SMALL E: not included in any glyphset definition</li>
<li>U+FF6B HALFWIDTH KATAKANA LETTER SMALL O: not included in any glyphset definition</li>
<li>U+FF6C HALFWIDTH KATAKANA LETTER SMALL YA: not included in any glyphset definition</li>
<li>U+FF6D HALFWIDTH KATAKANA LETTER SMALL YU: not included in any glyphset definition</li>
<li>U+FF6E HALFWIDTH KATAKANA LETTER SMALL YO: not included in any glyphset definition</li>
<li>U+FF6F HALFWIDTH KATAKANA LETTER SMALL TU: not included in any glyphset definition</li>
<li>U+FF70 HALFWIDTH KATAKANA-HIRAGANA PROLONGED SOUND MARK: not included in any glyphset definition</li>
<li>U+FF71 HALFWIDTH KATAKANA LETTER A: not included in any glyphset definition</li>
<li>U+FF72 HALFWIDTH KATAKANA LETTER I: not included in any glyphset definition</li>
<li>U+FF73 HALFWIDTH KATAKANA LETTER U: not included in any glyphset definition</li>
<li>U+FF74 HALFWIDTH KATAKANA LETTER E: not included in any glyphset definition</li>
<li>U+FF75 HALFWIDTH KATAKANA LETTER O: not included in any glyphset definition</li>
<li>U+FF76 HALFWIDTH KATAKANA LETTER KA: not included in any glyphset definition</li>
<li>U+FF77 HALFWIDTH KATAKANA LETTER KI: not included in any glyphset definition</li>
<li>U+FF78 HALFWIDTH KATAKANA LETTER KU: not included in any glyphset definition</li>
<li>U+FF79 HALFWIDTH KATAKANA LETTER KE: not included in any glyphset definition</li>
<li>U+FF7A HALFWIDTH KATAKANA LETTER KO: not included in any glyphset definition</li>
<li>U+FF7B HALFWIDTH KATAKANA LETTER SA: not included in any glyphset definition</li>
<li>U+FF7C HALFWIDTH KATAKANA LETTER SI: not included in any glyphset definition</li>
<li>U+FF7D HALFWIDTH KATAKANA LETTER SU: not included in any glyphset definition</li>
<li>U+FF7E HALFWIDTH KATAKANA LETTER SE: not included in any glyphset definition</li>
<li>U+FF7F HALFWIDTH KATAKANA LETTER SO: not included in any glyphset definition</li>
<li>U+FF80 HALFWIDTH KATAKANA LETTER TA: not included in any glyphset definition</li>
<li>U+FF81 HALFWIDTH KATAKANA LETTER TI: not included in any glyphset definition</li>
<li>U+FF82 HALFWIDTH KATAKANA LETTER TU: not included in any glyphset definition</li>
<li>U+FF83 HALFWIDTH KATAKANA LETTER TE: not included in any glyphset definition</li>
<li>U+FF84 HALFWIDTH KATAKANA LETTER TO: not included in any glyphset definition</li>
<li>U+FF85 HALFWIDTH KATAKANA LETTER NA: not included in any glyphset definition</li>
<li>U+FF86 HALFWIDTH KATAKANA LETTER NI: not included in any glyphset definition</li>
<li>U+FF87 HALFWIDTH KATAKANA LETTER NU: not included in any glyphset definition</li>
<li>U+FF88 HALFWIDTH KATAKANA LETTER NE: not included in any glyphset definition</li>
<li>U+FF89 HALFWIDTH KATAKANA LETTER NO: not included in any glyphset definition</li>
<li>U+FF8A HALFWIDTH KATAKANA LETTER HA: not included in any glyphset definition</li>
<li>U+FF8B HALFWIDTH KATAKANA LETTER HI: not included in any glyphset definition</li>
<li>U+FF8C HALFWIDTH KATAKANA LETTER HU: not included in any glyphset definition</li>
<li>U+FF8D HALFWIDTH KATAKANA LETTER HE: not included in any glyphset definition</li>
<li>U+FF8E HALFWIDTH KATAKANA LETTER HO: not included in any glyphset definition</li>
<li>U+FF8F HALFWIDTH KATAKANA LETTER MA: not included in any glyphset definition</li>
<li>U+FF90 HALFWIDTH KATAKANA LETTER MI: not included in any glyphset definition</li>
<li>U+FF91 HALFWIDTH KATAKANA LETTER MU: not included in any glyphset definition</li>
<li>U+FF92 HALFWIDTH KATAKANA LETTER ME: not included in any glyphset definition</li>
<li>U+FF93 HALFWIDTH KATAKANA LETTER MO: not included in any glyphset definition</li>
<li>U+FF94 HALFWIDTH KATAKANA LETTER YA: not included in any glyphset definition</li>
<li>U+FF95 HALFWIDTH KATAKANA LETTER YU: not included in any glyphset definition</li>
<li>U+FF96 HALFWIDTH KATAKANA LETTER YO: not included in any glyphset definition</li>
<li>U+FF97 HALFWIDTH KATAKANA LETTER RA: not included in any glyphset definition</li>
<li>U+FF98 HALFWIDTH KATAKANA LETTER RI: not included in any glyphset definition</li>
<li>U+FF99 HALFWIDTH KATAKANA LETTER RU: not included in any glyphset definition</li>
<li>U+FF9A HALFWIDTH KATAKANA LETTER RE: not included in any glyphset definition</li>
<li>U+FF9B HALFWIDTH KATAKANA LETTER RO: not included in any glyphset definition</li>
<li>U+FF9C HALFWIDTH KATAKANA LETTER WA: not included in any glyphset definition</li>
<li>U+FF9D HALFWIDTH KATAKANA LETTER N: not included in any glyphset definition</li>
<li>U+FF9E HALFWIDTH KATAKANA VOICED SOUND MARK: not included in any glyphset definition</li>
<li>U+FF9F HALFWIDTH KATAKANA SEMI-VOICED SOUND MARK: not included in any glyphset definition</li>
<li>U+FFE2 FULLWIDTH NOT SIGN: not included in any glyphset definition</li>
<li>U+FFE4 FULLWIDTH BROKEN BAR: not included in any glyphset definition</li>
<li>U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition</li>
<li>U+16FF2 : not included in any glyphset definition</li>
<li>U+16FF3 : not included in any glyphset definition</li>
<li>U+20164 CJK UNIFIED IDEOGRAPH-20164: not included in any glyphset definition</li>
<li>U+20676 CJK UNIFIED IDEOGRAPH-20676: not included in any glyphset definition</li>
<li>U+2070E CJK UNIFIED IDEOGRAPH-2070E: not included in any glyphset definition</li>
<li>U+20731 CJK UNIFIED IDEOGRAPH-20731: not included in any glyphset definition</li>
<li>U+20779 CJK UNIFIED IDEOGRAPH-20779: not included in any glyphset definition</li>
<li>U+20B9F CJK UNIFIED IDEOGRAPH-20B9F: not included in any glyphset definition</li>
<li>U+20C53 CJK UNIFIED IDEOGRAPH-20C53: not included in any glyphset definition</li>
<li>U+20C78 CJK UNIFIED IDEOGRAPH-20C78: not included in any glyphset definition</li>
<li>U+20C96 CJK UNIFIED IDEOGRAPH-20C96: not included in any glyphset definition</li>
<li>U+20CCF CJK UNIFIED IDEOGRAPH-20CCF: not included in any glyphset definition</li>
<li>U+20CD0 CJK UNIFIED IDEOGRAPH-20CD0: not included in any glyphset definition</li>
<li>U+20CD5 CJK UNIFIED IDEOGRAPH-20CD5: not included in any glyphset definition</li>
<li>U+20D15 CJK UNIFIED IDEOGRAPH-20D15: not included in any glyphset definition</li>
<li>U+20D7C CJK UNIFIED IDEOGRAPH-20D7C: not included in any glyphset definition</li>
<li>U+20D7F CJK UNIFIED IDEOGRAPH-20D7F: not included in any glyphset definition</li>
<li>U+20E0E CJK UNIFIED IDEOGRAPH-20E0E: not included in any glyphset definition</li>
<li>U+20E0F CJK UNIFIED IDEOGRAPH-20E0F: not included in any glyphset definition</li>
<li>U+20E77 CJK UNIFIED IDEOGRAPH-20E77: not included in any glyphset definition</li>
<li>U+20E9D CJK UNIFIED IDEOGRAPH-20E9D: not included in any glyphset definition</li>
<li>U+20EA2 CJK UNIFIED IDEOGRAPH-20EA2: not included in any glyphset definition</li>
<li>U+20ED7 CJK UNIFIED IDEOGRAPH-20ED7: not included in any glyphset definition</li>
<li>U+20EF9 CJK UNIFIED IDEOGRAPH-20EF9: not included in any glyphset definition</li>
<li>U+20EFA CJK UNIFIED IDEOGRAPH-20EFA: not included in any glyphset definition</li>
<li>U+20F2D CJK UNIFIED IDEOGRAPH-20F2D: not included in any glyphset definition</li>
<li>U+20F2E CJK UNIFIED IDEOGRAPH-20F2E: not included in any glyphset definition</li>
<li>U+20F4C CJK UNIFIED IDEOGRAPH-20F4C: not included in any glyphset definition</li>
<li>U+20FB4 CJK UNIFIED IDEOGRAPH-20FB4: not included in any glyphset definition</li>
<li>U+20FBC CJK UNIFIED IDEOGRAPH-20FBC: not included in any glyphset definition</li>
<li>U+20FEA CJK UNIFIED IDEOGRAPH-20FEA: not included in any glyphset definition</li>
<li>U+2105C CJK UNIFIED IDEOGRAPH-2105C: not included in any glyphset definition</li>
<li>U+2106F CJK UNIFIED IDEOGRAPH-2106F: not included in any glyphset definition</li>
<li>U+21075 CJK UNIFIED IDEOGRAPH-21075: not included in any glyphset definition</li>
<li>U+21076 CJK UNIFIED IDEOGRAPH-21076: not included in any glyphset definition</li>
<li>U+2107B CJK UNIFIED IDEOGRAPH-2107B: not included in any glyphset definition</li>
<li>U+210C1 CJK UNIFIED IDEOGRAPH-210C1: not included in any glyphset definition</li>
<li>U+210C9 CJK UNIFIED IDEOGRAPH-210C9: not included in any glyphset definition</li>
<li>U+211D9 CJK UNIFIED IDEOGRAPH-211D9: not included in any glyphset definition</li>
<li>U+2139A CJK UNIFIED IDEOGRAPH-2139A: not included in any glyphset definition</li>
<li>U+21413 CJK UNIFIED IDEOGRAPH-21413: not included in any glyphset definition</li>
<li>U+2144D CJK UNIFIED IDEOGRAPH-2144D: not included in any glyphset definition</li>
<li>U+220C7 CJK UNIFIED IDEOGRAPH-220C7: not included in any glyphset definition</li>
<li>U+227B5 CJK UNIFIED IDEOGRAPH-227B5: not included in any glyphset definition</li>
<li>U+22AD5 CJK UNIFIED IDEOGRAPH-22AD5: not included in any glyphset definition</li>
<li>U+22B43 CJK UNIFIED IDEOGRAPH-22B43: not included in any glyphset definition</li>
<li>U+22BCA CJK UNIFIED IDEOGRAPH-22BCA: not included in any glyphset definition</li>
<li>U+22C51 CJK UNIFIED IDEOGRAPH-22C51: not included in any glyphset definition</li>
<li>U+22C55 CJK UNIFIED IDEOGRAPH-22C55: not included in any glyphset definition</li>
<li>U+22CC2 CJK UNIFIED IDEOGRAPH-22CC2: not included in any glyphset definition</li>
<li>U+22D08 CJK UNIFIED IDEOGRAPH-22D08: not included in any glyphset definition</li>
<li>U+22D4C CJK UNIFIED IDEOGRAPH-22D4C: not included in any glyphset definition</li>
<li>U+22D67 CJK UNIFIED IDEOGRAPH-22D67: not included in any glyphset definition</li>
<li>U+22EB3 CJK UNIFIED IDEOGRAPH-22EB3: not included in any glyphset definition</li>
<li>U+235CB CJK UNIFIED IDEOGRAPH-235CB: not included in any glyphset definition</li>
<li>U+23C97 CJK UNIFIED IDEOGRAPH-23C97: not included in any glyphset definition</li>
<li>U+23C98 CJK UNIFIED IDEOGRAPH-23C98: not included in any glyphset definition</li>
<li>U+23CB7 CJK UNIFIED IDEOGRAPH-23CB7: not included in any glyphset definition</li>
<li>U+23E23 CJK UNIFIED IDEOGRAPH-23E23: not included in any glyphset definition</li>
<li>U+244D3 CJK UNIFIED IDEOGRAPH-244D3: not included in any glyphset definition</li>
<li>U+249DB CJK UNIFIED IDEOGRAPH-249DB: not included in any glyphset definition</li>
<li>U+24A7D CJK UNIFIED IDEOGRAPH-24A7D: not included in any glyphset definition</li>
<li>U+24AC9 CJK UNIFIED IDEOGRAPH-24AC9: not included in any glyphset definition</li>
<li>U+24DB8 CJK UNIFIED IDEOGRAPH-24DB8: not included in any glyphset definition</li>
<li>U+24DEA CJK UNIFIED IDEOGRAPH-24DEA: not included in any glyphset definition</li>
<li>U+2512B CJK UNIFIED IDEOGRAPH-2512B: not included in any glyphset definition</li>
<li>U+25532 CJK UNIFIED IDEOGRAPH-25532: not included in any glyphset definition</li>
<li>U+25562 CJK UNIFIED IDEOGRAPH-25562: not included in any glyphset definition</li>
<li>U+255A8 CJK UNIFIED IDEOGRAPH-255A8: not included in any glyphset definition</li>
<li>U+255FD CJK UNIFIED IDEOGRAPH-255FD: not included in any glyphset definition</li>
<li>U+25ED7 CJK UNIFIED IDEOGRAPH-25ED7: not included in any glyphset definition</li>
<li>U+26221 CJK UNIFIED IDEOGRAPH-26221: not included in any glyphset definition</li>
<li>U+26258 CJK UNIFIED IDEOGRAPH-26258: not included in any glyphset definition</li>
<li>U+2648D CJK UNIFIED IDEOGRAPH-2648D: not included in any glyphset definition</li>
<li>U+26676 CJK UNIFIED IDEOGRAPH-26676: not included in any glyphset definition</li>
<li>U+2677C CJK UNIFIED IDEOGRAPH-2677C: not included in any glyphset definition</li>
<li>U+267CC CJK UNIFIED IDEOGRAPH-267CC: not included in any glyphset definition</li>
<li>U+269F2 CJK UNIFIED IDEOGRAPH-269F2: not included in any glyphset definition</li>
<li>U+269FA CJK UNIFIED IDEOGRAPH-269FA: not included in any glyphset definition</li>
<li>U+26B5C CJK UNIFIED IDEOGRAPH-26B5C: not included in any glyphset definition</li>
<li>U+26C21 CJK UNIFIED IDEOGRAPH-26C21: not included in any glyphset definition</li>
<li>U+27A3E CJK UNIFIED IDEOGRAPH-27A3E: not included in any glyphset definition</li>
<li>U+27FF9 CJK UNIFIED IDEOGRAPH-27FF9: not included in any glyphset definition</li>
<li>U+2815D CJK UNIFIED IDEOGRAPH-2815D: not included in any glyphset definition</li>
<li>U+28207 CJK UNIFIED IDEOGRAPH-28207: not included in any glyphset definition</li>
<li>U+282E2 CJK UNIFIED IDEOGRAPH-282E2: not included in any glyphset definition</li>
<li>U+28408 CJK UNIFIED IDEOGRAPH-28408: not included in any glyphset definition</li>
<li>U+28678 CJK UNIFIED IDEOGRAPH-28678: not included in any glyphset definition</li>
<li>U+28695 CJK UNIFIED IDEOGRAPH-28695: not included in any glyphset definition</li>
<li>U+287E0 CJK UNIFIED IDEOGRAPH-287E0: not included in any glyphset definition</li>
<li>U+289C0 CJK UNIFIED IDEOGRAPH-289C0: not included in any glyphset definition</li>
<li>U+28A0F CJK UNIFIED IDEOGRAPH-28A0F: not included in any glyphset definition</li>
<li>U+28B46 CJK UNIFIED IDEOGRAPH-28B46: not included in any glyphset definition</li>
<li>U+28B49 CJK UNIFIED IDEOGRAPH-28B49: not included in any glyphset definition</li>
<li>U+28B4E CJK UNIFIED IDEOGRAPH-28B4E: not included in any glyphset definition</li>
<li>U+28C47 CJK UNIFIED IDEOGRAPH-28C47: not included in any glyphset definition</li>
<li>U+28C4F CJK UNIFIED IDEOGRAPH-28C4F: not included in any glyphset definition</li>
<li>U+28C51 CJK UNIFIED IDEOGRAPH-28C51: not included in any glyphset definition</li>
<li>U+28C54 CJK UNIFIED IDEOGRAPH-28C54: not included in any glyphset definition</li>
<li>U+28CCA CJK UNIFIED IDEOGRAPH-28CCA: not included in any glyphset definition</li>
<li>U+28CCD CJK UNIFIED IDEOGRAPH-28CCD: not included in any glyphset definition</li>
<li>U+28CD2 CJK UNIFIED IDEOGRAPH-28CD2: not included in any glyphset definition</li>
<li>U+28E99 CJK UNIFIED IDEOGRAPH-28E99: not included in any glyphset definition</li>
<li>U+29D98 CJK UNIFIED IDEOGRAPH-29D98: not included in any glyphset definition</li>
<li>U+29F7E CJK UNIFIED IDEOGRAPH-29F7E: not included in any glyphset definition</li>
<li>U+29F83 CJK UNIFIED IDEOGRAPH-29F83: not included in any glyphset definition</li>
<li>U+29F8C CJK UNIFIED IDEOGRAPH-29F8C: not included in any glyphset definition</li>
<li>U+2A7DD CJK UNIFIED IDEOGRAPH-2A7DD: not included in any glyphset definition</li>
<li>U+2A8FB CJK UNIFIED IDEOGRAPH-2A8FB: not included in any glyphset definition</li>
<li>U+2A917 CJK UNIFIED IDEOGRAPH-2A917: not included in any glyphset definition</li>
<li>U+2AA30 CJK UNIFIED IDEOGRAPH-2AA30: not included in any glyphset definition</li>
<li>U+2AA36 CJK UNIFIED IDEOGRAPH-2AA36: not included in any glyphset definition</li>
<li>U+2AA58 CJK UNIFIED IDEOGRAPH-2AA58: not included in any glyphset definition</li>
<li>U+2AFA2 CJK UNIFIED IDEOGRAPH-2AFA2: not included in any glyphset definition</li>
<li>U+2B127 CJK UNIFIED IDEOGRAPH-2B127: not included in any glyphset definition</li>
<li>U+2B128 CJK UNIFIED IDEOGRAPH-2B128: not included in any glyphset definition</li>
<li>U+2B137 CJK UNIFIED IDEOGRAPH-2B137: not included in any glyphset definition</li>
<li>U+2B138 CJK UNIFIED IDEOGRAPH-2B138: not included in any glyphset definition</li>
<li>U+2B1ED CJK UNIFIED IDEOGRAPH-2B1ED: not included in any glyphset definition</li>
<li>U+2B300 CJK UNIFIED IDEOGRAPH-2B300: not included in any glyphset definition</li>
<li>U+2B363 CJK UNIFIED IDEOGRAPH-2B363: not included in any glyphset definition</li>
<li>U+2B36F CJK UNIFIED IDEOGRAPH-2B36F: not included in any glyphset definition</li>
<li>U+2B372 CJK UNIFIED IDEOGRAPH-2B372: not included in any glyphset definition</li>
<li>U+2B37D CJK UNIFIED IDEOGRAPH-2B37D: not included in any glyphset definition</li>
<li>U+2B404 CJK UNIFIED IDEOGRAPH-2B404: not included in any glyphset definition</li>
<li>U+2B410 CJK UNIFIED IDEOGRAPH-2B410: not included in any glyphset definition</li>
<li>U+2B413 CJK UNIFIED IDEOGRAPH-2B413: not included in any glyphset definition</li>
<li>U+2B461 CJK UNIFIED IDEOGRAPH-2B461: not included in any glyphset definition</li>
<li>U+2B4E7 CJK UNIFIED IDEOGRAPH-2B4E7: not included in any glyphset definition</li>
<li>U+2B4EF CJK UNIFIED IDEOGRAPH-2B4EF: not included in any glyphset definition</li>
<li>U+2B4F6 CJK UNIFIED IDEOGRAPH-2B4F6: not included in any glyphset definition</li>
<li>U+2B4F9 CJK UNIFIED IDEOGRAPH-2B4F9: not included in any glyphset definition</li>
<li>U+2B50D CJK UNIFIED IDEOGRAPH-2B50D: not included in any glyphset definition</li>
<li>U+2B50E CJK UNIFIED IDEOGRAPH-2B50E: not included in any glyphset definition</li>
<li>U+2B536 CJK UNIFIED IDEOGRAPH-2B536: not included in any glyphset definition</li>
<li>U+2B5AE CJK UNIFIED IDEOGRAPH-2B5AE: not included in any glyphset definition</li>
<li>U+2B5AF CJK UNIFIED IDEOGRAPH-2B5AF: not included in any glyphset definition</li>
<li>U+2B5B3 CJK UNIFIED IDEOGRAPH-2B5B3: not included in any glyphset definition</li>
<li>U+2B5E7 CJK UNIFIED IDEOGRAPH-2B5E7: not included in any glyphset definition</li>
<li>U+2B5F4 CJK UNIFIED IDEOGRAPH-2B5F4: not included in any glyphset definition</li>
<li>U+2B61C CJK UNIFIED IDEOGRAPH-2B61C: not included in any glyphset definition</li>
<li>U+2B61D CJK UNIFIED IDEOGRAPH-2B61D: not included in any glyphset definition</li>
<li>U+2B626 CJK UNIFIED IDEOGRAPH-2B626: not included in any glyphset definition</li>
<li>U+2B627 CJK UNIFIED IDEOGRAPH-2B627: not included in any glyphset definition</li>
<li>U+2B628 CJK UNIFIED IDEOGRAPH-2B628: not included in any glyphset definition</li>
<li>U+2B62A CJK UNIFIED IDEOGRAPH-2B62A: not included in any glyphset definition</li>
<li>U+2B62C CJK UNIFIED IDEOGRAPH-2B62C: not included in any glyphset definition</li>
<li>U+2B695 CJK UNIFIED IDEOGRAPH-2B695: not included in any glyphset definition</li>
<li>U+2B696 CJK UNIFIED IDEOGRAPH-2B696: not included in any glyphset definition</li>
<li>U+2B6AD CJK UNIFIED IDEOGRAPH-2B6AD: not included in any glyphset definition</li>
<li>U+2B6ED CJK UNIFIED IDEOGRAPH-2B6ED: not included in any glyphset definition</li>
<li>U+2B7A9 CJK UNIFIED IDEOGRAPH-2B7A9: not included in any glyphset definition</li>
<li>U+2B7C5 CJK UNIFIED IDEOGRAPH-2B7C5: not included in any glyphset definition</li>
<li>U+2B7E6 CJK UNIFIED IDEOGRAPH-2B7E6: not included in any glyphset definition</li>
<li>U+2B7F7 CJK UNIFIED IDEOGRAPH-2B7F7: not included in any glyphset definition</li>
<li>U+2B7F9 CJK UNIFIED IDEOGRAPH-2B7F9: not included in any glyphset definition</li>
<li>U+2B7FC CJK UNIFIED IDEOGRAPH-2B7FC: not included in any glyphset definition</li>
<li>U+2B806 CJK UNIFIED IDEOGRAPH-2B806: not included in any glyphset definition</li>
<li>U+2B80A CJK UNIFIED IDEOGRAPH-2B80A: not included in any glyphset definition</li>
<li>U+2B81C CJK UNIFIED IDEOGRAPH-2B81C: not included in any glyphset definition</li>
<li>U+2B8B8 CJK UNIFIED IDEOGRAPH-2B8B8: not included in any glyphset definition</li>
<li>U+2BAC7 CJK UNIFIED IDEOGRAPH-2BAC7: not included in any glyphset definition</li>
<li>U+2BB5F CJK UNIFIED IDEOGRAPH-2BB5F: not included in any glyphset definition</li>
<li>U+2BB62 CJK UNIFIED IDEOGRAPH-2BB62: not included in any glyphset definition</li>
<li>U+2BB7C CJK UNIFIED IDEOGRAPH-2BB7C: not included in any glyphset definition</li>
<li>U+2BB83 CJK UNIFIED IDEOGRAPH-2BB83: not included in any glyphset definition</li>
<li>U+2BC1B CJK UNIFIED IDEOGRAPH-2BC1B: not included in any glyphset definition</li>
<li>U+2BD77 CJK UNIFIED IDEOGRAPH-2BD77: not included in any glyphset definition</li>
<li>U+2BD87 CJK UNIFIED IDEOGRAPH-2BD87: not included in any glyphset definition</li>
<li>U+2BDF7 CJK UNIFIED IDEOGRAPH-2BDF7: not included in any glyphset definition</li>
<li>U+2BE29 CJK UNIFIED IDEOGRAPH-2BE29: not included in any glyphset definition</li>
<li>U+2C029 CJK UNIFIED IDEOGRAPH-2C029: not included in any glyphset definition</li>
<li>U+2C02A CJK UNIFIED IDEOGRAPH-2C02A: not included in any glyphset definition</li>
<li>U+2C0A9 CJK UNIFIED IDEOGRAPH-2C0A9: not included in any glyphset definition</li>
<li>U+2C0CA CJK UNIFIED IDEOGRAPH-2C0CA: not included in any glyphset definition</li>
<li>U+2C1D5 CJK UNIFIED IDEOGRAPH-2C1D5: not included in any glyphset definition</li>
<li>U+2C1D9 CJK UNIFIED IDEOGRAPH-2C1D9: not included in any glyphset definition</li>
<li>U+2C1F9 CJK UNIFIED IDEOGRAPH-2C1F9: not included in any glyphset definition</li>
<li>U+2C27C CJK UNIFIED IDEOGRAPH-2C27C: not included in any glyphset definition</li>
<li>U+2C288 CJK UNIFIED IDEOGRAPH-2C288: not included in any glyphset definition</li>
<li>U+2C2A4 CJK UNIFIED IDEOGRAPH-2C2A4: not included in any glyphset definition</li>
<li>U+2C317 CJK UNIFIED IDEOGRAPH-2C317: not included in any glyphset definition</li>
<li>U+2C35B CJK UNIFIED IDEOGRAPH-2C35B: not included in any glyphset definition</li>
<li>U+2C361 CJK UNIFIED IDEOGRAPH-2C361: not included in any glyphset definition</li>
<li>U+2C364 CJK UNIFIED IDEOGRAPH-2C364: not included in any glyphset definition</li>
<li>U+2C488 CJK UNIFIED IDEOGRAPH-2C488: not included in any glyphset definition</li>
<li>U+2C494 CJK UNIFIED IDEOGRAPH-2C494: not included in any glyphset definition</li>
<li>U+2C497 CJK UNIFIED IDEOGRAPH-2C497: not included in any glyphset definition</li>
<li>U+2C542 CJK UNIFIED IDEOGRAPH-2C542: not included in any glyphset definition</li>
<li>U+2C613 CJK UNIFIED IDEOGRAPH-2C613: not included in any glyphset definition</li>
<li>U+2C618 CJK UNIFIED IDEOGRAPH-2C618: not included in any glyphset definition</li>
<li>U+2C621 CJK UNIFIED IDEOGRAPH-2C621: not included in any glyphset definition</li>
<li>U+2C629 CJK UNIFIED IDEOGRAPH-2C629: not included in any glyphset definition</li>
<li>U+2C62B CJK UNIFIED IDEOGRAPH-2C62B: not included in any glyphset definition</li>
<li>U+2C62C CJK UNIFIED IDEOGRAPH-2C62C: not included in any glyphset definition</li>
<li>U+2C62D CJK UNIFIED IDEOGRAPH-2C62D: not included in any glyphset definition</li>
<li>U+2C62F CJK UNIFIED IDEOGRAPH-2C62F: not included in any glyphset definition</li>
<li>U+2C642 CJK UNIFIED IDEOGRAPH-2C642: not included in any glyphset definition</li>
<li>U+2C64A CJK UNIFIED IDEOGRAPH-2C64A: not included in any glyphset definition</li>
<li>U+2C64B CJK UNIFIED IDEOGRAPH-2C64B: not included in any glyphset definition</li>
<li>U+2C72C CJK UNIFIED IDEOGRAPH-2C72C: not included in any glyphset definition</li>
<li>U+2C72F CJK UNIFIED IDEOGRAPH-2C72F: not included in any glyphset definition</li>
<li>U+2C79F CJK UNIFIED IDEOGRAPH-2C79F: not included in any glyphset definition</li>
<li>U+2C7C1 CJK UNIFIED IDEOGRAPH-2C7C1: not included in any glyphset definition</li>
<li>U+2C7FD CJK UNIFIED IDEOGRAPH-2C7FD: not included in any glyphset definition</li>
<li>U+2C8D9 CJK UNIFIED IDEOGRAPH-2C8D9: not included in any glyphset definition</li>
<li>U+2C8DE CJK UNIFIED IDEOGRAPH-2C8DE: not included in any glyphset definition</li>
<li>U+2C8E1 CJK UNIFIED IDEOGRAPH-2C8E1: not included in any glyphset definition</li>
<li>U+2C8F3 CJK UNIFIED IDEOGRAPH-2C8F3: not included in any glyphset definition</li>
<li>U+2C907 CJK UNIFIED IDEOGRAPH-2C907: not included in any glyphset definition</li>
<li>U+2C90A CJK UNIFIED IDEOGRAPH-2C90A: not included in any glyphset definition</li>
<li>U+2C91D CJK UNIFIED IDEOGRAPH-2C91D: not included in any glyphset definition</li>
<li>U+2CA02 CJK UNIFIED IDEOGRAPH-2CA02: not included in any glyphset definition</li>
<li>U+2CA0E CJK UNIFIED IDEOGRAPH-2CA0E: not included in any glyphset definition</li>
<li>U+2CA7D CJK UNIFIED IDEOGRAPH-2CA7D: not included in any glyphset definition</li>
<li>U+2CAA9 CJK UNIFIED IDEOGRAPH-2CAA9: not included in any glyphset definition</li>
<li>U+2CB29 CJK UNIFIED IDEOGRAPH-2CB29: not included in any glyphset definition</li>
<li>U+2CB2D CJK UNIFIED IDEOGRAPH-2CB2D: not included in any glyphset definition</li>
<li>U+2CB2E CJK UNIFIED IDEOGRAPH-2CB2E: not included in any glyphset definition</li>
<li>U+2CB31 CJK UNIFIED IDEOGRAPH-2CB31: not included in any glyphset definition</li>
<li>U+2CB38 CJK UNIFIED IDEOGRAPH-2CB38: not included in any glyphset definition</li>
<li>U+2CB39 CJK UNIFIED IDEOGRAPH-2CB39: not included in any glyphset definition</li>
<li>U+2CB3B CJK UNIFIED IDEOGRAPH-2CB3B: not included in any glyphset definition</li>
<li>U+2CB3F CJK UNIFIED IDEOGRAPH-2CB3F: not included in any glyphset definition</li>
<li>U+2CB41 CJK UNIFIED IDEOGRAPH-2CB41: not included in any glyphset definition</li>
<li>U+2CB4A CJK UNIFIED IDEOGRAPH-2CB4A: not included in any glyphset definition</li>
<li>U+2CB4E CJK UNIFIED IDEOGRAPH-2CB4E: not included in any glyphset definition</li>
<li>U+2CB5A CJK UNIFIED IDEOGRAPH-2CB5A: not included in any glyphset definition</li>
<li>U+2CB5B CJK UNIFIED IDEOGRAPH-2CB5B: not included in any glyphset definition</li>
<li>U+2CB64 CJK UNIFIED IDEOGRAPH-2CB64: not included in any glyphset definition</li>
<li>U+2CB69 CJK UNIFIED IDEOGRAPH-2CB69: not included in any glyphset definition</li>
<li>U+2CB6C CJK UNIFIED IDEOGRAPH-2CB6C: not included in any glyphset definition</li>
<li>U+2CB6F CJK UNIFIED IDEOGRAPH-2CB6F: not included in any glyphset definition</li>
<li>U+2CB73 CJK UNIFIED IDEOGRAPH-2CB73: not included in any glyphset definition</li>
<li>U+2CB76 CJK UNIFIED IDEOGRAPH-2CB76: not included in any glyphset definition</li>
<li>U+2CB78 CJK UNIFIED IDEOGRAPH-2CB78: not included in any glyphset definition</li>
<li>U+2CB7C CJK UNIFIED IDEOGRAPH-2CB7C: not included in any glyphset definition</li>
<li>U+2CBB1 CJK UNIFIED IDEOGRAPH-2CBB1: not included in any glyphset definition</li>
<li>U+2CBBF CJK UNIFIED IDEOGRAPH-2CBBF: not included in any glyphset definition</li>
<li>U+2CBC0 CJK UNIFIED IDEOGRAPH-2CBC0: not included in any glyphset definition</li>
<li>U+2CBCE CJK UNIFIED IDEOGRAPH-2CBCE: not included in any glyphset definition</li>
<li>U+2CC56 CJK UNIFIED IDEOGRAPH-2CC56: not included in any glyphset definition</li>
<li>U+2CC5F CJK UNIFIED IDEOGRAPH-2CC5F: not included in any glyphset definition</li>
<li>U+2CCF5 CJK UNIFIED IDEOGRAPH-2CCF5: not included in any glyphset definition</li>
<li>U+2CCF6 CJK UNIFIED IDEOGRAPH-2CCF6: not included in any glyphset definition</li>
<li>U+2CCFD CJK UNIFIED IDEOGRAPH-2CCFD: not included in any glyphset definition</li>
<li>U+2CCFF CJK UNIFIED IDEOGRAPH-2CCFF: not included in any glyphset definition</li>
<li>U+2CD02 CJK UNIFIED IDEOGRAPH-2CD02: not included in any glyphset definition</li>
<li>U+2CD03 CJK UNIFIED IDEOGRAPH-2CD03: not included in any glyphset definition</li>
<li>U+2CD0A CJK UNIFIED IDEOGRAPH-2CD0A: not included in any glyphset definition</li>
<li>U+2CD8B CJK UNIFIED IDEOGRAPH-2CD8B: not included in any glyphset definition</li>
<li>U+2CD8D CJK UNIFIED IDEOGRAPH-2CD8D: not included in any glyphset definition</li>
<li>U+2CD8F CJK UNIFIED IDEOGRAPH-2CD8F: not included in any glyphset definition</li>
<li>U+2CD90 CJK UNIFIED IDEOGRAPH-2CD90: not included in any glyphset definition</li>
<li>U+2CD9F CJK UNIFIED IDEOGRAPH-2CD9F: not included in any glyphset definition</li>
<li>U+2CDA0 CJK UNIFIED IDEOGRAPH-2CDA0: not included in any glyphset definition</li>
<li>U+2CDA8 CJK UNIFIED IDEOGRAPH-2CDA8: not included in any glyphset definition</li>
<li>U+2CDAD CJK UNIFIED IDEOGRAPH-2CDAD: not included in any glyphset definition</li>
<li>U+2CDAE CJK UNIFIED IDEOGRAPH-2CDAE: not included in any glyphset definition</li>
<li>U+2CDD5 CJK UNIFIED IDEOGRAPH-2CDD5: not included in any glyphset definition</li>
<li>U+2CE18 CJK UNIFIED IDEOGRAPH-2CE18: not included in any glyphset definition</li>
<li>U+2CE1A CJK UNIFIED IDEOGRAPH-2CE1A: not included in any glyphset definition</li>
<li>U+2CE23 CJK UNIFIED IDEOGRAPH-2CE23: not included in any glyphset definition</li>
<li>U+2CE26 CJK UNIFIED IDEOGRAPH-2CE26: not included in any glyphset definition</li>
<li>U+2CE2A CJK UNIFIED IDEOGRAPH-2CE2A: not included in any glyphset definition</li>
<li>U+2CE7C CJK UNIFIED IDEOGRAPH-2CE7C: not included in any glyphset definition</li>
<li>U+2CE88 CJK UNIFIED IDEOGRAPH-2CE88: not included in any glyphset definition</li>
<li>U+2CE93 CJK UNIFIED IDEOGRAPH-2CE93: not included in any glyphset definition</li>
<li>U+FFFFD : not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>chinese-hongkong</code>, <code>chinese-simplified</code>, <code>chinese-traditional</code>, <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>japanese</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ i̍ i̓ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ і́ ḭ̀ ḭ́ ḭ̄ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̇ i̎ i̒ i̤̇ i̤̊ i̤̋ i̤̍ i̤̎ i̤̒ i̤̓ i̥̇ i̥̊ i̥̋ i̥̍ i̥̎ i̥̒ i̥̓ i̦̇ i̦̊ i̦̋</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* u222C (U+222C) has a counter-clockwise outer contour

* u222C (U+222C) has a path with no bounds (probably a single point)

* u222D (U+222D) has a counter-clockwise outer contour

* u222D (U+222D) has a path with no bounds (probably a single point)

* u28C47 (U+28C47) has a counter-clockwise outer contour

* u28C4F (U+28C4F) has a counter-clockwise outer contour

* u3010 (U+3010) has a counter-clockwise outer contour

* u3011 (U+3011) has a counter-clockwise outer contour

* u73CC (U+73CC) has a counter-clockwise outer contour

* u73CC (U+73CC) has a counter-clockwise outer contour

* u73CC (U+73CC) has a counter-clockwise outer contour

* u73CC (U+73CC) has a counter-clockwise outer contour

* u939B (U+939B) has a counter-clockwise outer contour

* u939B (U+939B) has a counter-clockwise outer contour

* u9548 (U+9548) has a counter-clockwise outer contour

* uFE3B (U+FE3B) has a counter-clockwise outer contour

* uFE3C (U+FE3C) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* paragraph (U+00B6): L&lt;&lt;245.0,-89.0&gt;--&lt;244.0,695.0&gt;&gt;/L&lt;&lt;244.0,695.0&gt;--&lt;244.0,227.0&gt;&gt; = 0.07308131178608729

* u023A (U+023A): L&lt;&lt;299.0,583.0&gt;--&lt;222.0,294.0&gt;&gt;/L&lt;&lt;222.0,294.0&gt;--&lt;310.0,542.0&gt;&gt; = 4.617578009533678

* u1E11 (U+1E11): B&lt;&lt;433.0,-93.0&gt;-&lt;422.0,-87.0&gt;-&lt;405.0,-84.0&gt;&gt;/L&lt;&lt;405.0,-84.0&gt;--&lt;405.0,-84.0&gt;&gt; = 10.007979801441312

* u20FB4 (U+20FB4): L&lt;&lt;401.0,-56.0&gt;--&lt;401.0,255.0&gt;&gt;/L&lt;&lt;401.0,255.0&gt;--&lt;359.0,89.0&gt;&gt; = 14.198554023863164

* u2167 (U+2167): L&lt;&lt;471.0,54.0&gt;--&lt;471.0,689.0&gt;&gt;/L&lt;&lt;471.0,689.0&gt;--&lt;310.0,3.0&gt;&gt; = 13.207928462779101

* u22C51 (U+22C51): L&lt;&lt;899.0,441.0&gt;--&lt;840.0,426.0&gt;&gt;/L&lt;&lt;840.0,426.0&gt;--&lt;853.0,426.0&gt;&gt; = 14.264512298079882

* u24AC9 (U+24AC9): B&lt;&lt;486.0,830.0&gt;-&lt;486.0,727.0&gt;-&lt;480.0,666.0&gt;&gt;/L&lt;&lt;480.0,666.0&gt;--&lt;516.0,771.0&gt;&gt; = 13.307063825924383

* u255A8 (U+255A8): L&lt;&lt;418.0,201.0&gt;--&lt;419.0,189.0&gt;&gt;/L&lt;&lt;419.0,189.0&gt;--&lt;419.0,235.0&gt;&gt; = 4.763641690726143

* u255A8 (U+255A8): L&lt;&lt;419.0,187.0&gt;--&lt;418.0,201.0&gt;&gt;/L&lt;&lt;418.0,201.0&gt;--&lt;419.0,189.0&gt;&gt; = 0.6780249107510569

* u269F2 (U+269F2): L&lt;&lt;855.0,109.0&gt;--&lt;854.0,111.0&gt;&gt;/L&lt;&lt;854.0,111.0&gt;--&lt;889.0,-11.0&gt;&gt; = 10.557646880978115

* u289C0 (U+289C0): L&lt;&lt;549.0,-58.0&gt;--&lt;549.0,230.0&gt;&gt;/L&lt;&lt;549.0,230.0&gt;--&lt;519.0,108.0&gt;&gt; = 13.81502534126161

* u28B49 (U+28B49): L&lt;&lt;74.0,255.0&gt;--&lt;486.0,410.0&gt;&gt;/L&lt;&lt;486.0,410.0&gt;--&lt;412.0,398.0&gt;&gt; = 11.405955406137233

* u28C47 (U+28C47): L&lt;&lt;66.0,487.0&gt;--&lt;154.0,479.0&gt;&gt;/L&lt;&lt;154.0,479.0&gt;--&lt;144.0,479.0&gt;&gt; = 5.1944289077348

* u28C4F (U+28C4F): L&lt;&lt;66.0,487.0&gt;--&lt;154.0,479.0&gt;&gt;/L&lt;&lt;154.0,479.0&gt;--&lt;144.0,479.0&gt;&gt; = 5.1944289077348

* u28C51 (U+28C51): L&lt;&lt;144.0,479.0&gt;--&lt;154.0,479.0&gt;&gt;/L&lt;&lt;154.0,479.0&gt;--&lt;66.0,487.0&gt;&gt; = 5.1944289077348

* u2B50D (U+2B50D): L&lt;&lt;146.0,479.0&gt;--&lt;156.0,479.0&gt;&gt;/L&lt;&lt;156.0,479.0&gt;--&lt;69.0,487.0&gt;&gt; = 5.253802751262233

* u2B50E (U+2B50E): L&lt;&lt;138.0,479.0&gt;--&lt;148.0,479.0&gt;&gt;/L&lt;&lt;148.0,479.0&gt;--&lt;60.0,487.0&gt;&gt; = 5.1944289077348

* u2C288 (U+2C288): B&lt;&lt;290.0,797.0&gt;-&lt;290.0,633.0&gt;-&lt;280.0,486.0&gt;&gt;/L&lt;&lt;280.0,486.0&gt;--&lt;348.0,704.0&gt;&gt; = 13.432413245890185

* u2C2A4 (U+2C2A4): B&lt;&lt;297.0,810.0&gt;-&lt;297.0,646.0&gt;-&lt;287.0,499.0&gt;&gt;/L&lt;&lt;287.0,499.0&gt;--&lt;357.0,717.0&gt;&gt; = 13.91019575741011

* u2C361 (U+2C361): L&lt;&lt;710.0,81.0&gt;--&lt;766.0,90.0&gt;&gt;/L&lt;&lt;766.0,90.0&gt;--&lt;559.0,90.0&gt;&gt; = 9.130176482278666

* u2C361 (U+2C361): L&lt;&lt;826.0,28.0&gt;--&lt;781.0,22.0&gt;&gt;/L&lt;&lt;781.0,22.0&gt;--&lt;926.0,22.0&gt;&gt; = 7.594643368591397

* u2C62D (U+2C62D): L&lt;&lt;499.0,-71.0&gt;--&lt;499.0,323.0&gt;&gt;/L&lt;&lt;499.0,323.0&gt;--&lt;441.0,11.0&gt;&gt; = 10.530927852674804

* u2C62D (U+2C62D): L&lt;&lt;732.0,-71.0&gt;--&lt;732.0,276.0&gt;&gt;/L&lt;&lt;732.0,276.0&gt;--&lt;680.0,-5.0&gt;&gt; = 10.48417539652899

* u2C62D (U+2C62D): L&lt;&lt;880.0,-5.0&gt;--&lt;817.0,278.0&gt;&gt;/L&lt;&lt;817.0,278.0&gt;--&lt;817.0,-71.0&gt;&gt; = 12.550242717322131

* u2C91D (U+2C91D): L&lt;&lt;813.0,315.0&gt;--&lt;835.0,319.0&gt;&gt;/L&lt;&lt;835.0,319.0&gt;--&lt;826.0,319.0&gt;&gt; = 10.304846468766044

* u2CB38 (U+2CB38): L&lt;&lt;146.0,479.0&gt;--&lt;156.0,479.0&gt;&gt;/L&lt;&lt;156.0,479.0&gt;--&lt;66.0,487.0&gt;&gt; = 5.0796078600145425

* u2CB41 (U+2CB41): L&lt;&lt;146.0,479.0&gt;--&lt;156.0,479.0&gt;&gt;/L&lt;&lt;156.0,479.0&gt;--&lt;66.0,487.0&gt;&gt; = 5.0796078600145425

* u2CB4E (U+2CB4E): L&lt;&lt;151.0,479.0&gt;--&lt;161.0,479.0&gt;&gt;/L&lt;&lt;161.0,479.0&gt;--&lt;71.0,487.0&gt;&gt; = 5.0796078600145425

* u2CB5A (U+2CB5A): L&lt;&lt;146.0,479.0&gt;--&lt;156.0,479.0&gt;&gt;/L&lt;&lt;156.0,479.0&gt;--&lt;66.0,487.0&gt;&gt; = 5.0796078600145425

* u2CB6F (U+2CB6F): L&lt;&lt;539.0,456.0&gt;--&lt;539.0,-13.0&gt;&gt;/L&lt;&lt;539.0,-13.0&gt;--&lt;548.0,35.0&gt;&gt; = 10.61965527615514

* u2CB78 (U+2CB78): L&lt;&lt;146.0,479.0&gt;--&lt;156.0,479.0&gt;&gt;/L&lt;&lt;156.0,479.0&gt;--&lt;69.0,487.0&gt;&gt; = 5.253802751262233

* u2CE18 (U+2CE18): L&lt;&lt;273.0,366.0&gt;--&lt;257.0,366.0&gt;&gt;/L&lt;&lt;257.0,366.0&gt;--&lt;329.0,351.0&gt;&gt; = 11.768288932020628

* u2CE93 (U+2CE93): L&lt;&lt;868.0,415.0&gt;--&lt;849.0,495.0&gt;&gt;/L&lt;&lt;849.0,495.0&gt;--&lt;849.0,373.0&gt;&gt; = 13.360218444764461

* u3060 (U+3060): L&lt;&lt;749.0,571.0&gt;--&lt;731.0,569.0&gt;&gt;/L&lt;&lt;731.0,569.0&gt;--&lt;754.0,569.0&gt;&gt; = 6.340191745909908

* u3062 (U+3062): L&lt;&lt;688.0,571.0&gt;--&lt;626.0,564.0&gt;&gt;/L&lt;&lt;626.0,564.0&gt;--&lt;823.0,564.0&gt;&gt; = 6.441600099335006

* u3124 (U+3124): L&lt;&lt;529.0,-24.0&gt;--&lt;529.0,474.0&gt;&gt;/B&lt;&lt;529.0,474.0&gt;-&lt;492.0,279.0&gt;-&lt;401.5,157.5&gt;&gt; = 10.743787070980858

* u3231 (U+3231): L&lt;&lt;311.0,-49.0&gt;--&lt;311.0,268.0&gt;&gt;/L&lt;&lt;311.0,268.0&gt;--&lt;274.0,108.0&gt;&gt; = 13.02076730562467

* u32FF (U+32FF): L&lt;&lt;583.0,-55.0&gt;--&lt;583.0,256.0&gt;&gt;/L&lt;&lt;583.0,256.0&gt;--&lt;534.0,47.0&gt;&gt; = 13.194671075003052

* u337C (U+337C): L&lt;&lt;598.0,-55.0&gt;--&lt;598.0,256.0&gt;&gt;/L&lt;&lt;598.0,256.0&gt;--&lt;551.0,47.0&gt;&gt; = 12.673860005623133

* u3E06 (U+3E06): B&lt;&lt;268.0,830.0&gt;-&lt;268.0,657.0&gt;-&lt;258.0,504.0&gt;&gt;/L&lt;&lt;258.0,504.0&gt;--&lt;319.0,717.0&gt;&gt; = 12.241413785463854

* u3E0C (U+3E0C): B&lt;&lt;286.0,810.0&gt;-&lt;286.0,646.0&gt;-&lt;276.0,499.0&gt;&gt;/L&lt;&lt;276.0,499.0&gt;--&lt;345.0,717.0&gt;&gt; = 13.671619760435904

* u47F4 (U+47F4): L&lt;&lt;545.0,358.0&gt;--&lt;545.0,396.0&gt;&gt;/L&lt;&lt;545.0,396.0&gt;--&lt;534.0,-50.0&gt;&gt; = 1.4128381782191464

* u48C5 (U+48C5): L&lt;&lt;179.0,358.0&gt;--&lt;179.0,396.0&gt;&gt;/L&lt;&lt;179.0,396.0&gt;--&lt;169.0,-50.0&gt;&gt; = 1.2844435218005597

* u4955 (U+4955): L&lt;&lt;552.0,456.0&gt;--&lt;552.0,-13.0&gt;&gt;/L&lt;&lt;552.0,-13.0&gt;--&lt;561.0,35.0&gt;&gt; = 10.61965527615514

* u4C98 (U+4C98): L&lt;&lt;825.0,363.0&gt;--&lt;825.0,317.0&gt;&gt;/L&lt;&lt;825.0,317.0&gt;--&lt;837.0,423.0&gt;&gt; = 6.458816378718628

* u4CA2 (U+4CA2): L&lt;&lt;599.0,470.0&gt;--&lt;580.0,431.0&gt;&gt;/L&lt;&lt;580.0,431.0&gt;--&lt;586.0,440.0&gt;&gt; = 7.715673563548395

* u4F48 (U+4F48): L&lt;&lt;742.0,388.0&gt;--&lt;742.0,31.0&gt;&gt;/L&lt;&lt;742.0,31.0&gt;--&lt;749.0,59.0&gt;&gt; = 14.036243467926484

* u500C (U+500C): L&lt;&lt;815.0,554.0&gt;--&lt;815.0,498.0&gt;&gt;/L&lt;&lt;815.0,498.0&gt;--&lt;830.0,630.0&gt;&gt; = 6.483073692897206

* u5016 (U+5016): L&lt;&lt;580.0,334.0&gt;--&lt;532.0,332.0&gt;&gt;/L&lt;&lt;532.0,332.0&gt;--&lt;710.0,332.0&gt;&gt; = 2.3859440303887243

* u5043 (U+5043): L&lt;&lt;647.0,377.0&gt;--&lt;626.0,377.0&gt;&gt;/L&lt;&lt;626.0,377.0&gt;--&lt;716.0,361.0&gt;&gt; = 10.08059798754231

* u5056 (U+5056): L&lt;&lt;837.0,341.0&gt;--&lt;764.0,324.0&gt;&gt;/L&lt;&lt;764.0,324.0&gt;--&lt;879.0,324.0&gt;&gt; = 13.109208198154267

* u50C2 (U+50C2): L&lt;&lt;808.0,263.0&gt;--&lt;595.0,263.0&gt;&gt;/L&lt;&lt;595.0,263.0&gt;--&lt;621.0,257.0&gt;&gt; = 12.994616791916512

* u50E6 (U+50E6): L&lt;&lt;750.0,-14.0&gt;--&lt;750.0,352.0&gt;&gt;/B&lt;&lt;750.0,352.0&gt;-&lt;732.0,191.0&gt;-&lt;707.5,110.0&gt;&gt; = 6.3792481676131265

* u51F3 (U+51F3): L&lt;&lt;405.0,269.0&gt;--&lt;399.0,268.0&gt;&gt;/L&lt;&lt;399.0,268.0&gt;--&lt;609.0,268.0&gt;&gt; = 9.462322208025613

* u5217 (U+5217): L&lt;&lt;547.0,736.0&gt;--&lt;355.0,736.0&gt;&gt;/L&lt;&lt;355.0,736.0&gt;--&lt;362.0,735.0&gt;&gt; = 8.13010235415596

* u525C (U+525C): L&lt;&lt;193.0,582.0&gt;--&lt;192.0,582.0&gt;&gt;/L&lt;&lt;192.0,582.0&gt;--&lt;227.0,577.0&gt;&gt; = 8.13010235415596

* u52AC (U+52AC): L&lt;&lt;184.0,138.0&gt;--&lt;184.0,517.0&gt;&gt;/L&lt;&lt;184.0,517.0&gt;--&lt;161.0,298.0&gt;&gt; = 5.995386804075405

* u5379 (U+5379): L&lt;&lt;175.0,604.0&gt;--&lt;175.0,598.0&gt;&gt;/L&lt;&lt;175.0,598.0&gt;--&lt;221.0,812.0&gt;&gt; = 12.131321066632513

* u53B3 (U+53B3): L&lt;&lt;298.0,675.0&gt;--&lt;219.0,661.0&gt;&gt;/L&lt;&lt;219.0,661.0&gt;--&lt;487.0,661.0&gt;&gt; = 10.049348588124865

* u53B3 (U+53B3): L&lt;&lt;578.0,676.0&gt;--&lt;503.0,661.0&gt;&gt;/L&lt;&lt;503.0,661.0&gt;--&lt;763.0,661.0&gt;&gt; = 11.309932474020195

* u53D7 (U+53D7): L&lt;&lt;544.0,535.0&gt;--&lt;538.0,534.0&gt;&gt;/L&lt;&lt;538.0,534.0&gt;--&lt;665.0,534.0&gt;&gt; = 9.462322208025613

* u5450 (U+5450): L&lt;&lt;503.0,600.0&gt;--&lt;503.0,232.0&gt;&gt;/L&lt;&lt;503.0,232.0&gt;--&lt;593.0,600.0&gt;&gt; = 13.74279773915705

* u5486 (U+5486): L&lt;&lt;484.0,-24.0&gt;--&lt;484.0,401.0&gt;&gt;/L&lt;&lt;484.0,401.0&gt;--&lt;477.0,356.0&gt;&gt; = 8.84181456019167

* u5530 (U+5530): L&lt;&lt;583.0,379.0&gt;--&lt;583.0,73.0&gt;&gt;/L&lt;&lt;583.0,73.0&gt;--&lt;592.0,116.0&gt;&gt; = 11.821488340607226

* u5546 (U+5546): L&lt;&lt;930.0,623.0&gt;--&lt;712.0,623.0&gt;&gt;/L&lt;&lt;712.0,623.0&gt;--&lt;742.0,617.0&gt;&gt; = 11.309932474020195

* u55FD (U+55FD): L&lt;&lt;765.0,645.0&gt;--&lt;750.0,501.0&gt;&gt;/L&lt;&lt;750.0,501.0&gt;--&lt;765.0,575.0&gt;&gt; = 5.51188929190376

* u5600 (U+5600): L&lt;&lt;884.0,623.0&gt;--&lt;784.0,623.0&gt;&gt;/L&lt;&lt;784.0,623.0&gt;--&lt;800.0,621.0&gt;&gt; = 7.125016348901757

* u560D (U+560D): L&lt;&lt;810.0,263.0&gt;--&lt;620.0,263.0&gt;&gt;/L&lt;&lt;620.0,263.0&gt;--&lt;643.0,258.0&gt;&gt; = 12.2647737278924

* u561B (U+561B): L&lt;&lt;525.0,-51.0&gt;--&lt;525.0,269.0&gt;&gt;/L&lt;&lt;525.0,269.0&gt;--&lt;473.0,-11.0&gt;&gt; = 10.52078431387435

* u561B (U+561B): L&lt;&lt;753.0,-51.0&gt;--&lt;753.0,259.0&gt;&gt;/L&lt;&lt;753.0,259.0&gt;--&lt;694.0,-13.0&gt;&gt; = 12.238535393817664

* u561B (U+561B): L&lt;&lt;871.0,-11.0&gt;--&lt;817.0,290.0&gt;&gt;/L&lt;&lt;817.0,290.0&gt;--&lt;817.0,-51.0&gt;&gt; = 10.170782298074723

* u564E (U+564E): L&lt;&lt;608.0,27.0&gt;--&lt;580.0,24.0&gt;&gt;/L&lt;&lt;580.0,24.0&gt;--&lt;694.0,24.0&gt;&gt; = 6.115503566285384

* u566F (U+566F): L&lt;&lt;573.0,122.0&gt;--&lt;552.0,90.0&gt;&gt;/L&lt;&lt;552.0,90.0&gt;--&lt;566.0,109.0&gt;&gt; = 3.109463831001076

* u567A (U+567A): L&lt;&lt;647.0,255.0&gt;--&lt;647.0,248.0&gt;&gt;/L&lt;&lt;647.0,248.0&gt;--&lt;651.0,352.0&gt;&gt; = 2.2025981617658017

* u568E (U+568E): L&lt;&lt;718.0,199.0&gt;--&lt;713.0,211.0&gt;&gt;/B&lt;&lt;713.0,211.0&gt;-&lt;715.0,205.0&gt;-&lt;716.0,200.0&gt;&gt; = 4.184916125118319

* u5693 (U+5693): L&lt;&lt;678.0,579.0&gt;--&lt;863.0,579.0&gt;&gt;/L&lt;&lt;863.0,579.0&gt;--&lt;815.0,582.0&gt;&gt; = 3.576334374997269

* u56B1 (U+56B1): L&lt;&lt;417.0,38.0&gt;--&lt;522.0,55.0&gt;&gt;/L&lt;&lt;522.0,55.0&gt;--&lt;461.0,50.0&gt;&gt; = 4.510756052126092

* u56B1 (U+56B1): L&lt;&lt;421.0,458.0&gt;--&lt;420.0,468.0&gt;&gt;/L&lt;&lt;420.0,468.0&gt;--&lt;409.0,-49.0&gt;&gt; = 6.929468372630909

* u56C0 (U+56C0): L&lt;&lt;832.0,240.0&gt;--&lt;783.0,234.0&gt;&gt;/L&lt;&lt;783.0,234.0&gt;--&lt;836.0,234.0&gt;&gt; = 6.981057406829781

* u56CE (U+56CE): L&lt;&lt;646.0,404.0&gt;--&lt;612.0,554.0&gt;&gt;/L&lt;&lt;612.0,554.0&gt;--&lt;612.0,393.0&gt;&gt; = 12.771242564901442

* u56CE (U+56CE): L&lt;&lt;816.0,393.0&gt;--&lt;816.0,537.0&gt;&gt;/L&lt;&lt;816.0,537.0&gt;--&lt;786.0,404.0&gt;&gt; = 12.711132565529468

* u5747 (U+5747): L&lt;&lt;384.0,559.0&gt;--&lt;384.0,538.0&gt;&gt;/L&lt;&lt;384.0,538.0&gt;--&lt;425.0,821.0&gt;&gt; = 8.243446972894288

* u5789 (U+5789): L&lt;&lt;468.0,-24.0&gt;--&lt;468.0,373.0&gt;&gt;/L&lt;&lt;468.0,373.0&gt;--&lt;465.0,356.0&gt;&gt; = 10.00797980144135

* u5789 (U+5789): L&lt;&lt;741.0,214.0&gt;--&lt;719.0,214.0&gt;&gt;/L&lt;&lt;719.0,214.0&gt;--&lt;786.0,206.0&gt;&gt; = 6.809050179613415

* u5830 (U+5830): L&lt;&lt;652.0,365.0&gt;--&lt;631.0,365.0&gt;&gt;/L&lt;&lt;631.0,365.0&gt;--&lt;721.0,349.0&gt;&gt; = 10.08059798754231

* u5831 (U+5831): L&lt;&lt;273.0,334.0&gt;--&lt;225.0,332.0&gt;&gt;/L&lt;&lt;225.0,332.0&gt;--&lt;342.0,332.0&gt;&gt; = 2.3859440303887243

* u587F (U+587F): L&lt;&lt;823.0,263.0&gt;--&lt;634.0,263.0&gt;&gt;/L&lt;&lt;634.0,263.0&gt;--&lt;659.0,258.0&gt;&gt; = 11.309932474020195

* u5892 (U+5892): L&lt;&lt;884.0,623.0&gt;--&lt;784.0,623.0&gt;&gt;/L&lt;&lt;784.0,623.0&gt;--&lt;800.0,621.0&gt;&gt; = 7.125016348901757

* u5893 (U+5893): B&lt;&lt;354.5,195.5&gt;-&lt;291.0,163.0&gt;-&lt;211.0,143.0&gt;&gt;/L&lt;&lt;211.0,143.0&gt;--&lt;452.0,143.0&gt;&gt; = 14.036243467926484

* u58BE (U+58BE): L&lt;&lt;249.0,552.0&gt;--&lt;342.0,598.0&gt;&gt;/L&lt;&lt;342.0,598.0&gt;--&lt;297.0,583.0&gt;&gt; = 7.883139316729763

* u58BE (U+58BE): L&lt;&lt;82.0,469.0&gt;--&lt;244.0,549.0&gt;&gt;/L&lt;&lt;244.0,549.0&gt;--&lt;170.0,525.0&gt;&gt; = 8.312271281163143

* u58F9 (U+58F9): L&lt;&lt;405.0,29.0&gt;--&lt;370.0,24.0&gt;&gt;/L&lt;&lt;370.0,24.0&gt;--&lt;606.0,24.0&gt;&gt; = 8.13010235415596

* u58F9 (U+58F9): L&lt;&lt;728.0,127.0&gt;--&lt;654.0,127.0&gt;&gt;/L&lt;&lt;654.0,127.0&gt;--&lt;728.0,112.0&gt;&gt; = 11.458752345877198

* u5A1A (U+5A1A): L&lt;&lt;816.0,339.0&gt;--&lt;697.0,339.0&gt;&gt;/L&lt;&lt;697.0,339.0&gt;--&lt;731.0,331.0&gt;&gt; = 13.24051991518721

* u5A49 (U+5A49): L&lt;&lt;541.0,582.0&gt;--&lt;533.0,582.0&gt;&gt;/L&lt;&lt;533.0,582.0&gt;--&lt;567.0,574.0&gt;&gt; = 13.24051991518721

* u5AAC (U+5AAC): L&lt;&lt;701.0,-58.0&gt;--&lt;701.0,277.0&gt;&gt;/L&lt;&lt;701.0,277.0&gt;--&lt;633.0,-26.0&gt;&gt; = 12.648882516625008

* u5AAC (U+5AAC): L&lt;&lt;852.0,-24.0&gt;--&lt;797.0,278.0&gt;&gt;/L&lt;&lt;797.0,278.0&gt;--&lt;797.0,-58.0&gt;&gt; = 10.321541042743755

* u5AE1 (U+5AE1): L&lt;&lt;931.0,623.0&gt;--&lt;831.0,623.0&gt;&gt;/L&lt;&lt;831.0,623.0&gt;--&lt;848.0,621.0&gt;&gt; = 6.709836807756896

* u5AF2 (U+5AF2): L&lt;&lt;541.0,-51.0&gt;--&lt;541.0,269.0&gt;&gt;/L&lt;&lt;541.0,269.0&gt;--&lt;491.0,-11.0&gt;&gt; = 10.124671655397806

* u5AF2 (U+5AF2): L&lt;&lt;760.0,-51.0&gt;--&lt;760.0,259.0&gt;&gt;/L&lt;&lt;760.0,259.0&gt;--&lt;703.0,-13.0&gt;&gt; = 11.83556708047782

* u5AF2 (U+5AF2): L&lt;&lt;873.0,-11.0&gt;--&lt;822.0,290.0&gt;&gt;/L&lt;&lt;822.0,290.0&gt;--&lt;822.0,-51.0&gt;&gt; = 9.616591570049943

* u5B21 (U+5B21): L&lt;&lt;590.0,122.0&gt;--&lt;562.0,77.0&gt;&gt;/L&lt;&lt;562.0,77.0&gt;--&lt;584.0,109.0&gt;&gt; = 2.6177311858225365

* u5B24 (U+5B24): L&lt;&lt;872.0,317.0&gt;--&lt;835.0,462.0&gt;&gt;/L&lt;&lt;835.0,462.0&gt;--&lt;835.0,304.0&gt;&gt; = 14.314826910404852

* u5B37 (U+5B37): L&lt;&lt;872.0,317.0&gt;--&lt;835.0,462.0&gt;&gt;/L&lt;&lt;835.0,462.0&gt;--&lt;835.0,304.0&gt;&gt; = 14.314826910404852

* u5B57 (U+5B57): L&lt;&lt;187.0,554.0&gt;--&lt;821.0,554.0&gt;&gt;/L&lt;&lt;821.0,554.0&gt;--&lt;808.0,557.0&gt;&gt; = 12.994616791916512

* u5B75 (U+5B75): L&lt;&lt;207.0,549.0&gt;--&lt;237.0,337.0&gt;&gt;/B&lt;&lt;237.0,337.0&gt;-&lt;242.0,431.0&gt;-&lt;242.0,625.0&gt;&gt; = 11.099192890575727

* u5BF6 (U+5BF6): L&lt;&lt;811.0,683.0&gt;--&lt;519.0,683.0&gt;&gt;/L&lt;&lt;519.0,683.0&gt;--&lt;589.0,669.0&gt;&gt; = 11.309932474020195

* u5C07 (U+5C07): L&lt;&lt;624.0,736.0&gt;--&lt;561.0,662.0&gt;&gt;/L&lt;&lt;561.0,662.0&gt;--&lt;579.0,680.0&gt;&gt; = 4.590543185605989

* u5C0E (U+5C0E): L&lt;&lt;933.0,227.0&gt;--&lt;701.0,214.0&gt;&gt;/L&lt;&lt;701.0,214.0&gt;--&lt;777.0,214.0&gt;&gt; = 3.207185467278706

* u5C22 (U+5C22): L&lt;&lt;529.0,-20.0&gt;--&lt;529.0,489.0&gt;&gt;/B&lt;&lt;529.0,489.0&gt;-&lt;491.0,297.0&gt;-&lt;400.0,171.0&gt;&gt; = 11.19511142629998

* u5C24 (U+5C24): L&lt;&lt;529.0,-24.0&gt;--&lt;529.0,474.0&gt;&gt;/B&lt;&lt;529.0,474.0&gt;-&lt;492.0,279.0&gt;-&lt;401.5,157.5&gt;&gt; = 10.743787070980858

* u5C60 (U+5C60): L&lt;&lt;181.0,296.0&gt;--&lt;181.0,309.0&gt;&gt;/L&lt;&lt;181.0,309.0&gt;--&lt;165.0,-56.0&gt;&gt; = 2.5099889380792546

* u5C6C (U+5C6C): L&lt;&lt;643.0,67.0&gt;--&lt;690.0,78.0&gt;&gt;/L&lt;&lt;690.0,78.0&gt;--&lt;659.0,78.0&gt;&gt; = 13.172553423326871

* u5D73 (U+5D73): L&lt;&lt;246.0,579.0&gt;--&lt;338.0,593.0&gt;&gt;/L&lt;&lt;338.0,593.0&gt;--&lt;137.0,593.0&gt;&gt; = 8.652541791114704

* u5D81 (U+5D81): L&lt;&lt;817.0,263.0&gt;--&lt;644.0,263.0&gt;&gt;/L&lt;&lt;644.0,263.0&gt;--&lt;667.0,258.0&gt;&gt; = 12.2647737278924

* u5DAE (U+5DAE): L&lt;&lt;753.0,199.0&gt;--&lt;745.0,199.0&gt;&gt;/L&lt;&lt;745.0,199.0&gt;--&lt;827.0,180.0&gt;&gt; = 13.045637062948598

* u5DC7 (U+5DC7): L&lt;&lt;432.0,38.0&gt;--&lt;534.0,55.0&gt;&gt;/L&lt;&lt;534.0,55.0&gt;--&lt;475.0,50.0&gt;&gt; = 4.618321832944919

* u5DC7 (U+5DC7): L&lt;&lt;436.0,458.0&gt;--&lt;435.0,468.0&gt;&gt;/L&lt;&lt;435.0,468.0&gt;--&lt;424.0,-49.0&gt;&gt; = 6.929468372630909

* u5DD8 (U+5DD8): L&lt;&lt;852.0,-54.0&gt;--&lt;814.0,241.0&gt;&gt;/B&lt;&lt;814.0,241.0&gt;-&lt;807.0,156.0&gt;-&lt;797.0,87.5&gt;&gt; = 12.047905955425335

* u5DE9 (U+5DE9): L&lt;&lt;603.0,516.0&gt;--&lt;668.0,182.0&gt;&gt;/L&lt;&lt;668.0,182.0&gt;--&lt;668.0,736.0&gt;&gt; = 11.012723603415871

* u5DE9 (U+5DE9): L&lt;&lt;604.0,162.0&gt;--&lt;541.0,486.0&gt;&gt;/B&lt;&lt;541.0,486.0&gt;-&lt;537.0,254.0&gt;-&lt;510.0,149.5&gt;&gt; = 11.991301251389308

* u5E06 (U+5E06): L&lt;&lt;661.0,516.0&gt;--&lt;726.0,182.0&gt;&gt;/L&lt;&lt;726.0,182.0&gt;--&lt;726.0,736.0&gt;&gt; = 11.012723603415871

* u5E06 (U+5E06): L&lt;&lt;662.0,162.0&gt;--&lt;599.0,486.0&gt;&gt;/B&lt;&lt;599.0,486.0&gt;-&lt;593.0,245.0&gt;-&lt;574.0,123.5&gt;&gt; = 12.429697187343987

* u5E3B (U+5E3B): L&lt;&lt;305.0,604.0&gt;--&lt;305.0,68.0&gt;&gt;/L&lt;&lt;305.0,68.0&gt;--&lt;311.0,114.0&gt;&gt; = 7.431407971172489

* u5E3D (U+5E3D): L&lt;&lt;305.0,604.0&gt;--&lt;305.0,68.0&gt;&gt;/L&lt;&lt;305.0,68.0&gt;--&lt;311.0,114.0&gt;&gt; = 7.431407971172489

* u5E63 (U+5E63): L&lt;&lt;392.0,546.0&gt;--&lt;420.0,384.0&gt;&gt;/L&lt;&lt;420.0,384.0&gt;--&lt;420.0,584.0&gt;&gt; = 9.80609275989708

* u5E6A (U+5E6A): L&lt;&lt;837.0,520.0&gt;--&lt;837.0,493.0&gt;&gt;/L&lt;&lt;837.0,493.0&gt;--&lt;846.0,574.0&gt;&gt; = 6.340191745909908

* u5E96 (U+5E96): L&lt;&lt;325.0,-24.0&gt;--&lt;325.0,324.0&gt;&gt;/L&lt;&lt;325.0,324.0&gt;--&lt;321.0,303.0&gt;&gt; = 10.784297867562596

* u5F0A (U+5F0A): L&lt;&lt;188.0,564.0&gt;--&lt;188.0,318.0&gt;&gt;/L&lt;&lt;188.0,318.0&gt;--&lt;214.0,527.0&gt;&gt; = 7.091273255327566

* u5F46 (U+5F46): L&lt;&lt;188.0,635.0&gt;--&lt;188.0,476.0&gt;&gt;/L&lt;&lt;188.0,476.0&gt;--&lt;215.0,625.0&gt;&gt; = 10.271003720479047

* u5F5D (U+5F5D): L&lt;&lt;796.0,230.0&gt;--&lt;825.0,240.0&gt;&gt;/L&lt;&lt;825.0,240.0&gt;--&lt;818.0,239.0&gt;&gt; = 10.895503683412684

* u5F5E (U+5F5E): L&lt;&lt;796.0,230.0&gt;--&lt;825.0,240.0&gt;&gt;/L&lt;&lt;825.0,240.0&gt;--&lt;818.0,239.0&gt;&gt; = 10.895503683412684

* u5F6C (U+5F6C): L&lt;&lt;194.0,-71.0&gt;--&lt;194.0,230.0&gt;&gt;/L&lt;&lt;194.0,230.0&gt;--&lt;141.0,11.0&gt;&gt; = 13.604528864632057

* u5F6C (U+5F6C): L&lt;&lt;448.0,-71.0&gt;--&lt;448.0,215.0&gt;&gt;/L&lt;&lt;448.0,215.0&gt;--&lt;392.0,-5.0&gt;&gt; = 14.281095735970814

* u5FAA (U+5FAA): L&lt;&lt;653.0,448.0&gt;--&lt;653.0,430.0&gt;&gt;/L&lt;&lt;653.0,430.0&gt;--&lt;662.0,520.0&gt;&gt; = 5.710593137499633

* u6016 (U+6016): L&lt;&lt;742.0,388.0&gt;--&lt;742.0,31.0&gt;&gt;/L&lt;&lt;742.0,31.0&gt;--&lt;749.0,59.0&gt;&gt; = 14.036243467926484

* u6083 (U+6083): L&lt;&lt;699.0,469.0&gt;--&lt;703.0,470.0&gt;&gt;/L&lt;&lt;703.0,470.0&gt;--&lt;699.0,470.0&gt;&gt; = 14.036243467926484

* u6094 (U+6094): L&lt;&lt;380.0,600.0&gt;--&lt;385.0,447.0&gt;&gt;/L&lt;&lt;385.0,447.0&gt;--&lt;451.0,815.0&gt;&gt; = 12.039520452700156

* u60A4 (U+60A4): L&lt;&lt;444.0,545.0&gt;--&lt;423.0,513.0&gt;&gt;/L&lt;&lt;423.0,513.0&gt;--&lt;437.0,532.0&gt;&gt; = 3.109463831001076

* u60BB (U+60BB): L&lt;&lt;590.0,334.0&gt;--&lt;542.0,332.0&gt;&gt;/L&lt;&lt;542.0,332.0&gt;--&lt;710.0,332.0&gt;&gt; = 2.3859440303887243

* u60CB (U+60CB): L&lt;&lt;539.0,582.0&gt;--&lt;531.0,582.0&gt;&gt;/L&lt;&lt;531.0,582.0&gt;--&lt;565.0,574.0&gt;&gt; = 13.24051991518721

* u611B (U+611B): L&lt;&lt;177.0,497.0&gt;--&lt;177.0,380.0&gt;&gt;/L&lt;&lt;177.0,380.0&gt;--&lt;190.0,444.0&gt;&gt; = 11.481991354748077

* u611B (U+611B): L&lt;&lt;551.0,546.0&gt;--&lt;546.0,545.0&gt;&gt;/L&lt;&lt;546.0,545.0&gt;--&lt;673.0,545.0&gt;&gt; = 11.309932474020195

* u6147 (U+6147): L&lt;&lt;444.0,765.0&gt;--&lt;246.0,723.0&gt;&gt;/L&lt;&lt;246.0,723.0&gt;--&lt;440.0,723.0&gt;&gt; = 11.976132444203364

* u615C (U+615C): L&lt;&lt;201.0,701.0&gt;--&lt;181.0,618.0&gt;&gt;/L&lt;&lt;181.0,618.0&gt;--&lt;196.0,667.0&gt;&gt; = 3.4725866235193106

* u618B (U+618B): L&lt;&lt;177.0,564.0&gt;--&lt;177.0,318.0&gt;&gt;/L&lt;&lt;177.0,318.0&gt;--&lt;203.0,527.0&gt;&gt; = 7.091273255327566

* u6193 (U+6193): L&lt;&lt;791.0,315.0&gt;--&lt;813.0,319.0&gt;&gt;/L&lt;&lt;813.0,319.0&gt;--&lt;804.0,319.0&gt;&gt; = 10.304846468766044

* u61C7 (U+61C7): L&lt;&lt;83.0,469.0&gt;--&lt;363.0,601.0&gt;&gt;/L&lt;&lt;363.0,601.0&gt;--&lt;310.0,582.0&gt;&gt; = 5.518251500339715

* u61CB (U+61CB): L&lt;&lt;656.0,599.0&gt;--&lt;627.0,367.0&gt;&gt;/L&lt;&lt;627.0,367.0&gt;--&lt;715.0,612.0&gt;&gt; = 12.632443373026835

* u61DE (U+61DE): L&lt;&lt;829.0,520.0&gt;--&lt;829.0,493.0&gt;&gt;/L&lt;&lt;829.0,493.0&gt;--&lt;839.0,574.0&gt;&gt; = 7.037940763184638

* u61E8 (U+61E8): L&lt;&lt;858.0,-26.0&gt;--&lt;821.0,238.0&gt;&gt;/B&lt;&lt;821.0,238.0&gt;-&lt;814.0,161.0&gt;-&lt;802.5,99.5&gt;&gt; = 13.172553423326871

* u621B (U+621B): L&lt;&lt;650.0,112.0&gt;--&lt;814.0,152.0&gt;&gt;/L&lt;&lt;814.0,152.0&gt;--&lt;602.0,152.0&gt;&gt; = 13.70696100407981

* u621B (U+621B): L&lt;&lt;662.0,268.0&gt;--&lt;748.0,288.0&gt;&gt;/L&lt;&lt;748.0,288.0&gt;--&lt;733.0,288.0&gt;&gt; = 13.091893064346833

* u621B (U+621B): L&lt;&lt;784.0,209.0&gt;--&lt;745.0,200.0&gt;&gt;/L&lt;&lt;745.0,200.0&gt;--&lt;898.0,200.0&gt;&gt; = 12.994616791916512

* u6232 (U+6232): L&lt;&lt;184.0,38.0&gt;--&lt;331.0,55.0&gt;&gt;/L&lt;&lt;331.0,55.0&gt;--&lt;246.0,50.0&gt;&gt; = 3.2302776344644166

* u6232 (U+6232): L&lt;&lt;190.0,458.0&gt;--&lt;188.0,468.0&gt;&gt;/L&lt;&lt;188.0,468.0&gt;--&lt;173.0,-49.0&gt;&gt; = 12.971819631942296

* u638F (U+638F): L&lt;&lt;489.0,655.0&gt;--&lt;437.0,497.0&gt;&gt;/L&lt;&lt;437.0,497.0&gt;--&lt;503.0,605.0&gt;&gt; = 13.212470417013622

* u63E0 (U+63E0): L&lt;&lt;654.0,377.0&gt;--&lt;634.0,377.0&gt;&gt;/L&lt;&lt;634.0,377.0&gt;--&lt;721.0,361.0&gt;&gt; = 10.420712396794501

* u6412 (U+6412): L&lt;&lt;512.0,524.0&gt;--&lt;511.0,528.0&gt;&gt;/L&lt;&lt;511.0,528.0&gt;--&lt;511.0,524.0&gt;&gt; = 14.036243467926484

* u6416 (U+6416): L&lt;&lt;440.0,626.0&gt;--&lt;481.0,667.0&gt;&gt;/L&lt;&lt;481.0,667.0&gt;--&lt;406.0,616.0&gt;&gt; = 10.784297867562596

* u6423 (U+6423): L&lt;&lt;514.0,445.0&gt;--&lt;534.0,222.0&gt;&gt;/L&lt;&lt;534.0,222.0&gt;--&lt;562.0,482.0&gt;&gt; = 11.271549005625745

* u6458 (U+6458): L&lt;&lt;936.0,623.0&gt;--&lt;820.0,623.0&gt;&gt;/L&lt;&lt;820.0,623.0&gt;--&lt;837.0,621.0&gt;&gt; = 6.709836807756896

* u645F (U+645F): L&lt;&lt;827.0,263.0&gt;--&lt;632.0,263.0&gt;&gt;/L&lt;&lt;632.0,263.0&gt;--&lt;654.0,259.0&gt;&gt; = 10.304846468766044

* u6487 (U+6487): L&lt;&lt;508.0,456.0&gt;--&lt;508.0,-13.0&gt;&gt;/L&lt;&lt;508.0,-13.0&gt;--&lt;518.0,35.0&gt;&gt; = 11.768288932020628

* u64CE (U+64CE): L&lt;&lt;151.0,384.0&gt;--&lt;151.0,500.0&gt;&gt;/L&lt;&lt;151.0,500.0&gt;--&lt;143.0,460.0&gt;&gt; = 11.309932474020227

* u64E6 (U+64E6): L&lt;&lt;678.0,579.0&gt;--&lt;863.0,579.0&gt;&gt;/L&lt;&lt;863.0,579.0&gt;--&lt;815.0,582.0&gt;&gt; = 3.576334374997269

* u64EC (U+64EC): L&lt;&lt;302.0,174.0&gt;--&lt;393.0,174.0&gt;&gt;/L&lt;&lt;393.0,174.0&gt;--&lt;320.0,180.0&gt;&gt; = 4.698680517299439

* u6500 (U+6500): L&lt;&lt;433.0,512.0&gt;--&lt;406.0,535.0&gt;&gt;/L&lt;&lt;406.0,535.0&gt;--&lt;412.0,529.0&gt;&gt; = 4.573921259900818

* u6572 (U+6572): L&lt;&lt;373.0,224.0&gt;--&lt;373.0,-1.0&gt;&gt;/L&lt;&lt;373.0,-1.0&gt;--&lt;376.0,17.0&gt;&gt; = 9.462322208025613

* u6575 (U+6575): L&lt;&lt;505.0,623.0&gt;--&lt;418.0,623.0&gt;&gt;/L&lt;&lt;418.0,623.0&gt;--&lt;437.0,621.0&gt;&gt; = 6.009005957494474

* u662B (U+662B): L&lt;&lt;368.0,737.0&gt;--&lt;368.0,330.0&gt;&gt;/L&lt;&lt;368.0,330.0&gt;--&lt;480.0,806.0&gt;&gt; = 13.24051991518721

* u66D6 (U+66D6): L&lt;&lt;558.0,122.0&gt;--&lt;537.0,90.0&gt;&gt;/L&lt;&lt;537.0,90.0&gt;--&lt;551.0,109.0&gt;&gt; = 3.109463831001076

* u66E9 (U+66E9): L&lt;&lt;884.0,60.0&gt;--&lt;668.0,42.0&gt;&gt;/L&lt;&lt;668.0,42.0&gt;--&lt;930.0,-2.0&gt;&gt; = 14.29687448075618

* u6710 (U+6710): L&lt;&lt;372.0,785.0&gt;--&lt;372.0,325.0&gt;&gt;/L&lt;&lt;372.0,325.0&gt;--&lt;485.0,806.0&gt;&gt; = 13.220600187337643

* u6713 (U+6713): L&lt;&lt;370.0,325.0&gt;--&lt;371.0,331.0&gt;&gt;/L&lt;&lt;371.0,331.0&gt;--&lt;370.0,322.0&gt;&gt; = 3.1221304621157

* u6713 (U+6713): L&lt;&lt;370.0,785.0&gt;--&lt;370.0,325.0&gt;&gt;/L&lt;&lt;370.0,325.0&gt;--&lt;371.0,331.0&gt;&gt; = 9.462322208025613

* u6718 (U+6718): L&lt;&lt;373.0,325.0&gt;--&lt;374.0,331.0&gt;&gt;/L&lt;&lt;374.0,331.0&gt;--&lt;373.0,322.0&gt;&gt; = 3.1221304621157

* u6718 (U+6718): L&lt;&lt;373.0,785.0&gt;--&lt;373.0,325.0&gt;&gt;/L&lt;&lt;373.0,325.0&gt;--&lt;374.0,331.0&gt;&gt; = 9.462322208025613

* u674B (U+674B): L&lt;&lt;603.0,516.0&gt;--&lt;668.0,182.0&gt;&gt;/L&lt;&lt;668.0,182.0&gt;--&lt;668.0,736.0&gt;&gt; = 11.012723603415871

* u674B (U+674B): L&lt;&lt;604.0,162.0&gt;--&lt;541.0,486.0&gt;&gt;/B&lt;&lt;541.0,486.0&gt;-&lt;537.0,254.0&gt;-&lt;510.0,149.5&gt;&gt; = 11.991301251389308

* u679E (U+679E): L&lt;&lt;183.0,-68.0&gt;--&lt;183.0,305.0&gt;&gt;/L&lt;&lt;183.0,305.0&gt;--&lt;139.0,112.0&gt;&gt; = 12.842754043944451

* u67B8 (U+67B8): L&lt;&lt;434.0,565.0&gt;--&lt;434.0,533.0&gt;&gt;/L&lt;&lt;434.0,533.0&gt;--&lt;455.0,802.0&gt;&gt; = 4.463851181968316

* u682F (U+682F): L&lt;&lt;567.0,-52.0&gt;--&lt;567.0,378.0&gt;&gt;/L&lt;&lt;567.0,378.0&gt;--&lt;511.0,56.0&gt;&gt; = 9.865806943084365

* u6886 (U+6886): L&lt;&lt;204.0,-51.0&gt;--&lt;204.0,291.0&gt;&gt;/L&lt;&lt;204.0,291.0&gt;--&lt;152.0,80.0&gt;&gt; = 13.84440563731597

* u68FA (U+68FA): L&lt;&lt;816.0,554.0&gt;--&lt;816.0,498.0&gt;&gt;/L&lt;&lt;816.0,498.0&gt;--&lt;831.0,630.0&gt;&gt; = 6.483073692897206

* u691F (U+691F): L&lt;&lt;195.0,-56.0&gt;--&lt;195.0,283.0&gt;&gt;/L&lt;&lt;195.0,283.0&gt;--&lt;155.0,112.0&gt;&gt; = 13.165794454440796

* u6921 (U+6921): L&lt;&lt;200.0,-50.0&gt;--&lt;200.0,264.0&gt;&gt;/L&lt;&lt;200.0,264.0&gt;--&lt;163.0,112.0&gt;&gt; = 13.680925359319371

* u6925 (U+6925): L&lt;&lt;211.0,-52.0&gt;--&lt;211.0,273.0&gt;&gt;/L&lt;&lt;211.0,273.0&gt;--&lt;175.0,102.0&gt;&gt; = 11.888658039627968

* u692D (U+692D): L&lt;&lt;695.0,-55.0&gt;--&lt;695.0,371.0&gt;&gt;/L&lt;&lt;695.0,371.0&gt;--&lt;670.0,151.0&gt;&gt; = 6.483073692897206

* u6959 (U+6959): L&lt;&lt;725.0,-48.0&gt;--&lt;725.0,291.0&gt;&gt;/L&lt;&lt;725.0,291.0&gt;--&lt;666.0,14.0&gt;&gt; = 12.02410880268954

* u6959 (U+6959): L&lt;&lt;863.0,19.0&gt;--&lt;807.0,305.0&gt;&gt;/L&lt;&lt;807.0,305.0&gt;--&lt;807.0,-48.0&gt;&gt; = 11.07859141821809

* u6960 (U+6960): L&lt;&lt;195.0,-56.0&gt;--&lt;195.0,283.0&gt;&gt;/L&lt;&lt;195.0,283.0&gt;--&lt;155.0,112.0&gt;&gt; = 13.165794454440796

* u696F (U+696F): L&lt;&lt;426.0,565.0&gt;--&lt;426.0,523.0&gt;&gt;/L&lt;&lt;426.0,523.0&gt;--&lt;435.0,655.0&gt;&gt; = 3.900493742381876

* u696F (U+696F): L&lt;&lt;658.0,448.0&gt;--&lt;658.0,430.0&gt;&gt;/L&lt;&lt;658.0,430.0&gt;--&lt;667.0,520.0&gt;&gt; = 5.710593137499633

* u6975 (U+6975): L&lt;&lt;348.0,24.0&gt;--&lt;601.0,24.0&gt;&gt;/L&lt;&lt;601.0,24.0&gt;--&lt;488.0,42.0&gt;&gt; = 9.050721677183743

* u6981 (U+6981): L&lt;&lt;814.0,567.0&gt;--&lt;814.0,553.0&gt;&gt;/L&lt;&lt;814.0,553.0&gt;--&lt;822.0,648.0&gt;&gt; = 4.813550893706515

* u699C (U+699C): L&lt;&lt;518.0,524.0&gt;--&lt;517.0,528.0&gt;&gt;/L&lt;&lt;517.0,528.0&gt;--&lt;517.0,524.0&gt;&gt; = 14.036243467926484

* u69A3 (U+69A3): L&lt;&lt;436.0,626.0&gt;--&lt;477.0,667.0&gt;&gt;/L&lt;&lt;477.0,667.0&gt;--&lt;402.0,616.0&gt;&gt; = 10.784297867562596

* u69DB (U+69DB): L&lt;&lt;190.0,-48.0&gt;--&lt;190.0,270.0&gt;&gt;/L&lt;&lt;190.0,270.0&gt;--&lt;155.0,112.0&gt;&gt; = 12.49040571790919

* u69DF (U+69DF): L&lt;&lt;201.0,-50.0&gt;--&lt;201.0,261.0&gt;&gt;/L&lt;&lt;201.0,261.0&gt;--&lt;165.0,112.0&gt;&gt; = 13.582963529836702

* u69E8 (U+69E8): L&lt;&lt;193.0,-50.0&gt;--&lt;193.0,277.0&gt;&gt;/L&lt;&lt;193.0,277.0&gt;--&lt;151.0,112.0&gt;&gt; = 14.281095735970814

* u6A05 (U+6A05): L&lt;&lt;187.0,-68.0&gt;--&lt;187.0,305.0&gt;&gt;/L&lt;&lt;187.0,305.0&gt;--&lt;143.0,112.0&gt;&gt; = 12.842754043944451

* u6A13 (U+6A13): L&lt;&lt;829.0,263.0&gt;--&lt;649.0,263.0&gt;&gt;/L&lt;&lt;649.0,263.0&gt;--&lt;673.0,258.0&gt;&gt; = 11.768288932020628

* u6A35 (U+6A35): L&lt;&lt;197.0,-58.0&gt;--&lt;197.0,262.0&gt;&gt;/L&lt;&lt;197.0,262.0&gt;--&lt;157.0,102.0&gt;&gt; = 14.036243467926484

* u6A52 (U+6A52): L&lt;&lt;195.0,-56.0&gt;--&lt;195.0,283.0&gt;&gt;/L&lt;&lt;195.0,283.0&gt;--&lt;155.0,112.0&gt;&gt; = 13.165794454440796

* u6A53 (U+6A53): L&lt;&lt;449.0,502.0&gt;--&lt;449.0,430.0&gt;&gt;/L&lt;&lt;449.0,430.0&gt;--&lt;462.0,482.0&gt;&gt; = 14.036243467926484

* u6A5E (U+6A5E): L&lt;&lt;801.0,315.0&gt;--&lt;823.0,319.0&gt;&gt;/L&lt;&lt;823.0,319.0&gt;--&lt;814.0,319.0&gt;&gt; = 10.304846468766044

* u6A73 (U+6A73): L&lt;&lt;176.0,-50.0&gt;--&lt;176.0,256.0&gt;&gt;/L&lt;&lt;176.0,256.0&gt;--&lt;142.0,112.0&gt;&gt; = 13.284866484902187

* u6A91 (U+6A91): L&lt;&lt;195.0,-56.0&gt;--&lt;195.0,283.0&gt;&gt;/L&lt;&lt;195.0,283.0&gt;--&lt;155.0,112.0&gt;&gt; = 13.165794454440796

* u6AA0 (U+6AA0): L&lt;&lt;179.0,336.0&gt;--&lt;179.0,433.0&gt;&gt;/L&lt;&lt;179.0,433.0&gt;--&lt;177.0,425.0&gt;&gt; = 14.036243467926484

* u6AAB (U+6AAB): L&lt;&lt;689.0,579.0&gt;--&lt;866.0,579.0&gt;&gt;/L&lt;&lt;866.0,579.0&gt;--&lt;820.0,582.0&gt;&gt; = 3.7313969991604012

* u6AAC (U+6AAC): L&lt;&lt;829.0,520.0&gt;--&lt;829.0,493.0&gt;&gt;/L&lt;&lt;829.0,493.0&gt;--&lt;839.0,574.0&gt;&gt; = 7.037940763184638

* u6AB3 (U+6AB3): L&lt;&lt;201.0,-50.0&gt;--&lt;201.0,261.0&gt;&gt;/L&lt;&lt;201.0,261.0&gt;--&lt;165.0,112.0&gt;&gt; = 13.582963529836702

* u6ABB (U+6ABB): L&lt;&lt;190.0,-48.0&gt;--&lt;190.0,270.0&gt;&gt;/L&lt;&lt;190.0,270.0&gt;--&lt;155.0,112.0&gt;&gt; = 12.49040571790919

* u6AC8 (U+6AC8): L&lt;&lt;591.0,270.0&gt;--&lt;581.0,268.0&gt;&gt;/L&lt;&lt;581.0,268.0&gt;--&lt;712.0,268.0&gt;&gt; = 11.309932474020195

* u6ADE (U+6ADE): L&lt;&lt;783.0,460.0&gt;--&lt;805.0,464.0&gt;&gt;/L&lt;&lt;805.0,464.0&gt;--&lt;787.0,464.0&gt;&gt; = 10.304846468766044

* u6AE2 (U+6AE2): L&lt;&lt;181.0,-50.0&gt;--&lt;181.0,282.0&gt;&gt;/L&lt;&lt;181.0,282.0&gt;--&lt;143.0,112.0&gt;&gt; = 12.600159826080658

* u6AE4 (U+6AE4): L&lt;&lt;204.0,-58.0&gt;--&lt;204.0,282.0&gt;&gt;/L&lt;&lt;204.0,282.0&gt;--&lt;165.0,112.0&gt;&gt; = 12.92075033583156

* u6B0C (U+6B0C): L&lt;&lt;758.0,44.0&gt;--&lt;758.0,12.0&gt;&gt;/L&lt;&lt;758.0,12.0&gt;--&lt;811.0,227.0&gt;&gt; = 13.847977619160014

* u6B13 (U+6B13): L&lt;&lt;183.0,-58.0&gt;--&lt;183.0,282.0&gt;&gt;/L&lt;&lt;183.0,282.0&gt;--&lt;144.0,112.0&gt;&gt; = 12.92075033583156

* u6B54 (U+6B54): L&lt;&lt;165.0,-24.0&gt;--&lt;165.0,23.0&gt;&gt;/L&lt;&lt;165.0,23.0&gt;--&lt;163.0,-49.0&gt;&gt; = 1.5911402711945815

* u6B5C (U+6B5C): L&lt;&lt;154.0,144.0&gt;--&lt;154.0,331.0&gt;&gt;/L&lt;&lt;154.0,331.0&gt;--&lt;138.0,263.0&gt;&gt; = 13.24051991518721

* u6B8B (U+6B8B): L&lt;&lt;531.0,736.0&gt;--&lt;339.0,736.0&gt;&gt;/L&lt;&lt;339.0,736.0&gt;--&lt;346.0,735.0&gt;&gt; = 8.13010235415596

* u6B9B (U+6B9B): L&lt;&lt;391.0,24.0&gt;--&lt;628.0,24.0&gt;&gt;/L&lt;&lt;628.0,24.0&gt;--&lt;523.0,42.0&gt;&gt; = 9.727578551401587

* u6BAA (U+6BAA): L&lt;&lt;645.0,27.0&gt;--&lt;610.0,24.0&gt;&gt;/L&lt;&lt;610.0,24.0&gt;--&lt;712.0,24.0&gt;&gt; = 4.899092453787774

* u6C6D (U+6C6D): L&lt;&lt;503.0,600.0&gt;--&lt;503.0,232.0&gt;&gt;/L&lt;&lt;503.0,232.0&gt;--&lt;595.0,600.0&gt;&gt; = 14.036243467926484

* u6D27 (U+6D27): L&lt;&lt;509.0,-52.0&gt;--&lt;509.0,436.0&gt;&gt;/L&lt;&lt;509.0,436.0&gt;--&lt;431.0,56.0&gt;&gt; = 11.599595221116342

* u6DAB (U+6DAB): L&lt;&lt;815.0,554.0&gt;--&lt;815.0,498.0&gt;&gt;/L&lt;&lt;815.0,498.0&gt;--&lt;830.0,630.0&gt;&gt; = 6.483073692897206

* u6DAC (U+6DAC): L&lt;&lt;576.0,334.0&gt;--&lt;528.0,332.0&gt;&gt;/L&lt;&lt;528.0,332.0&gt;--&lt;706.0,332.0&gt;&gt; = 2.3859440303887243

* u6E38 (U+6E38): L&lt;&lt;671.0,463.0&gt;--&lt;671.0,498.0&gt;&gt;/L&lt;&lt;671.0,498.0&gt;--&lt;661.0,451.0&gt;&gt; = 12.01147838636543

* u6E7A (U+6E7A): L&lt;&lt;678.0,-58.0&gt;--&lt;678.0,309.0&gt;&gt;/L&lt;&lt;678.0,309.0&gt;--&lt;594.0,-25.0&gt;&gt; = 14.11694169556958

* u6E7A (U+6E7A): L&lt;&lt;845.0,-24.0&gt;--&lt;776.0,317.0&gt;&gt;/L&lt;&lt;776.0,317.0&gt;--&lt;776.0,-58.0&gt;&gt; = 11.439122287807166

* u6EC5 (U+6EC5): L&lt;&lt;453.0,445.0&gt;--&lt;476.0,222.0&gt;&gt;/L&lt;&lt;476.0,222.0&gt;--&lt;508.0,482.0&gt;&gt; = 12.905110490768532

* u6EF4 (U+6EF4): L&lt;&lt;932.0,631.0&gt;--&lt;793.0,631.0&gt;&gt;/L&lt;&lt;793.0,631.0&gt;--&lt;806.0,629.0&gt;&gt; = 8.746162262555211

* u6F0A (U+6F0A): L&lt;&lt;808.0,263.0&gt;--&lt;595.0,263.0&gt;&gt;/L&lt;&lt;595.0,263.0&gt;--&lt;621.0,257.0&gt;&gt; = 12.994616791916512

* u6F41 (U+6F41): L&lt;&lt;403.0,198.0&gt;--&lt;357.0,227.0&gt;&gt;/L&lt;&lt;357.0,227.0&gt;--&lt;541.0,40.0&gt;&gt; = 13.234540657243226

* u6F5B (U+6F5B): L&lt;&lt;403.0,632.0&gt;--&lt;327.0,632.0&gt;&gt;/L&lt;&lt;327.0,632.0&gt;--&lt;368.0,622.0&gt;&gt; = 13.70696100407981

* u6F5B (U+6F5B): L&lt;&lt;745.0,632.0&gt;--&lt;634.0,632.0&gt;&gt;/L&lt;&lt;634.0,632.0&gt;--&lt;689.0,619.0&gt;&gt; = 13.298570330494275

* u6FA7 (U+6FA7): L&lt;&lt;477.0,115.0&gt;--&lt;514.0,123.0&gt;&gt;/L&lt;&lt;514.0,123.0&gt;--&lt;477.0,123.0&gt;&gt; = 12.200468727380786

* u6FA7 (U+6FA7): L&lt;&lt;558.0,30.0&gt;--&lt;523.0,24.0&gt;&gt;/L&lt;&lt;523.0,24.0&gt;--&lt;714.0,24.0&gt;&gt; = 9.727578551401587

* u6FAF (U+6FAF): L&lt;&lt;524.0,231.0&gt;--&lt;455.0,219.0&gt;&gt;/L&lt;&lt;455.0,219.0&gt;--&lt;560.0,219.0&gt;&gt; = 9.865806943084365

* u6FF0 (U+6FF0): L&lt;&lt;638.0,-50.0&gt;--&lt;638.0,394.0&gt;&gt;/L&lt;&lt;638.0,394.0&gt;--&lt;635.0,382.0&gt;&gt; = 14.036243467926484

* u7009 (U+7009): L&lt;&lt;837.0,615.0&gt;--&lt;837.0,611.0&gt;&gt;/L&lt;&lt;837.0,611.0&gt;--&lt;846.0,680.0&gt;&gt; = 7.431407971172489

* u701B (U+701B): L&lt;&lt;758.0,74.0&gt;--&lt;743.0,216.0&gt;&gt;/B&lt;&lt;743.0,216.0&gt;-&lt;737.0,18.0&gt;-&lt;716.0,-56.0&gt;&gt; = 7.765713397209828

* u701B (U+701B): L&lt;&lt;786.0,253.0&gt;--&lt;801.0,115.0&gt;&gt;/L&lt;&lt;801.0,115.0&gt;--&lt;801.0,331.0&gt;&gt; = 6.203447901691829

* u7032 (U+7032): L&lt;&lt;347.0,226.0&gt;--&lt;347.0,214.0&gt;&gt;/L&lt;&lt;347.0,214.0&gt;--&lt;350.0,226.0&gt;&gt; = 14.036243467926484

* u7067 (U+7067): L&lt;&lt;418.0,35.0&gt;--&lt;361.0,24.0&gt;&gt;/L&lt;&lt;361.0,24.0&gt;--&lt;443.0,24.0&gt;&gt; = 10.922804719869259

* u7069 (U+7069): L&lt;&lt;418.0,35.0&gt;--&lt;361.0,24.0&gt;&gt;/L&lt;&lt;361.0,24.0&gt;--&lt;443.0,24.0&gt;&gt; = 10.922804719869259

* u707F (U+707F): B&lt;&lt;323.0,830.0&gt;-&lt;323.0,667.0&gt;-&lt;315.0,544.0&gt;&gt;/L&lt;&lt;315.0,544.0&gt;--&lt;371.0,717.0&gt;&gt; = 14.215423945558586

* u7080 (U+7080): B&lt;&lt;314.0,810.0&gt;-&lt;314.0,647.0&gt;-&lt;306.0,526.0&gt;&gt;/L&lt;&lt;306.0,526.0&gt;--&lt;361.0,707.0&gt;&gt; = 13.11967158596773

* u7086 (U+7086): B&lt;&lt;327.0,810.0&gt;-&lt;327.0,629.0&gt;-&lt;315.0,495.0&gt;&gt;/L&lt;&lt;315.0,495.0&gt;--&lt;385.0,698.0&gt;&gt; = 13.90829118759605

* u70AE (U+70AE): L&lt;&lt;542.0,530.0&gt;--&lt;542.0,536.0&gt;&gt;/L&lt;&lt;542.0,536.0&gt;--&lt;541.0,530.0&gt;&gt; = 9.462322208025613

* u70B7 (U+70B7): B&lt;&lt;315.0,808.0&gt;-&lt;315.0,556.0&gt;-&lt;291.0,402.0&gt;&gt;/L&lt;&lt;291.0,402.0&gt;--&lt;380.0,636.0&gt;&gt; = 11.965946961295248

* u70BC (U+70BC): B&lt;&lt;306.0,808.0&gt;-&lt;306.0,556.0&gt;-&lt;282.0,402.0&gt;&gt;/L&lt;&lt;282.0,402.0&gt;--&lt;371.0,636.0&gt;&gt; = 11.965946961295248

* u70C1 (U+70C1): B&lt;&lt;324.0,808.0&gt;-&lt;324.0,556.0&gt;-&lt;300.0,402.0&gt;&gt;/L&lt;&lt;300.0,402.0&gt;--&lt;389.0,636.0&gt;&gt; = 11.965946961295248

* u70C2 (U+70C2): B&lt;&lt;315.0,808.0&gt;-&lt;315.0,556.0&gt;-&lt;291.0,402.0&gt;&gt;/L&lt;&lt;291.0,402.0&gt;--&lt;380.0,636.0&gt;&gt; = 11.965946961295248

* u70C3 (U+70C3): B&lt;&lt;338.0,808.0&gt;-&lt;338.0,556.0&gt;-&lt;312.0,402.0&gt;&gt;/L&lt;&lt;312.0,402.0&gt;--&lt;410.0,636.0&gt;&gt; = 13.141157428208436

* u70D9 (U+70D9): B&lt;&lt;295.0,830.0&gt;-&lt;295.0,609.0&gt;-&lt;278.0,450.0&gt;&gt;/L&lt;&lt;278.0,450.0&gt;--&lt;369.0,718.0&gt;&gt; = 12.65225399304788

* u70DB (U+70DB): B&lt;&lt;287.0,830.0&gt;-&lt;287.0,640.0&gt;-&lt;275.0,503.0&gt;&gt;/L&lt;&lt;275.0,503.0&gt;--&lt;346.0,717.0&gt;&gt; = 13.348757585616422

* u70E4 (U+70E4): B&lt;&lt;286.0,830.0&gt;-&lt;286.0,654.0&gt;-&lt;276.0,531.0&gt;&gt;/L&lt;&lt;276.0,531.0&gt;--&lt;338.0,717.0&gt;&gt; = 13.786978131534957

* u70E7 (U+70E7): B&lt;&lt;293.0,830.0&gt;-&lt;293.0,605.0&gt;-&lt;277.0,455.0&gt;&gt;/L&lt;&lt;277.0,455.0&gt;--&lt;363.0,717.0&gt;&gt; = 12.083597835490254

* u70E8 (U+70E8): B&lt;&lt;294.0,810.0&gt;-&lt;294.0,629.0&gt;-&lt;284.0,499.0&gt;&gt;/L&lt;&lt;284.0,499.0&gt;--&lt;352.0,717.0&gt;&gt; = 12.925384184975417

* u70EC (U+70EC): B&lt;&lt;273.0,830.0&gt;-&lt;273.0,628.0&gt;-&lt;262.0,487.0&gt;&gt;/L&lt;&lt;262.0,487.0&gt;--&lt;327.0,717.0&gt;&gt; = 11.319905050998788

* u70F1 (U+70F1): B&lt;&lt;311.0,830.0&gt;-&lt;311.0,640.0&gt;-&lt;299.0,502.0&gt;&gt;/L&lt;&lt;299.0,502.0&gt;--&lt;372.0,718.0&gt;&gt; = 13.703608020731936

* u70FA (U+70FA): B&lt;&lt;303.0,811.0&gt;-&lt;303.0,600.0&gt;-&lt;288.0,451.0&gt;&gt;/L&lt;&lt;288.0,451.0&gt;--&lt;379.0,718.0&gt;&gt; = 13.071677213367307

* u70FB (U+70FB): B&lt;&lt;292.0,830.0&gt;-&lt;292.0,677.0&gt;-&lt;284.0,544.0&gt;&gt;/L&lt;&lt;284.0,544.0&gt;--&lt;339.0,717.0&gt;&gt; = 14.194237786710927

* u7106 (U+7106): B&lt;&lt;306.0,811.0&gt;-&lt;306.0,600.0&gt;-&lt;291.0,451.0&gt;&gt;/L&lt;&lt;291.0,451.0&gt;--&lt;382.0,718.0&gt;&gt; = 13.071677213367307

* u7110 (U+7110): B&lt;&lt;303.0,811.0&gt;-&lt;303.0,600.0&gt;-&lt;288.0,451.0&gt;&gt;/L&lt;&lt;288.0,451.0&gt;--&lt;379.0,718.0&gt;&gt; = 13.071677213367307

* u7117 (U+7117): B&lt;&lt;297.0,830.0&gt;-&lt;297.0,654.0&gt;-&lt;287.0,531.0&gt;&gt;/L&lt;&lt;287.0,531.0&gt;--&lt;349.0,717.0&gt;&gt; = 13.786978131534957

* u7145 (U+7145): B&lt;&lt;293.0,830.0&gt;-&lt;293.0,640.0&gt;-&lt;281.0,503.0&gt;&gt;/L&lt;&lt;281.0,503.0&gt;--&lt;352.0,717.0&gt;&gt; = 13.348757585616422

* u7146 (U+7146): B&lt;&lt;297.0,830.0&gt;-&lt;297.0,654.0&gt;-&lt;287.0,531.0&gt;&gt;/L&lt;&lt;287.0,531.0&gt;--&lt;349.0,717.0&gt;&gt; = 13.786978131534957

* u7149 (U+7149): B&lt;&lt;310.0,808.0&gt;-&lt;310.0,573.0&gt;-&lt;286.0,402.0&gt;&gt;/L&lt;&lt;286.0,402.0&gt;--&lt;375.0,636.0&gt;&gt; = 12.8345789585267

* u714A (U+714A): B&lt;&lt;290.0,810.0&gt;-&lt;290.0,653.0&gt;-&lt;284.0,533.0&gt;&gt;/L&lt;&lt;284.0,533.0&gt;--&lt;331.0,697.0&gt;&gt; = 13.129122532405301

* u714B (U+714B): L&lt;&lt;537.0,129.0&gt;--&lt;537.0,170.0&gt;&gt;/L&lt;&lt;537.0,170.0&gt;--&lt;519.0,52.0&gt;&gt; = 8.673174047879721

* u7150 (U+7150): B&lt;&lt;294.0,810.0&gt;-&lt;294.0,629.0&gt;-&lt;284.0,499.0&gt;&gt;/L&lt;&lt;284.0,499.0&gt;--&lt;352.0,717.0&gt;&gt; = 12.925384184975417

* u7159 (U+7159): B&lt;&lt;290.0,810.0&gt;-&lt;290.0,653.0&gt;-&lt;284.0,533.0&gt;&gt;/L&lt;&lt;284.0,533.0&gt;--&lt;331.0,697.0&gt;&gt; = 13.129122532405301

* u715C (U+715C): B&lt;&lt;303.0,811.0&gt;-&lt;303.0,600.0&gt;-&lt;288.0,451.0&gt;&gt;/L&lt;&lt;288.0,451.0&gt;--&lt;379.0,718.0&gt;&gt; = 13.071677213367307

* u7164 (U+7164): B&lt;&lt;291.0,830.0&gt;-&lt;291.0,619.0&gt;-&lt;274.0,461.0&gt;&gt;/L&lt;&lt;274.0,461.0&gt;--&lt;366.0,718.0&gt;&gt; = 13.555071082188086

* u7168 (U+7168): B&lt;&lt;290.0,810.0&gt;-&lt;290.0,653.0&gt;-&lt;284.0,533.0&gt;&gt;/L&lt;&lt;284.0,533.0&gt;--&lt;331.0,697.0&gt;&gt; = 13.129122532405301

* u716C (U+716C): B&lt;&lt;302.0,810.0&gt;-&lt;302.0,656.0&gt;-&lt;294.0,526.0&gt;&gt;/L&lt;&lt;294.0,526.0&gt;--&lt;349.0,707.0&gt;&gt; = 13.380863655641793

* u7184 (U+7184): B&lt;&lt;307.0,830.0&gt;-&lt;307.0,663.0&gt;-&lt;298.0,537.0&gt;&gt;/L&lt;&lt;298.0,537.0&gt;--&lt;357.0,717.0&gt;&gt; = 14.062377282713772

* u7194 (U+7194): B&lt;&lt;280.0,817.0&gt;-&lt;280.0,683.0&gt;-&lt;274.0,575.0&gt;&gt;/L&lt;&lt;274.0,575.0&gt;--&lt;323.0,731.0&gt;&gt; = 14.257807415106178

* u71A0 (U+71A0): B&lt;&lt;287.0,830.0&gt;-&lt;287.0,643.0&gt;-&lt;275.0,503.0&gt;&gt;/L&lt;&lt;275.0,503.0&gt;--&lt;346.0,717.0&gt;&gt; = 13.455497684779733

* u71A5 (U+71A5): B&lt;&lt;288.0,830.0&gt;-&lt;288.0,630.0&gt;-&lt;273.0,460.0&gt;&gt;/L&lt;&lt;273.0,460.0&gt;--&lt;355.0,717.0&gt;&gt; = 12.653671679342597

* u71B0 (U+71B0): B&lt;&lt;280.0,810.0&gt;-&lt;280.0,682.0&gt;-&lt;277.0,580.0&gt;&gt;/L&lt;&lt;277.0,580.0&gt;--&lt;314.0,717.0&gt;&gt; = 13.428788741679712

* u71B5 (U+71B5): B&lt;&lt;278.0,830.0&gt;-&lt;278.0,663.0&gt;-&lt;269.0,535.0&gt;&gt;/L&lt;&lt;269.0,535.0&gt;--&lt;325.0,717.0&gt;&gt; = 13.08073879203223

* u71B5 (U+71B5): L&lt;&lt;884.0,623.0&gt;--&lt;784.0,623.0&gt;&gt;/L&lt;&lt;784.0,623.0&gt;--&lt;800.0,621.0&gt;&gt; = 7.125016348901757

* u71BA (U+71BA): B&lt;&lt;297.0,830.0&gt;-&lt;297.0,654.0&gt;-&lt;287.0,531.0&gt;&gt;/L&lt;&lt;287.0,531.0&gt;--&lt;349.0,717.0&gt;&gt; = 13.786978131534957

* u71BB (U+71BB): B&lt;&lt;266.0,830.0&gt;-&lt;266.0,638.0&gt;-&lt;255.0,487.0&gt;&gt;/L&lt;&lt;255.0,487.0&gt;--&lt;321.0,717.0&gt;&gt; = 11.844672593259789

* u71BE (U+71BE): B&lt;&lt;274.0,830.0&gt;-&lt;274.0,660.0&gt;-&lt;267.0,544.0&gt;&gt;/L&lt;&lt;267.0,544.0&gt;--&lt;313.0,717.0&gt;&gt; = 11.436866116796024

* u71C1 (U+71C1): B&lt;&lt;290.0,810.0&gt;-&lt;290.0,646.0&gt;-&lt;280.0,499.0&gt;&gt;/L&lt;&lt;280.0,499.0&gt;--&lt;348.0,717.0&gt;&gt; = 13.432413245890185

* u71C3 (U+71C3): B&lt;&lt;268.0,830.0&gt;-&lt;268.0,657.0&gt;-&lt;258.0,504.0&gt;&gt;/L&lt;&lt;258.0,504.0&gt;--&lt;319.0,717.0&gt;&gt; = 12.241413785463854

* u71C8 (U+71C8): B&lt;&lt;273.0,830.0&gt;-&lt;273.0,646.0&gt;-&lt;262.0,498.0&gt;&gt;/L&lt;&lt;262.0,498.0&gt;--&lt;330.0,717.0&gt;&gt; = 12.999033429648398

* u71C9 (U+71C9): B&lt;&lt;280.0,810.0&gt;-&lt;280.0,682.0&gt;-&lt;277.0,580.0&gt;&gt;/L&lt;&lt;277.0,580.0&gt;--&lt;314.0,717.0&gt;&gt; = 13.428788741679712

* u71CB (U+71CB): B&lt;&lt;301.0,810.0&gt;-&lt;301.0,653.0&gt;-&lt;294.0,533.0&gt;&gt;/L&lt;&lt;294.0,533.0&gt;--&lt;344.0,697.0&gt;&gt; = 13.616842508260875

* u71CF (U+71CF): B&lt;&lt;288.0,810.0&gt;-&lt;288.0,646.0&gt;-&lt;278.0,499.0&gt;&gt;/L&lt;&lt;278.0,499.0&gt;--&lt;347.0,717.0&gt;&gt; = 13.671619760435904

* u71D2 (U+71D2): B&lt;&lt;293.0,830.0&gt;-&lt;293.0,620.0&gt;-&lt;277.0,455.0&gt;&gt;/L&lt;&lt;277.0,455.0&gt;--&lt;363.0,717.0&gt;&gt; = 12.63348845689495

* u71D6 (U+71D6): B&lt;&lt;288.0,810.0&gt;-&lt;288.0,646.0&gt;-&lt;278.0,499.0&gt;&gt;/L&lt;&lt;278.0,499.0&gt;--&lt;347.0,717.0&gt;&gt; = 13.671619760435904

* u71D7 (U+71D7): B&lt;&lt;309.0,830.0&gt;-&lt;309.0,648.0&gt;-&lt;299.0,522.0&gt;&gt;/L&lt;&lt;299.0,522.0&gt;--&lt;361.0,717.0&gt;&gt; = 13.100223054390652

* u71DC (U+71DC): B&lt;&lt;264.0,830.0&gt;-&lt;264.0,638.0&gt;-&lt;253.0,487.0&gt;&gt;/L&lt;&lt;253.0,487.0&gt;--&lt;318.0,717.0&gt;&gt; = 11.61424842396666

* u71E0 (U+71E0): B&lt;&lt;279.0,830.0&gt;-&lt;279.0,648.0&gt;-&lt;268.0,503.0&gt;&gt;/L&lt;&lt;268.0,503.0&gt;--&lt;338.0,738.0&gt;&gt; = 12.249071765499224

* u71E5 (U+71E5): B&lt;&lt;278.0,830.0&gt;-&lt;278.0,663.0&gt;-&lt;269.0,535.0&gt;&gt;/L&lt;&lt;269.0,535.0&gt;--&lt;325.0,717.0&gt;&gt; = 13.08073879203223

* u71EC (U+71EC): B&lt;&lt;259.0,810.0&gt;-&lt;259.0,655.0&gt;-&lt;253.0,538.0&gt;&gt;/L&lt;&lt;253.0,538.0&gt;--&lt;296.0,716.0&gt;&gt; = 10.645248908513866

* u71ED (U+71ED): B&lt;&lt;287.0,830.0&gt;-&lt;287.0,643.0&gt;-&lt;275.0,503.0&gt;&gt;/L&lt;&lt;275.0,503.0&gt;--&lt;346.0,717.0&gt;&gt; = 13.455497684779733

* u71F4 (U+71F4): B&lt;&lt;281.0,830.0&gt;-&lt;281.0,663.0&gt;-&lt;272.0,535.0&gt;&gt;/L&lt;&lt;272.0,535.0&gt;--&lt;328.0,717.0&gt;&gt; = 13.08073879203223

* u71F5 (U+71F5): B&lt;&lt;288.0,830.0&gt;-&lt;288.0,630.0&gt;-&lt;273.0,460.0&gt;&gt;/L&lt;&lt;273.0,460.0&gt;--&lt;355.0,717.0&gt;&gt; = 12.653671679342597

* u71F6 (U+71F6): B&lt;&lt;278.0,830.0&gt;-&lt;278.0,663.0&gt;-&lt;269.0,535.0&gt;&gt;/L&lt;&lt;269.0,535.0&gt;--&lt;325.0,717.0&gt;&gt; = 13.08073879203223

* u71F8 (U+71F8): B&lt;&lt;262.0,830.0&gt;-&lt;262.0,638.0&gt;-&lt;251.0,487.0&gt;&gt;/L&lt;&lt;251.0,487.0&gt;--&lt;316.0,717.0&gt;&gt; = 11.61424842396666

* u71FB (U+71FB): B&lt;&lt;297.0,809.0&gt;-&lt;297.0,634.0&gt;-&lt;286.0,496.0&gt;&gt;/L&lt;&lt;286.0,496.0&gt;--&lt;355.0,717.0&gt;&gt; = 12.781842468326465

* u71FC (U+71FC): B&lt;&lt;262.0,830.0&gt;-&lt;262.0,638.0&gt;-&lt;251.0,487.0&gt;&gt;/L&lt;&lt;251.0,487.0&gt;--&lt;316.0,717.0&gt;&gt; = 11.61424842396666

* u71FF (U+71FF): B&lt;&lt;293.0,830.0&gt;-&lt;293.0,628.0&gt;-&lt;279.0,476.0&gt;&gt;/L&lt;&lt;279.0,476.0&gt;--&lt;360.0,718.0&gt;&gt; = 13.24355187461188

* u7200 (U+7200): B&lt;&lt;249.0,810.0&gt;-&lt;249.0,655.0&gt;-&lt;243.0,538.0&gt;&gt;/L&lt;&lt;243.0,538.0&gt;--&lt;284.0,716.0&gt;&gt; = 10.035432563264179

* u7206 (U+7206): B&lt;&lt;292.0,830.0&gt;-&lt;292.0,674.0&gt;-&lt;284.0,540.0&gt;&gt;/L&lt;&lt;284.0,540.0&gt;--&lt;336.0,717.0&gt;&gt; = 12.955425137758734

* u7207 (U+7207): L&lt;&lt;333.0,188.0&gt;--&lt;302.0,184.0&gt;&gt;/L&lt;&lt;302.0,184.0&gt;--&lt;337.0,187.0&gt;&gt; = 2.453286906104442

* u720C (U+720C): B&lt;&lt;302.0,810.0&gt;-&lt;302.0,656.0&gt;-&lt;294.0,526.0&gt;&gt;/L&lt;&lt;294.0,526.0&gt;--&lt;349.0,707.0&gt;&gt; = 13.380863655641793

* u720D (U+720D): B&lt;&lt;251.0,830.0&gt;-&lt;251.0,662.0&gt;-&lt;243.0,521.0&gt;&gt;/L&lt;&lt;243.0,521.0&gt;--&lt;292.0,716.0&gt;&gt; = 10.858014974012308

* u7210 (U+7210): B&lt;&lt;257.0,830.0&gt;-&lt;257.0,651.0&gt;-&lt;248.0,517.0&gt;&gt;/L&lt;&lt;248.0,517.0&gt;--&lt;306.0,717.0&gt;&gt; = 12.329705887867648

* u721B (U+721B): B&lt;&lt;292.0,830.0&gt;-&lt;292.0,660.0&gt;-&lt;283.0,529.0&gt;&gt;/L&lt;&lt;283.0,529.0&gt;--&lt;341.0,717.0&gt;&gt; = 13.215375373136217

* u722A (U+722A): L&lt;&lt;870.0,753.0&gt;--&lt;728.0,717.0&gt;&gt;/L&lt;&lt;728.0,717.0&gt;--&lt;794.0,723.0&gt;&gt; = 9.031534991016981

* u7231 (U+7231): L&lt;&lt;553.0,546.0&gt;--&lt;548.0,545.0&gt;&gt;/L&lt;&lt;548.0,545.0&gt;--&lt;675.0,545.0&gt;&gt; = 11.309932474020195

* u7258 (U+7258): L&lt;&lt;534.0,473.0&gt;--&lt;532.0,485.0&gt;&gt;/L&lt;&lt;532.0,485.0&gt;--&lt;532.0,462.0&gt;&gt; = 9.462322208025613

* u72CD (U+72CD): L&lt;&lt;484.0,-24.0&gt;--&lt;484.0,401.0&gt;&gt;/L&lt;&lt;484.0,401.0&gt;--&lt;477.0,356.0&gt;&gt; = 8.84181456019167

* u7363 (U+7363): L&lt;&lt;210.0,613.0&gt;--&lt;116.0,603.0&gt;&gt;/L&lt;&lt;116.0,603.0&gt;--&lt;203.0,603.0&gt;&gt; = 6.0724564072076905

* u7374 (U+7374): L&lt;&lt;796.0,520.0&gt;--&lt;796.0,517.0&gt;&gt;/L&lt;&lt;796.0,517.0&gt;--&lt;803.0,574.0&gt;&gt; = 7.001267557495299

* u742F (U+742F): L&lt;&lt;813.0,554.0&gt;--&lt;813.0,498.0&gt;&gt;/L&lt;&lt;813.0,498.0&gt;--&lt;828.0,630.0&gt;&gt; = 6.483073692897206

* u7433 (U+7433): L&lt;&lt;441.0,-71.0&gt;--&lt;441.0,273.0&gt;&gt;/L&lt;&lt;441.0,273.0&gt;--&lt;375.0,11.0&gt;&gt; = 14.139108311650501

* u7446 (U+7446): L&lt;&lt;532.0,129.0&gt;--&lt;532.0,170.0&gt;&gt;/L&lt;&lt;532.0,170.0&gt;--&lt;514.0,52.0&gt;&gt; = 8.673174047879721

* u746C (U+746C): L&lt;&lt;662.0,690.0&gt;--&lt;735.0,704.0&gt;&gt;/L&lt;&lt;735.0,704.0&gt;--&lt;557.0,704.0&gt;&gt; = 10.856413348062235

* u746C (U+746C): L&lt;&lt;712.0,101.0&gt;--&lt;768.0,111.0&gt;&gt;/L&lt;&lt;768.0,111.0&gt;--&lt;561.0,111.0&gt;&gt; = 10.124671655397806

* u746C (U+746C): L&lt;&lt;828.0,43.0&gt;--&lt;783.0,35.0&gt;&gt;/L&lt;&lt;783.0,35.0&gt;--&lt;928.0,35.0&gt;&gt; = 10.08059798754231

* u7497 (U+7497): L&lt;&lt;710.0,79.0&gt;--&lt;766.0,89.0&gt;&gt;/L&lt;&lt;766.0,89.0&gt;--&lt;559.0,89.0&gt;&gt; = 10.124671655397806

* u7497 (U+7497): L&lt;&lt;826.0,28.0&gt;--&lt;781.0,21.0&gt;&gt;/L&lt;&lt;781.0,21.0&gt;--&lt;926.0,21.0&gt;&gt; = 8.84181456019167

* u74A4 (U+74A4): L&lt;&lt;799.0,315.0&gt;--&lt;821.0,319.0&gt;&gt;/L&lt;&lt;821.0,319.0&gt;--&lt;812.0,319.0&gt;&gt; = 10.304846468766044

* u74A6 (U+74A6): L&lt;&lt;558.0,122.0&gt;--&lt;537.0,90.0&gt;&gt;/L&lt;&lt;537.0,90.0&gt;--&lt;551.0,109.0&gt;&gt; = 3.109463831001076

* u74A7 (U+74A7): L&lt;&lt;710.0,87.0&gt;--&lt;766.0,97.0&gt;&gt;/L&lt;&lt;766.0,97.0&gt;--&lt;559.0,97.0&gt;&gt; = 10.124671655397806

* u74A7 (U+74A7): L&lt;&lt;826.0,32.0&gt;--&lt;781.0,24.0&gt;&gt;/L&lt;&lt;781.0,24.0&gt;--&lt;926.0,24.0&gt;&gt; = 10.08059798754231

* u74BD (U+74BD): L&lt;&lt;63.0,688.0&gt;--&lt;282.0,736.0&gt;&gt;/L&lt;&lt;282.0,736.0&gt;--&lt;70.0,736.0&gt;&gt; = 12.36249241571429

* u74DB (U+74DB): L&lt;&lt;849.0,-54.0&gt;--&lt;809.0,241.0&gt;&gt;/B&lt;&lt;809.0,241.0&gt;-&lt;802.0,156.0&gt;-&lt;791.5,87.5&gt;&gt; = 12.429678044503175

* u74DC (U+74DC): L&lt;&lt;870.0,753.0&gt;--&lt;728.0,717.0&gt;&gt;/L&lt;&lt;728.0,717.0&gt;--&lt;794.0,723.0&gt;&gt; = 9.031534991016981

* u750E (U+750E): L&lt;&lt;401.0,241.0&gt;--&lt;333.0,234.0&gt;&gt;/L&lt;&lt;333.0,234.0&gt;--&lt;405.0,234.0&gt;&gt; = 5.8773926066431

* u7525 (U+7525): L&lt;&lt;813.0,339.0&gt;--&lt;694.0,339.0&gt;&gt;/L&lt;&lt;694.0,339.0&gt;--&lt;728.0,331.0&gt;&gt; = 13.24051991518721

* u7551 (U+7551): B&lt;&lt;355.0,830.0&gt;-&lt;355.0,623.0&gt;-&lt;336.0,461.0&gt;&gt;/L&lt;&lt;336.0,461.0&gt;--&lt;413.0,717.0&gt;&gt; = 10.050986356750771

* u7579 (U+7579): L&lt;&lt;553.0,582.0&gt;--&lt;552.0,582.0&gt;&gt;/L&lt;&lt;552.0,582.0&gt;--&lt;587.0,577.0&gt;&gt; = 8.13010235415596

* u7582 (U+7582): L&lt;&lt;199.0,398.0&gt;--&lt;879.0,398.0&gt;&gt;/L&lt;&lt;879.0,398.0&gt;--&lt;578.0,443.0&gt;&gt; = 8.502839155857497

* u7582 (U+7582): L&lt;&lt;406.0,443.0&gt;--&lt;146.0,404.0&gt;&gt;/L&lt;&lt;146.0,404.0&gt;--&lt;199.0,404.0&gt;&gt; = 8.530765609948139

* u75B1 (U+75B1): L&lt;&lt;418.0,-24.0&gt;--&lt;418.0,327.0&gt;&gt;/L&lt;&lt;418.0,327.0&gt;--&lt;406.0,277.0&gt;&gt; = 13.495733280795811

* u7621 (U+7621): L&lt;&lt;422.0,-37.0&gt;--&lt;422.0,70.0&gt;&gt;/L&lt;&lt;422.0,70.0&gt;--&lt;401.0,-39.0&gt;&gt; = 10.905022045234425

* u7656 (U+7656): L&lt;&lt;404.0,-43.0&gt;--&lt;404.0,144.0&gt;&gt;/L&lt;&lt;404.0,144.0&gt;--&lt;395.0,-24.0&gt;&gt; = 3.0664855011258196

* u767B (U+767B): L&lt;&lt;400.0,42.0&gt;--&lt;323.0,24.0&gt;&gt;/L&lt;&lt;323.0,24.0&gt;--&lt;608.0,24.0&gt;&gt; = 13.157542740014783

* u769C (U+769C): L&lt;&lt;741.0,224.0&gt;--&lt;741.0,-1.0&gt;&gt;/L&lt;&lt;741.0,-1.0&gt;--&lt;744.0,17.0&gt;&gt; = 9.462322208025613

* u76B9 (U+76B9): L&lt;&lt;458.0,654.0&gt;--&lt;458.0,677.0&gt;&gt;/L&lt;&lt;458.0,677.0&gt;--&lt;430.0,430.0&gt;&gt; = 6.46745892779148

* u779C (U+779C): L&lt;&lt;811.0,263.0&gt;--&lt;622.0,263.0&gt;&gt;/L&lt;&lt;622.0,263.0&gt;--&lt;645.0,258.0&gt;&gt; = 12.2647737278924

* u77AC (U+77AC): L&lt;&lt;449.0,502.0&gt;--&lt;449.0,430.0&gt;&gt;/L&lt;&lt;449.0,430.0&gt;--&lt;462.0,482.0&gt;&gt; = 14.036243467926484

* u77B9 (U+77B9): L&lt;&lt;559.0,122.0&gt;--&lt;528.0,77.0&gt;&gt;/L&lt;&lt;528.0,77.0&gt;--&lt;552.0,109.0&gt;&gt; = 2.3073729969621

* u77C7 (U+77C7): L&lt;&lt;796.0,520.0&gt;--&lt;796.0,517.0&gt;&gt;/L&lt;&lt;796.0,517.0&gt;--&lt;803.0,574.0&gt;&gt; = 7.001267557495299

* u77DA (U+77DA): L&lt;&lt;736.0,71.0&gt;--&lt;767.0,78.0&gt;&gt;/L&lt;&lt;767.0,78.0&gt;--&lt;760.0,78.0&gt;&gt; = 12.724355685422363

* u77FE (U+77FE): L&lt;&lt;680.0,516.0&gt;--&lt;745.0,182.0&gt;&gt;/L&lt;&lt;745.0,182.0&gt;--&lt;745.0,736.0&gt;&gt; = 11.012723603415871

* u77FE (U+77FE): L&lt;&lt;681.0,162.0&gt;--&lt;618.0,486.0&gt;&gt;/B&lt;&lt;618.0,486.0&gt;-&lt;612.0,247.0&gt;-&lt;593.0,123.0&gt;&gt; = 12.441626559153134

* u7832 (U+7832): L&lt;&lt;602.0,486.0&gt;--&lt;602.0,523.0&gt;&gt;/L&lt;&lt;602.0,523.0&gt;--&lt;581.0,357.0&gt;&gt; = 7.209961845615799

* u784A (U+784A): L&lt;&lt;241.0,496.0&gt;--&lt;412.0,496.0&gt;&gt;/L&lt;&lt;412.0,496.0&gt;--&lt;408.0,497.0&gt;&gt; = 14.036243467926484

* u7897 (U+7897): L&lt;&lt;553.0,582.0&gt;--&lt;552.0,582.0&gt;&gt;/L&lt;&lt;552.0,582.0&gt;--&lt;587.0,577.0&gt;&gt; = 8.13010235415596

* u790E (U+790E): L&lt;&lt;865.0,415.0&gt;--&lt;845.0,495.0&gt;&gt;/L&lt;&lt;845.0,495.0&gt;--&lt;845.0,373.0&gt;&gt; = 14.036243467926484

* u791E (U+791E): L&lt;&lt;796.0,520.0&gt;--&lt;796.0,517.0&gt;&gt;/L&lt;&lt;796.0,517.0&gt;--&lt;803.0,574.0&gt;&gt; = 7.001267557495299

* u79AE (U+79AE): L&lt;&lt;565.0,115.0&gt;--&lt;602.0,123.0&gt;&gt;/L&lt;&lt;602.0,123.0&gt;--&lt;565.0,123.0&gt;&gt; = 12.200468727380786

* u79AE (U+79AE): L&lt;&lt;639.0,30.0&gt;--&lt;611.0,24.0&gt;&gt;/L&lt;&lt;611.0,24.0&gt;--&lt;727.0,24.0&gt;&gt; = 12.094757077012089

* u7A57 (U+7A57): L&lt;&lt;799.0,315.0&gt;--&lt;821.0,319.0&gt;&gt;/L&lt;&lt;821.0,319.0&gt;--&lt;812.0,319.0&gt;&gt; = 10.304846468766044

* u7AAE (U+7AAE): L&lt;&lt;90.0,6.0&gt;--&lt;325.0,90.0&gt;&gt;/L&lt;&lt;325.0,90.0&gt;--&lt;88.0,65.0&gt;&gt; = 13.64767752497373

* u7AC3 (U+7AC3): L&lt;&lt;648.0,641.0&gt;--&lt;812.0,641.0&gt;&gt;/L&lt;&lt;812.0,641.0&gt;--&lt;803.0,642.0&gt;&gt; = 6.340191745909908

* u7AE5 (U+7AE5): L&lt;&lt;258.0,709.0&gt;--&lt;329.0,719.0&gt;&gt;/L&lt;&lt;329.0,719.0&gt;--&lt;95.0,719.0&gt;&gt; = 8.017093073655333

* u7AE5 (U+7AE5): L&lt;&lt;386.0,595.0&gt;--&lt;315.0,585.0&gt;&gt;/L&lt;&lt;315.0,585.0&gt;--&lt;618.0,585.0&gt;&gt; = 8.017093073655333

* u7B66 (U+7B66): L&lt;&lt;101.0,498.0&gt;--&lt;126.0,498.0&gt;&gt;/L&lt;&lt;126.0,498.0&gt;--&lt;69.0,506.0&gt;&gt; = 7.989326766396871

* u7B8B (U+7B8B): L&lt;&lt;541.0,177.0&gt;--&lt;821.0,177.0&gt;&gt;/L&lt;&lt;821.0,177.0&gt;--&lt;622.0,220.0&gt;&gt; = 12.193034475506952

* u7B9F (U+7B9F): L&lt;&lt;157.0,532.0&gt;--&lt;161.0,532.0&gt;&gt;/L&lt;&lt;161.0,532.0&gt;--&lt;69.0,546.0&gt;&gt; = 8.652541791114704

* u7BA2 (U+7BA2): L&lt;&lt;101.0,498.0&gt;--&lt;126.0,498.0&gt;&gt;/L&lt;&lt;126.0,498.0&gt;--&lt;69.0,506.0&gt;&gt; = 7.989326766396871

* u7BB1 (U+7BB1): L&lt;&lt;399.0,532.0&gt;--&lt;305.0,522.0&gt;&gt;/L&lt;&lt;305.0,522.0&gt;--&lt;333.0,522.0&gt;&gt; = 6.0724564072076905

* u7BD4 (U+7BD4): L&lt;&lt;126.0,609.0&gt;--&lt;160.0,609.0&gt;&gt;/L&lt;&lt;160.0,609.0&gt;--&lt;72.0,629.0&gt;&gt; = 12.80426606528674

* u7BF1 (U+7BF1): L&lt;&lt;538.0,178.0&gt;--&lt;614.0,188.0&gt;&gt;/L&lt;&lt;614.0,188.0&gt;--&lt;490.0,188.0&gt;&gt; = 7.495857639729836

* u7BF3 (U+7BF3): L&lt;&lt;141.0,546.0&gt;--&lt;153.0,546.0&gt;&gt;/L&lt;&lt;153.0,546.0&gt;--&lt;68.0,559.0&gt;&gt; = 8.69550287742474

* u7C3E (U+7C3E): L&lt;&lt;277.0,446.0&gt;--&lt;524.0,508.0&gt;&gt;/L&lt;&lt;524.0,508.0&gt;--&lt;221.0,508.0&gt;&gt; = 14.09081086048848

* u7C63 (U+7C63): L&lt;&lt;106.0,609.0&gt;--&lt;129.0,609.0&gt;&gt;/L&lt;&lt;129.0,609.0&gt;--&lt;70.0,621.0&gt;&gt; = 11.496563017585768

* u7CB1 (U+7CB1): L&lt;&lt;364.0,213.0&gt;--&lt;272.0,199.0&gt;&gt;/L&lt;&lt;272.0,199.0&gt;--&lt;445.0,199.0&gt;&gt; = 8.652541791114704

* u7CB1 (U+7CB1): L&lt;&lt;541.0,199.0&gt;--&lt;699.0,199.0&gt;&gt;/L&lt;&lt;699.0,199.0&gt;--&lt;615.0,214.0&gt;&gt; = 10.124671655397806

* u7CB2 (U+7CB2): L&lt;&lt;387.0,230.0&gt;--&lt;303.0,219.0&gt;&gt;/L&lt;&lt;303.0,219.0&gt;--&lt;449.0,219.0&gt;&gt; = 7.460566126168332

* u7CB2 (U+7CB2): L&lt;&lt;545.0,219.0&gt;--&lt;667.0,219.0&gt;&gt;/L&lt;&lt;667.0,219.0&gt;--&lt;602.0,234.0&gt;&gt; = 12.994616791916512

* u7CD2 (U+7CD2): L&lt;&lt;500.0,-38.0&gt;--&lt;500.0,371.0&gt;&gt;/L&lt;&lt;500.0,371.0&gt;--&lt;446.0,139.0&gt;&gt; = 13.102789941262442

* u7D0D (U+7D0D): L&lt;&lt;570.0,600.0&gt;--&lt;570.0,256.0&gt;&gt;/L&lt;&lt;570.0,256.0&gt;--&lt;641.0,600.0&gt;&gt; = 11.661828426015832

* u7D9D (U+7D9D): L&lt;&lt;370.0,201.0&gt;--&lt;377.0,104.0&gt;&gt;/L&lt;&lt;377.0,104.0&gt;--&lt;459.0,602.0&gt;&gt; = 13.47793533093551

* u7D9D (U+7D9D): L&lt;&lt;498.0,-61.0&gt;--&lt;498.0,333.0&gt;&gt;/L&lt;&lt;498.0,333.0&gt;--&lt;457.0,87.0&gt;&gt; = 9.462322208025613

* u7D9D (U+7D9D): L&lt;&lt;730.0,-61.0&gt;--&lt;730.0,286.0&gt;&gt;/L&lt;&lt;730.0,286.0&gt;--&lt;678.0,5.0&gt;&gt; = 10.48417539652899

* u7D9D (U+7D9D): L&lt;&lt;876.0,5.0&gt;--&lt;814.0,288.0&gt;&gt;/L&lt;&lt;814.0,288.0&gt;--&lt;814.0,-61.0&gt;&gt; = 12.357199747537305

* u7DD7 (U+7DD7): L&lt;&lt;505.0,-68.0&gt;--&lt;505.0,308.0&gt;&gt;/L&lt;&lt;505.0,308.0&gt;--&lt;456.0,113.0&gt;&gt; = 14.10535776433523

* u7E05 (U+7E05): L&lt;&lt;708.0,89.0&gt;--&lt;704.0,46.0&gt;&gt;/L&lt;&lt;704.0,46.0&gt;--&lt;757.0,214.0&gt;&gt; = 12.194699120312906

* u7E37 (U+7E37): L&lt;&lt;809.0,263.0&gt;--&lt;629.0,263.0&gt;&gt;/L&lt;&lt;629.0,263.0&gt;--&lt;653.0,258.0&gt;&gt; = 11.768288932020628

* u7E41 (U+7E41): L&lt;&lt;200.0,717.0&gt;--&lt;184.0,662.0&gt;&gt;/L&lt;&lt;184.0,662.0&gt;--&lt;197.0,697.0&gt;&gt; = 4.1562415182336325

* u7E70 (U+7E70): L&lt;&lt;402.0,201.0&gt;--&lt;403.0,189.0&gt;&gt;/L&lt;&lt;403.0,189.0&gt;--&lt;403.0,234.0&gt;&gt; = 4.763641690726143

* u7E86 (U+7E86): L&lt;&lt;388.0,201.0&gt;--&lt;404.0,10.0&gt;&gt;/L&lt;&lt;404.0,10.0&gt;--&lt;404.0,24.0&gt;&gt; = 4.788466550313606

* u7F88 (U+7F88): L&lt;&lt;822.0,131.0&gt;--&lt;825.0,-18.0&gt;&gt;/L&lt;&lt;825.0,-18.0&gt;--&lt;828.0,-2.0&gt;&gt; = 11.773105727260502

* u7F95 (U+7F95): L&lt;&lt;90.0,292.0&gt;--&lt;595.0,292.0&gt;&gt;/L&lt;&lt;595.0,292.0&gt;--&lt;269.0,365.0&gt;&gt; = 12.62182025652434

* u7F95 (U+7F95): L&lt;&lt;930.0,399.0&gt;--&lt;340.0,399.0&gt;&gt;/L&lt;&lt;340.0,399.0&gt;--&lt;652.0,329.0&gt;&gt; = 12.645420396532943

* u7FA3 (U+7FA3): L&lt;&lt;216.0,341.0&gt;--&lt;268.0,353.0&gt;&gt;/L&lt;&lt;268.0,353.0&gt;--&lt;230.0,353.0&gt;&gt; = 12.994616791916512

* u7FA9 (U+7FA9): L&lt;&lt;524.0,378.0&gt;--&lt;606.0,397.0&gt;&gt;/L&lt;&lt;606.0,397.0&gt;--&lt;447.0,397.0&gt;&gt; = 13.045637062948598

* u7FBC (U+7FBC): L&lt;&lt;337.0,619.0&gt;--&lt;425.0,635.0&gt;&gt;/L&lt;&lt;425.0,635.0&gt;--&lt;200.0,635.0&gt;&gt; = 10.304846468766044

* u7FE9 (U+7FE9): L&lt;&lt;389.0,139.0&gt;--&lt;389.0,-12.0&gt;&gt;/L&lt;&lt;389.0,-12.0&gt;--&lt;396.0,23.0&gt;&gt; = 11.309932474020195

* u8006 (U+8006): L&lt;&lt;404.0,399.0&gt;--&lt;398.0,428.0&gt;&gt;/L&lt;&lt;398.0,428.0&gt;--&lt;398.0,348.0&gt;&gt; = 11.689369175439202

* u8009 (U+8009): L&lt;&lt;404.0,399.0&gt;--&lt;398.0,428.0&gt;&gt;/L&lt;&lt;398.0,428.0&gt;--&lt;398.0,348.0&gt;&gt; = 11.689369175439202

* u802A (U+802A): L&lt;&lt;522.0,524.0&gt;--&lt;520.0,533.0&gt;&gt;/L&lt;&lt;520.0,533.0&gt;--&lt;520.0,524.0&gt;&gt; = 12.528807709151492

* u802C (U+802C): L&lt;&lt;813.0,263.0&gt;--&lt;633.0,263.0&gt;&gt;/L&lt;&lt;633.0,263.0&gt;--&lt;657.0,258.0&gt;&gt; = 11.768288932020628

* u8077 (U+8077): L&lt;&lt;741.0,429.0&gt;--&lt;717.0,660.0&gt;&gt;/L&lt;&lt;717.0,660.0&gt;--&lt;717.0,636.0&gt;&gt; = 5.931526924919723

* u80AC (U+80AC): L&lt;&lt;649.0,-24.0&gt;--&lt;649.0,260.0&gt;&gt;/B&lt;&lt;649.0,260.0&gt;-&lt;624.0,150.0&gt;-&lt;589.5,81.0&gt;&gt; = 12.80426606528674

* u80AD (U+80AD): L&lt;&lt;546.0,600.0&gt;--&lt;546.0,256.0&gt;&gt;/L&lt;&lt;546.0,256.0&gt;--&lt;623.0,600.0&gt;&gt; = 12.616954992704374

* u8124 (U+8124): L&lt;&lt;545.0,358.0&gt;--&lt;545.0,396.0&gt;&gt;/L&lt;&lt;545.0,396.0&gt;--&lt;534.0,-50.0&gt;&gt; = 1.4128381782191464

* u8155 (U+8155): L&lt;&lt;538.0,582.0&gt;--&lt;537.0,582.0&gt;&gt;/L&lt;&lt;537.0,582.0&gt;--&lt;572.0,577.0&gt;&gt; = 8.13010235415596

* u8165 (U+8165): L&lt;&lt;554.0,129.0&gt;--&lt;554.0,170.0&gt;&gt;/L&lt;&lt;554.0,170.0&gt;--&lt;537.0,52.0&gt;&gt; = 8.198068846016264

* u8168 (U+8168): L&lt;&lt;370.0,325.0&gt;--&lt;371.0,331.0&gt;&gt;/L&lt;&lt;371.0,331.0&gt;--&lt;370.0,322.0&gt;&gt; = 3.1221304621157

* u8168 (U+8168): L&lt;&lt;370.0,785.0&gt;--&lt;370.0,325.0&gt;&gt;/L&lt;&lt;370.0,325.0&gt;--&lt;371.0,331.0&gt;&gt; = 9.462322208025613

* u816F (U+816F): L&lt;&lt;657.0,448.0&gt;--&lt;657.0,430.0&gt;&gt;/L&lt;&lt;657.0,430.0&gt;--&lt;666.0,520.0&gt;&gt; = 5.710593137499633

* u8180 (U+8180): L&lt;&lt;492.0,524.0&gt;--&lt;490.0,533.0&gt;&gt;/L&lt;&lt;490.0,533.0&gt;--&lt;490.0,524.0&gt;&gt; = 12.528807709151492

* u81A2 (U+81A2): L&lt;&lt;828.0,263.0&gt;--&lt;647.0,263.0&gt;&gt;/L&lt;&lt;647.0,263.0&gt;--&lt;670.0,258.0&gt;&gt; = 12.2647737278924

* u81C1 (U+81C1): L&lt;&lt;497.0,486.0&gt;--&lt;497.0,517.0&gt;&gt;/L&lt;&lt;497.0,517.0&gt;--&lt;469.0,-69.0&gt;&gt; = 2.7356016991130856

* u81DF (U+81DF): L&lt;&lt;758.0,44.0&gt;--&lt;758.0,12.0&gt;&gt;/L&lt;&lt;758.0,12.0&gt;--&lt;811.0,227.0&gt;&gt; = 13.847977619160014

* u8274 (U+8274): L&lt;&lt;383.0,254.0&gt;--&lt;383.0,30.0&gt;&gt;/L&lt;&lt;383.0,30.0&gt;--&lt;393.0,70.0&gt;&gt; = 14.036243467926484

* u8276 (U+8276): L&lt;&lt;202.0,116.0&gt;--&lt;251.0,123.0&gt;&gt;/L&lt;&lt;251.0,123.0&gt;--&lt;202.0,123.0&gt;&gt; = 8.13010235415596

* u8276 (U+8276): L&lt;&lt;389.0,123.0&gt;--&lt;367.0,123.0&gt;&gt;/L&lt;&lt;367.0,123.0&gt;--&lt;389.0,119.0&gt;&gt; = 10.304846468766044

* u8276 (U+8276): L&lt;&lt;485.0,108.0&gt;--&lt;442.0,108.0&gt;&gt;/L&lt;&lt;442.0,108.0&gt;--&lt;447.0,107.0&gt;&gt; = 11.309932474020195

* u8277 (U+8277): L&lt;&lt;282.0,34.0&gt;--&lt;211.0,24.0&gt;&gt;/L&lt;&lt;211.0,24.0&gt;--&lt;325.0,24.0&gt;&gt; = 8.017093073655333

* u8373 (U+8373): L&lt;&lt;402.0,42.0&gt;--&lt;325.0,24.0&gt;&gt;/L&lt;&lt;325.0,24.0&gt;--&lt;610.0,24.0&gt;&gt; = 13.157542740014783

* u839A (U+839A): L&lt;&lt;544.0,164.0&gt;--&lt;537.0,163.0&gt;&gt;/L&lt;&lt;537.0,163.0&gt;--&lt;641.0,163.0&gt;&gt; = 8.13010235415596

* u83E9 (U+83E9): L&lt;&lt;228.0,462.0&gt;--&lt;254.0,466.0&gt;&gt;/L&lt;&lt;254.0,466.0&gt;--&lt;110.0,466.0&gt;&gt; = 8.746162262555211

* u84CD (U+84CD): L&lt;&lt;403.0,301.0&gt;--&lt;398.0,331.0&gt;&gt;/L&lt;&lt;398.0,331.0&gt;--&lt;398.0,275.0&gt;&gt; = 9.462322208025613

* u84E0 (U+84E0): L&lt;&lt;538.0,178.0&gt;--&lt;614.0,188.0&gt;&gt;/L&lt;&lt;614.0,188.0&gt;--&lt;490.0,188.0&gt;&gt; = 7.495857639729836

* u8503 (U+8503): L&lt;&lt;792.0,112.0&gt;--&lt;862.0,122.0&gt;&gt;/L&lt;&lt;862.0,122.0&gt;--&lt;822.0,122.0&gt;&gt; = 8.13010235415596

* u8513 (U+8513): L&lt;&lt;465.0,75.0&gt;--&lt;664.0,120.0&gt;&gt;/L&lt;&lt;664.0,120.0&gt;--&lt;78.0,120.0&gt;&gt; = 12.742028658184863

* u8559 (U+8559): L&lt;&lt;872.0,119.0&gt;--&lt;852.0,134.0&gt;&gt;/L&lt;&lt;852.0,134.0&gt;--&lt;919.0,68.0&gt;&gt; = 7.699315137147302

* u856B (U+856B): L&lt;&lt;261.0,562.0&gt;--&lt;300.0,571.0&gt;&gt;/L&lt;&lt;300.0,571.0&gt;--&lt;95.0,571.0&gt;&gt; = 12.994616791916512

* u856B (U+856B): L&lt;&lt;383.0,496.0&gt;--&lt;370.0,493.0&gt;&gt;/L&lt;&lt;370.0,493.0&gt;--&lt;624.0,493.0&gt;&gt; = 12.994616791916512

* u85A9 (U+85A9): L&lt;&lt;537.0,383.0&gt;--&lt;817.0,383.0&gt;&gt;/L&lt;&lt;817.0,383.0&gt;--&lt;651.0,424.0&gt;&gt; = 13.873702685485217

* u85D0 (U+85D0): L&lt;&lt;246.0,330.0&gt;--&lt;323.0,371.0&gt;&gt;/L&lt;&lt;323.0,371.0&gt;--&lt;286.0,360.0&gt;&gt; = 11.476780515827171

* u85D0 (U+85D0): L&lt;&lt;85.0,245.0&gt;--&lt;225.0,319.0&gt;&gt;/L&lt;&lt;225.0,319.0&gt;--&lt;167.0,302.0&gt;&gt; = 11.523607805523815

* u85ED (U+85ED): L&lt;&lt;90.0,0.0&gt;--&lt;300.0,63.0&gt;&gt;/L&lt;&lt;300.0,63.0&gt;--&lt;92.0,45.0&gt;&gt; = 11.753277686889454

* u8629 (U+8629): L&lt;&lt;199.0,578.0&gt;--&lt;189.0,549.0&gt;&gt;/L&lt;&lt;189.0,549.0&gt;--&lt;198.0,570.0&gt;&gt; = 4.172984476079407

* u8629 (U+8629): L&lt;&lt;753.0,645.0&gt;--&lt;695.0,645.0&gt;&gt;/L&lt;&lt;695.0,645.0&gt;--&lt;701.0,644.0&gt;&gt; = 9.462322208025613

* u8653 (U+8653): L&lt;&lt;426.0,216.0&gt;--&lt;427.0,211.0&gt;&gt;/L&lt;&lt;427.0,211.0&gt;--&lt;440.0,592.0&gt;&gt; = 13.264148431379855

* u868B (U+868B): L&lt;&lt;582.0,600.0&gt;--&lt;582.0,256.0&gt;&gt;/L&lt;&lt;582.0,256.0&gt;--&lt;650.0,600.0&gt;&gt; = 11.181754210196681

* u8725 (U+8725): L&lt;&lt;537.0,-58.0&gt;--&lt;537.0,296.0&gt;&gt;/L&lt;&lt;537.0,296.0&gt;--&lt;491.0,112.0&gt;&gt; = 14.036243467926484

* u8758 (U+8758): L&lt;&lt;690.0,365.0&gt;--&lt;673.0,365.0&gt;&gt;/L&lt;&lt;673.0,365.0&gt;--&lt;751.0,349.0&gt;&gt; = 11.592175410291073

* u8772 (U+8772): L&lt;&lt;475.0,271.0&gt;--&lt;475.0,263.0&gt;&gt;/L&lt;&lt;475.0,263.0&gt;--&lt;477.0,271.0&gt;&gt; = 14.036243467926484

* u87B3 (U+87B3): L&lt;&lt;861.0,518.0&gt;--&lt;861.0,482.0&gt;&gt;/L&lt;&lt;861.0,482.0&gt;--&lt;866.0,580.0&gt;&gt; = 2.9207215210003468

* u87BB (U+87BB): L&lt;&lt;821.0,263.0&gt;--&lt;641.0,263.0&gt;&gt;/L&lt;&lt;641.0,263.0&gt;--&lt;665.0,258.0&gt;&gt; = 11.768288932020628

* u87BD (U+87BD): L&lt;&lt;221.0,671.0&gt;--&lt;223.0,673.0&gt;&gt;/L&lt;&lt;223.0,673.0&gt;--&lt;117.0,605.0&gt;&gt; = 12.319445256636591

* u87C4 (U+87C4): L&lt;&lt;447.0,292.0&gt;--&lt;511.0,292.0&gt;&gt;/L&lt;&lt;511.0,292.0&gt;--&lt;486.0,295.0&gt;&gt; = 6.842773412630916

* u87CE (U+87CE): L&lt;&lt;799.0,332.0&gt;--&lt;848.0,63.0&gt;&gt;/L&lt;&lt;848.0,63.0&gt;--&lt;848.0,402.0&gt;&gt; = 10.3235889540357

* u87EA (U+87EA): L&lt;&lt;811.0,315.0&gt;--&lt;831.0,319.0&gt;&gt;/L&lt;&lt;831.0,319.0&gt;--&lt;823.0,319.0&gt;&gt; = 11.309932474020195

* u8806 (U+8806): L&lt;&lt;617.0,378.0&gt;--&lt;680.0,384.0&gt;&gt;/L&lt;&lt;680.0,384.0&gt;--&lt;550.0,384.0&gt;&gt; = 5.4403320310054815

* u880A (U+880A): L&lt;&lt;515.0,486.0&gt;--&lt;515.0,517.0&gt;&gt;/L&lt;&lt;515.0,517.0&gt;--&lt;488.0,-69.0&gt;&gt; = 2.638042206951803

* u880D (U+880D): L&lt;&lt;465.0,253.0&gt;--&lt;465.0,159.0&gt;&gt;/L&lt;&lt;465.0,159.0&gt;--&lt;498.0,315.0&gt;&gt; = 11.944177188446329

* u8842 (U+8842): L&lt;&lt;175.0,604.0&gt;--&lt;175.0,598.0&gt;&gt;/L&lt;&lt;175.0,598.0&gt;--&lt;221.0,812.0&gt;&gt; = 12.131321066632513

* u8843 (U+8843): L&lt;&lt;172.0,604.0&gt;--&lt;172.0,598.0&gt;&gt;/L&lt;&lt;172.0,598.0&gt;--&lt;216.0,812.0&gt;&gt; = 11.618524352794632

* u884A (U+884A): L&lt;&lt;163.0,604.0&gt;--&lt;163.0,598.0&gt;&gt;/L&lt;&lt;163.0,598.0&gt;--&lt;204.0,812.0&gt;&gt; = 10.845800398162659

* u8872 (U+8872): L&lt;&lt;516.0,600.0&gt;--&lt;516.0,248.0&gt;&gt;/L&lt;&lt;516.0,248.0&gt;--&lt;600.0,600.0&gt;&gt; = 13.421835067886196

* u888D (U+888D): L&lt;&lt;499.0,-24.0&gt;--&lt;499.0,434.0&gt;&gt;/L&lt;&lt;499.0,434.0&gt;--&lt;494.0,413.0&gt;&gt; = 13.392497753751098

* u88F2 (U+88F2): L&lt;&lt;575.0,492.0&gt;--&lt;642.0,103.0&gt;&gt;/L&lt;&lt;642.0,103.0&gt;--&lt;642.0,571.0&gt;&gt; = 9.772542056093283

* u88F2 (U+88F2): L&lt;&lt;784.0,492.0&gt;--&lt;852.0,97.0&gt;&gt;/L&lt;&lt;852.0,97.0&gt;--&lt;852.0,571.0&gt;&gt; = 9.76783413355948

* u8907 (U+8907): L&lt;&lt;489.0,285.0&gt;--&lt;489.0,439.0&gt;&gt;/L&lt;&lt;489.0,439.0&gt;--&lt;488.0,435.0&gt;&gt; = 14.036243467926484

* u8913 (U+8913): L&lt;&lt;701.0,-58.0&gt;--&lt;701.0,277.0&gt;&gt;/L&lt;&lt;701.0,277.0&gt;--&lt;633.0,-26.0&gt;&gt; = 12.648882516625008

* u8913 (U+8913): L&lt;&lt;852.0,-24.0&gt;--&lt;797.0,278.0&gt;&gt;/L&lt;&lt;797.0,278.0&gt;--&lt;797.0,-58.0&gt;&gt; = 10.321541042743755

* u8938 (U+8938): L&lt;&lt;811.0,263.0&gt;--&lt;619.0,263.0&gt;&gt;/L&lt;&lt;619.0,263.0&gt;--&lt;645.0,257.0&gt;&gt; = 12.994616791916512

* u893D (U+893D): L&lt;&lt;552.0,110.0&gt;--&lt;850.0,186.0&gt;&gt;/L&lt;&lt;850.0,186.0&gt;--&lt;484.0,186.0&gt;&gt; = 14.307357120410265

* u895C (U+895C): L&lt;&lt;504.0,346.0&gt;--&lt;504.0,392.0&gt;&gt;/L&lt;&lt;504.0,392.0&gt;--&lt;481.0,-67.0&gt;&gt; = 2.8686309980652394

* u896B (U+896B): L&lt;&lt;576.0,488.0&gt;--&lt;576.0,268.0&gt;&gt;/B&lt;&lt;576.0,268.0&gt;-&lt;601.0,380.0&gt;-&lt;601.0,579.0&gt;&gt; = 12.58296249407691

* u8972 (U+8972): L&lt;&lt;552.0,110.0&gt;--&lt;850.0,186.0&gt;&gt;/L&lt;&lt;850.0,186.0&gt;--&lt;484.0,186.0&gt;&gt; = 14.307357120410265

* u89A1 (U+89A1): L&lt;&lt;189.0,447.0&gt;--&lt;249.0,211.0&gt;&gt;/L&lt;&lt;249.0,211.0&gt;--&lt;249.0,736.0&gt;&gt; = 14.264512298079907

* u89A1 (U+89A1): L&lt;&lt;331.0,736.0&gt;--&lt;331.0,253.0&gt;&gt;/B&lt;&lt;331.0,253.0&gt;-&lt;357.0,387.0&gt;-&lt;367.0,467.0&gt;&gt; = 10.980650010173553

* u89CB (U+89CB): L&lt;&lt;189.0,447.0&gt;--&lt;249.0,211.0&gt;&gt;/L&lt;&lt;249.0,211.0&gt;--&lt;249.0,736.0&gt;&gt; = 14.264512298079907

* u89CB (U+89CB): L&lt;&lt;331.0,736.0&gt;--&lt;331.0,253.0&gt;&gt;/B&lt;&lt;331.0,253.0&gt;-&lt;356.0,381.0&gt;-&lt;365.0,452.0&gt;&gt; = 11.05145702666541

* u89DE (U+89DE): L&lt;&lt;455.0,558.0&gt;--&lt;455.0,493.0&gt;&gt;/L&lt;&lt;455.0,493.0&gt;--&lt;527.0,806.0&gt;&gt; = 12.954503067189549

* u89F4 (U+89F4): L&lt;&lt;448.0,558.0&gt;--&lt;448.0,493.0&gt;&gt;/L&lt;&lt;448.0,493.0&gt;--&lt;520.0,806.0&gt;&gt; = 12.954503067189549

* u89F4 (U+89F4): L&lt;&lt;535.0,334.0&gt;--&lt;535.0,521.0&gt;&gt;/L&lt;&lt;535.0,521.0&gt;--&lt;521.0,460.0&gt;&gt; = 12.92599912470594

* u8B07 (U+8B07): L&lt;&lt;668.0,632.0&gt;--&lt;801.0,632.0&gt;&gt;/L&lt;&lt;801.0,632.0&gt;--&lt;784.0,634.0&gt;&gt; = 6.709836807756896

* u8B2B (U+8B2B): L&lt;&lt;901.0,623.0&gt;--&lt;814.0,623.0&gt;&gt;/L&lt;&lt;814.0,623.0&gt;--&lt;833.0,621.0&gt;&gt; = 6.009005957494474

* u8B53 (U+8B53): L&lt;&lt;772.0,305.0&gt;--&lt;827.0,319.0&gt;&gt;/L&lt;&lt;827.0,319.0&gt;--&lt;788.0,319.0&gt;&gt; = 14.281095735970814

* u8B8E (U+8B8E): L&lt;&lt;637.0,484.0&gt;--&lt;637.0,476.0&gt;&gt;/L&lt;&lt;637.0,476.0&gt;--&lt;707.0,817.0&gt;&gt; = 11.60044379604984

* u8B9E (U+8B9E): L&lt;&lt;849.0,-54.0&gt;--&lt;810.0,241.0&gt;&gt;/B&lt;&lt;810.0,241.0&gt;-&lt;803.0,156.0&gt;-&lt;792.5,87.5&gt;&gt; = 12.238876074915696

* u8C21 (U+8C21): L&lt;&lt;680.0,460.0&gt;--&lt;605.0,460.0&gt;&gt;/L&lt;&lt;605.0,460.0&gt;--&lt;609.0,459.0&gt;&gt; = 14.036243467926484

* u8C2A (U+8C2A): L&lt;&lt;936.0,623.0&gt;--&lt;820.0,623.0&gt;&gt;/L&lt;&lt;820.0,623.0&gt;--&lt;837.0,621.0&gt;&gt; = 6.709836807756896

* u8C48 (U+8C48): L&lt;&lt;402.0,42.0&gt;--&lt;325.0,24.0&gt;&gt;/L&lt;&lt;325.0,24.0&gt;--&lt;610.0,24.0&gt;&gt; = 13.157542740014783

* u8C4C (U+8C4C): L&lt;&lt;538.0,582.0&gt;--&lt;533.0,582.0&gt;&gt;/L&lt;&lt;533.0,582.0&gt;--&lt;565.0,577.0&gt;&gt; = 8.880659150520234

* u8C54 (U+8C54): L&lt;&lt;272.0,34.0&gt;--&lt;204.0,24.0&gt;&gt;/L&lt;&lt;204.0,24.0&gt;--&lt;314.0,24.0&gt;&gt; = 8.36588612403259

* u8C85 (U+8C85): L&lt;&lt;845.0,57.0&gt;--&lt;776.0,338.0&gt;&gt;/L&lt;&lt;776.0,338.0&gt;--&lt;776.0,-43.0&gt;&gt; = 13.796111682338214

* u8CC4 (U+8CC4): L&lt;&lt;560.0,-52.0&gt;--&lt;560.0,378.0&gt;&gt;/L&lt;&lt;560.0,378.0&gt;--&lt;504.0,56.0&gt;&gt; = 9.865806943084365

* u8CD1 (U+8CD1): L&lt;&lt;532.0,358.0&gt;--&lt;532.0,396.0&gt;&gt;/L&lt;&lt;532.0,396.0&gt;--&lt;521.0,-50.0&gt;&gt; = 1.4128381782191464

* u8CD3 (U+8CD3): L&lt;&lt;794.0,495.0&gt;--&lt;421.0,424.0&gt;&gt;/L&lt;&lt;421.0,424.0&gt;--&lt;840.0,424.0&gt;&gt; = 10.777239129208125

* u8D13 (U+8D13): L&lt;&lt;729.0,57.0&gt;--&lt;729.0,24.0&gt;&gt;/L&lt;&lt;729.0,24.0&gt;--&lt;772.0,219.0&gt;&gt; = 12.435441502527647

* u8D3F (U+8D3F): L&lt;&lt;553.0,-52.0&gt;--&lt;553.0,378.0&gt;&gt;/L&lt;&lt;553.0,378.0&gt;--&lt;497.0,56.0&gt;&gt; = 9.865806943084365

* u8D48 (U+8D48): L&lt;&lt;525.0,358.0&gt;--&lt;525.0,396.0&gt;&gt;/L&lt;&lt;525.0,396.0&gt;--&lt;514.0,-50.0&gt;&gt; = 1.4128381782191464

* u8D49 (U+8D49): L&lt;&lt;346.0,536.0&gt;--&lt;262.0,526.0&gt;&gt;/L&lt;&lt;262.0,526.0&gt;--&lt;462.0,526.0&gt;&gt; = 6.788974574438767

* u8D49 (U+8D49): L&lt;&lt;558.0,526.0&gt;--&lt;736.0,526.0&gt;&gt;/L&lt;&lt;736.0,526.0&gt;--&lt;664.0,537.0&gt;&gt; = 8.686354581236653

* u8D6B (U+8D6B): L&lt;&lt;706.0,407.0&gt;--&lt;690.0,-29.0&gt;&gt;/L&lt;&lt;690.0,-29.0&gt;--&lt;701.0,9.0&gt;&gt; = 14.04268445261215

* u8E62 (U+8E62): L&lt;&lt;931.0,623.0&gt;--&lt;835.0,623.0&gt;&gt;/L&lt;&lt;835.0,623.0&gt;--&lt;851.0,621.0&gt;&gt; = 7.125016348901757

* u8E63 (U+8E63): L&lt;&lt;804.0,332.0&gt;--&lt;853.0,63.0&gt;&gt;/L&lt;&lt;853.0,63.0&gt;--&lt;853.0,402.0&gt;&gt; = 10.3235889540357

* u8E74 (U+8E74): L&lt;&lt;772.0,-14.0&gt;--&lt;772.0,316.0&gt;&gt;/B&lt;&lt;772.0,316.0&gt;-&lt;760.0,191.0&gt;-&lt;738.5,110.5&gt;&gt; = 5.48359044446442

* u8E85 (U+8E85): L&lt;&lt;545.0,144.0&gt;--&lt;545.0,331.0&gt;&gt;/L&lt;&lt;545.0,331.0&gt;--&lt;509.0,185.0&gt;&gt; = 13.851419013805002

* u8E89 (U+8E89): L&lt;&lt;617.0,378.0&gt;--&lt;680.0,384.0&gt;&gt;/L&lt;&lt;680.0,384.0&gt;--&lt;550.0,384.0&gt;&gt; = 5.4403320310054815

* u8E9E (U+8E9E): B&lt;&lt;516.0,830.0&gt;-&lt;516.0,727.0&gt;-&lt;511.0,666.0&gt;&gt;/L&lt;&lt;511.0,666.0&gt;--&lt;544.0,771.0&gt;&gt; = 12.761288583779463

* u8EAB (U+8EAB): L&lt;&lt;98.0,10.0&gt;--&lt;555.0,167.0&gt;&gt;/L&lt;&lt;555.0,167.0&gt;--&lt;77.0,124.0&gt;&gt; = 13.81950896623153

* u8EC6 (U+8EC6): L&lt;&lt;608.0,115.0&gt;--&lt;659.0,123.0&gt;&gt;/L&lt;&lt;659.0,123.0&gt;--&lt;608.0,123.0&gt;&gt; = 8.914926957147863

* u8EC6 (U+8EC6): L&lt;&lt;687.0,29.0&gt;--&lt;654.0,24.0&gt;&gt;/L&lt;&lt;654.0,24.0&gt;--&lt;729.0,24.0&gt;&gt; = 8.615648184164108

* u8EC6 (U+8EC6): L&lt;&lt;800.0,123.0&gt;--&lt;777.0,123.0&gt;&gt;/L&lt;&lt;777.0,123.0&gt;--&lt;800.0,118.0&gt;&gt; = 12.2647737278924

* u8EC6 (U+8EC6): L&lt;&lt;896.0,108.0&gt;--&lt;852.0,108.0&gt;&gt;/L&lt;&lt;852.0,108.0&gt;--&lt;857.0,107.0&gt;&gt; = 11.309932474020195

* u8F1B (U+8F1B): L&lt;&lt;572.0,455.0&gt;--&lt;632.0,89.0&gt;&gt;/L&lt;&lt;632.0,89.0&gt;--&lt;632.0,527.0&gt;&gt; = 9.30994017498605

* u8F1B (U+8F1B): L&lt;&lt;700.0,527.0&gt;--&lt;700.0,100.0&gt;&gt;/L&lt;&lt;700.0,100.0&gt;--&lt;733.0,299.0&gt;&gt; = 9.415626391540325

* u8F39 (U+8F39): L&lt;&lt;546.0,285.0&gt;--&lt;546.0,496.0&gt;&gt;/L&lt;&lt;546.0,496.0&gt;--&lt;545.0,492.0&gt;&gt; = 14.036243467926484

* u8F45 (U+8F45): L&lt;&lt;787.0,100.0&gt;--&lt;743.0,118.0&gt;&gt;/L&lt;&lt;743.0,118.0&gt;--&lt;938.0,-9.0&gt;&gt; = 10.826452405175717

* u8F63 (U+8F63): L&lt;&lt;689.0,402.0&gt;--&lt;714.0,448.0&gt;&gt;/L&lt;&lt;714.0,448.0&gt;--&lt;707.0,440.0&gt;&gt; = 12.662806559397625

* u8F7D (U+8F7D): L&lt;&lt;620.0,490.0&gt;--&lt;349.0,490.0&gt;&gt;/L&lt;&lt;349.0,490.0&gt;--&lt;370.0,486.0&gt;&gt; = 10.784297867562596

* u8F9F (U+8F9F): L&lt;&lt;184.0,-48.0&gt;--&lt;184.0,213.0&gt;&gt;/L&lt;&lt;184.0,213.0&gt;--&lt;167.0,52.0&gt;&gt; = 6.027530295521282

* u902D (U+902D): L&lt;&lt;815.0,593.0&gt;--&lt;815.0,541.0&gt;&gt;/L&lt;&lt;815.0,541.0&gt;--&lt;830.0,652.0&gt;&gt; = 7.696051722016556

* u904A (U+904A): L&lt;&lt;695.0,503.0&gt;--&lt;695.0,518.0&gt;&gt;/L&lt;&lt;695.0,518.0&gt;--&lt;690.0,495.0&gt;&gt; = 12.2647737278924

* u905E (U+905E): L&lt;&lt;805.0,499.0&gt;--&lt;814.0,451.0&gt;&gt;/L&lt;&lt;814.0,451.0&gt;--&lt;814.0,469.0&gt;&gt; = 10.61965527615514

* u9069 (U+9069): L&lt;&lt;928.0,650.0&gt;--&lt;811.0,650.0&gt;&gt;/L&lt;&lt;811.0,650.0&gt;--&lt;818.0,649.0&gt;&gt; = 8.13010235415596

* u90F4 (U+90F4): L&lt;&lt;194.0,-51.0&gt;--&lt;194.0,240.0&gt;&gt;/L&lt;&lt;194.0,240.0&gt;--&lt;141.0,21.0&gt;&gt; = 13.604528864632057

* u90F4 (U+90F4): L&lt;&lt;448.0,-51.0&gt;--&lt;448.0,225.0&gt;&gt;/L&lt;&lt;448.0,225.0&gt;--&lt;392.0,5.0&gt;&gt; = 14.281095735970814

* u90FE (U+90FE): L&lt;&lt;343.0,377.0&gt;--&lt;322.0,377.0&gt;&gt;/L&lt;&lt;322.0,377.0&gt;--&lt;405.0,361.0&gt;&gt; = 10.911128384283376

* u9117 (U+9117): L&lt;&lt;383.0,224.0&gt;--&lt;383.0,-1.0&gt;&gt;/L&lt;&lt;383.0,-1.0&gt;--&lt;386.0,17.0&gt;&gt; = 9.462322208025613

* u9127 (U+9127): L&lt;&lt;110.0,1.0&gt;--&lt;284.0,38.0&gt;&gt;/L&lt;&lt;284.0,38.0&gt;--&lt;200.0,25.0&gt;&gt; = 3.207364847730034

* u9146 (U+9146): L&lt;&lt;296.0,33.0&gt;--&lt;223.0,24.0&gt;&gt;/L&lt;&lt;223.0,24.0&gt;--&lt;359.0,24.0&gt;&gt; = 7.02839623894957

* u9182 (U+9182): L&lt;&lt;543.0,-71.0&gt;--&lt;543.0,323.0&gt;&gt;/L&lt;&lt;543.0,323.0&gt;--&lt;498.0,12.0&gt;&gt; = 8.233244960135043

* u9182 (U+9182): L&lt;&lt;748.0,-71.0&gt;--&lt;748.0,276.0&gt;&gt;/L&lt;&lt;748.0,276.0&gt;--&lt;702.0,-5.0&gt;&gt; = 9.29691914697019

* u9182 (U+9182): L&lt;&lt;878.0,-5.0&gt;--&lt;823.0,278.0&gt;&gt;/L&lt;&lt;823.0,278.0&gt;--&lt;823.0,-71.0&gt;&gt; = 10.998121786267378

* u91B4 (U+91B4): L&lt;&lt;598.0,115.0&gt;--&lt;650.0,123.0&gt;&gt;/L&lt;&lt;650.0,123.0&gt;--&lt;598.0,123.0&gt;&gt; = 8.746162262555211

* u91B4 (U+91B4): L&lt;&lt;679.0,29.0&gt;--&lt;646.0,24.0&gt;&gt;/L&lt;&lt;646.0,24.0&gt;--&lt;725.0,24.0&gt;&gt; = 8.615648184164108

* u91B4 (U+91B4): L&lt;&lt;798.0,123.0&gt;--&lt;774.0,123.0&gt;&gt;/L&lt;&lt;774.0,123.0&gt;--&lt;798.0,118.0&gt;&gt; = 11.768288932020628

* u91B4 (U+91B4): L&lt;&lt;894.0,108.0&gt;--&lt;849.0,108.0&gt;&gt;/L&lt;&lt;849.0,108.0&gt;--&lt;854.0,107.0&gt;&gt; = 11.309932474020195

* u91E9 (U+91E9): L&lt;&lt;661.0,516.0&gt;--&lt;726.0,182.0&gt;&gt;/L&lt;&lt;726.0,182.0&gt;--&lt;726.0,736.0&gt;&gt; = 11.012723603415871

* u91E9 (U+91E9): L&lt;&lt;662.0,162.0&gt;--&lt;599.0,486.0&gt;&gt;/B&lt;&lt;599.0,486.0&gt;-&lt;593.0,245.0&gt;-&lt;574.0,123.5&gt;&gt; = 12.429697187343987

* u923D (U+923D): L&lt;&lt;774.0,388.0&gt;--&lt;774.0,50.0&gt;&gt;/L&lt;&lt;774.0,50.0&gt;--&lt;776.0,59.0&gt;&gt; = 12.528807709151522

* u924B (U+924B): L&lt;&lt;556.0,-24.0&gt;--&lt;556.0,372.0&gt;&gt;/L&lt;&lt;556.0,372.0&gt;--&lt;554.0,357.0&gt;&gt; = 7.594643368591447

* u9276 (U+9276): L&lt;&lt;430.0,509.0&gt;--&lt;356.0,492.0&gt;&gt;/L&lt;&lt;356.0,492.0&gt;--&lt;366.0,492.0&gt;&gt; = 12.938056317186467

* u929C (U+929C): L&lt;&lt;283.0,431.0&gt;--&lt;294.0,453.0&gt;&gt;/L&lt;&lt;294.0,453.0&gt;--&lt;279.0,432.0&gt;&gt; = 8.972626614896358

* u92AA (U+92AA): L&lt;&lt;572.0,-52.0&gt;--&lt;572.0,209.0&gt;&gt;/L&lt;&lt;572.0,209.0&gt;--&lt;533.0,56.0&gt;&gt; = 14.300277449185575

* u92BC (U+92BC): L&lt;&lt;721.0,834.0&gt;--&lt;721.0,286.0&gt;&gt;/L&lt;&lt;721.0,286.0&gt;--&lt;817.0,822.0&gt;&gt; = 10.154266580200266

* u92FA (U+92FA): L&lt;&lt;468.0,324.0&gt;--&lt;468.0,290.0&gt;&gt;/L&lt;&lt;468.0,290.0&gt;--&lt;532.0,582.0&gt;&gt; = 12.36249241571432

* u92FA (U+92FA): L&lt;&lt;582.0,582.0&gt;--&lt;573.0,582.0&gt;&gt;/L&lt;&lt;573.0,582.0&gt;--&lt;613.0,577.0&gt;&gt; = 7.125016348901757

* u92FA (U+92FA): L&lt;&lt;717.0,-21.0&gt;--&lt;717.0,491.0&gt;&gt;/L&lt;&lt;717.0,491.0&gt;--&lt;605.0,-46.0&gt;&gt; = 11.781070560194918

* u9312 (U+9312): L&lt;&lt;415.0,509.0&gt;--&lt;344.0,492.0&gt;&gt;/L&lt;&lt;344.0,492.0&gt;--&lt;354.0,492.0&gt;&gt; = 13.465208094811722

* u9376 (U+9376): L&lt;&lt;481.0,520.0&gt;--&lt;421.0,506.0&gt;&gt;/L&lt;&lt;421.0,506.0&gt;--&lt;455.0,506.0&gt;&gt; = 13.134022306396327

* u938F (U+938F): L&lt;&lt;658.0,697.0&gt;--&lt;701.0,704.0&gt;&gt;/L&lt;&lt;701.0,704.0&gt;--&lt;556.0,704.0&gt;&gt; = 9.24611274556323

* u9396 (U+9396): L&lt;&lt;494.0,520.0&gt;--&lt;434.0,506.0&gt;&gt;/L&lt;&lt;434.0,506.0&gt;--&lt;468.0,506.0&gt;&gt; = 13.134022306396327

* u93B3 (U+93B3): L&lt;&lt;464.0,510.0&gt;--&lt;407.0,496.0&gt;&gt;/L&lt;&lt;407.0,496.0&gt;--&lt;439.0,496.0&gt;&gt; = 13.799485396019362

* u93CB (U+93CB): L&lt;&lt;799.0,332.0&gt;--&lt;848.0,63.0&gt;&gt;/L&lt;&lt;848.0,63.0&gt;--&lt;848.0,402.0&gt;&gt; = 10.3235889540357

* u93D1 (U+93D1): L&lt;&lt;936.0,623.0&gt;--&lt;849.0,623.0&gt;&gt;/L&lt;&lt;849.0,623.0&gt;--&lt;865.0,621.0&gt;&gt; = 7.125016348901757

* u93DE (U+93DE): L&lt;&lt;476.0,44.0&gt;--&lt;482.0,14.0&gt;&gt;/L&lt;&lt;482.0,14.0&gt;--&lt;492.0,280.0&gt;&gt; = 13.46289526312066

* u93E4 (U+93E4): L&lt;&lt;827.0,263.0&gt;--&lt;665.0,263.0&gt;&gt;/L&lt;&lt;665.0,263.0&gt;--&lt;690.0,258.0&gt;&gt; = 11.309932474020195

* u93FB (U+93FB): L&lt;&lt;400.0,237.0&gt;--&lt;387.0,144.0&gt;&gt;/L&lt;&lt;387.0,144.0&gt;--&lt;491.0,413.0&gt;&gt; = 13.17982897764939

* u9404 (U+9404): L&lt;&lt;473.0,510.0&gt;--&lt;469.0,509.0&gt;&gt;/L&lt;&lt;469.0,509.0&gt;--&lt;934.0,509.0&gt;&gt; = 14.036243467926484

* u9413 (U+9413): L&lt;&lt;424.0,509.0&gt;--&lt;351.0,492.0&gt;&gt;/L&lt;&lt;351.0,492.0&gt;--&lt;361.0,492.0&gt;&gt; = 13.109208198154267

* u9429 (U+9429): L&lt;&lt;401.0,504.0&gt;--&lt;349.0,492.0&gt;&gt;/L&lt;&lt;349.0,492.0&gt;--&lt;359.0,492.0&gt;&gt; = 12.994616791916512

* u9431 (U+9431): L&lt;&lt;807.0,199.0&gt;--&lt;795.0,199.0&gt;&gt;/L&lt;&lt;795.0,199.0&gt;--&lt;881.0,179.0&gt;&gt; = 13.091893064346833

* u9432 (U+9432): L&lt;&lt;545.0,144.0&gt;--&lt;545.0,331.0&gt;&gt;/L&lt;&lt;545.0,331.0&gt;--&lt;509.0,185.0&gt;&gt; = 13.851419013805002

* u9440 (U+9440): L&lt;&lt;599.0,122.0&gt;--&lt;571.0,77.0&gt;&gt;/L&lt;&lt;571.0,77.0&gt;--&lt;593.0,109.0&gt;&gt; = 2.6177311858225365

* u9441 (U+9441): L&lt;&lt;645.0,144.0&gt;--&lt;632.0,118.0&gt;&gt;/L&lt;&lt;632.0,118.0&gt;--&lt;637.0,124.0&gt;&gt; = 13.24051991518721

* u9454 (U+9454): L&lt;&lt;721.0,579.0&gt;--&lt;874.0,579.0&gt;&gt;/L&lt;&lt;874.0,579.0&gt;--&lt;832.0,582.0&gt;&gt; = 4.085616779974888

* u946B (U+946B): L&lt;&lt;625.0,20.0&gt;--&lt;564.0,13.0&gt;&gt;/L&lt;&lt;564.0,13.0&gt;--&lt;660.0,13.0&gt;&gt; = 6.546290783293998

* u9477 (U+9477): L&lt;&lt;346.0,11.0&gt;--&lt;360.0,16.0&gt;&gt;/L&lt;&lt;360.0,16.0&gt;--&lt;106.0,-24.0&gt;&gt; = 10.70436597384442

* u9492 (U+9492): L&lt;&lt;661.0,516.0&gt;--&lt;726.0,182.0&gt;&gt;/L&lt;&lt;726.0,182.0&gt;--&lt;726.0,736.0&gt;&gt; = 11.012723603415871

* u9492 (U+9492): L&lt;&lt;662.0,162.0&gt;--&lt;599.0,486.0&gt;&gt;/B&lt;&lt;599.0,486.0&gt;-&lt;593.0,245.0&gt;-&lt;574.0,123.5&gt;&gt; = 12.429697187343987

* u9496 (U+9496): L&lt;&lt;145.0,499.0&gt;--&lt;152.0,499.0&gt;&gt;/L&lt;&lt;152.0,499.0&gt;--&lt;64.0,507.0&gt;&gt; = 5.1944289077348

* u94B8 (U+94B8): L&lt;&lt;774.0,388.0&gt;--&lt;774.0,50.0&gt;&gt;/L&lt;&lt;774.0,50.0&gt;--&lt;776.0,59.0&gt;&gt; = 12.528807709151522

* u94CB (U+94CB): L&lt;&lt;156.0,479.0&gt;--&lt;161.0,479.0&gt;&gt;/L&lt;&lt;161.0,479.0&gt;--&lt;78.0,487.0&gt;&gt; = 5.505477857978337

* u94D5 (U+94D5): L&lt;&lt;581.0,-52.0&gt;--&lt;581.0,378.0&gt;&gt;/L&lt;&lt;581.0,378.0&gt;--&lt;528.0,56.0&gt;&gt; = 9.346864874101241

* u94E4 (U+94E4): L&lt;&lt;137.0,479.0&gt;--&lt;138.0,479.0&gt;&gt;/L&lt;&lt;138.0,479.0&gt;--&lt;57.0,487.0&gt;&gt; = 5.640549432156827

* u9507 (U+9507): L&lt;&lt;150.0,479.0&gt;--&lt;155.0,479.0&gt;&gt;/L&lt;&lt;155.0,479.0&gt;--&lt;75.0,487.0&gt;&gt; = 5.710593137499633

* u9509 (U+9509): L&lt;&lt;374.0,297.0&gt;--&lt;374.0,294.0&gt;&gt;/L&lt;&lt;374.0,294.0&gt;--&lt;478.0,821.0&gt;&gt; = 11.163503272340904

* u950E (U+950E): L&lt;&lt;147.0,479.0&gt;--&lt;151.0,479.0&gt;&gt;/L&lt;&lt;151.0,479.0&gt;--&lt;75.0,487.0&gt;&gt; = 6.009005957494535

* u9514 (U+9514): L&lt;&lt;152.0,479.0&gt;--&lt;157.0,479.0&gt;&gt;/L&lt;&lt;157.0,479.0&gt;--&lt;75.0,487.0&gt;&gt; = 5.572197803963754

* u9533 (U+9533): L&lt;&lt;141.0,479.0&gt;--&lt;152.0,479.0&gt;&gt;/L&lt;&lt;152.0,479.0&gt;--&lt;66.0,487.0&gt;&gt; = 5.3145456699447315

* u9548 (U+9548): L&lt;&lt;66.0,487.0&gt;--&lt;158.0,479.0&gt;&gt;/L&lt;&lt;158.0,479.0&gt;--&lt;147.0,479.0&gt;&gt; = 4.969740728110289

* u9549 (U+9549): L&lt;&lt;154.0,479.0&gt;--&lt;158.0,479.0&gt;&gt;/L&lt;&lt;158.0,479.0&gt;--&lt;75.0,487.0&gt;&gt; = 5.505477857978337

* u954D (U+954D): L&lt;&lt;154.0,479.0&gt;--&lt;158.0,479.0&gt;&gt;/L&lt;&lt;158.0,479.0&gt;--&lt;75.0,487.0&gt;&gt; = 5.505477857978337

* u954E (U+954E): L&lt;&lt;154.0,479.0&gt;--&lt;158.0,479.0&gt;&gt;/L&lt;&lt;158.0,479.0&gt;--&lt;75.0,487.0&gt;&gt; = 5.505477857978337

* u9551 (U+9551): L&lt;&lt;529.0,524.0&gt;--&lt;528.0,528.0&gt;&gt;/L&lt;&lt;528.0,528.0&gt;--&lt;528.0,524.0&gt;&gt; = 14.036243467926484

* u955D (U+955D): L&lt;&lt;932.0,623.0&gt;--&lt;832.0,623.0&gt;&gt;/L&lt;&lt;832.0,623.0&gt;--&lt;849.0,621.0&gt;&gt; = 6.709836807756896

* u9567 (U+9567): L&lt;&lt;132.0,479.0&gt;--&lt;146.0,479.0&gt;&gt;/L&lt;&lt;146.0,479.0&gt;--&lt;65.0,487.0&gt;&gt; = 5.640549432156827

* u9568 (U+9568): L&lt;&lt;155.0,479.0&gt;--&lt;159.0,479.0&gt;&gt;/L&lt;&lt;159.0,479.0&gt;--&lt;78.0,487.0&gt;&gt; = 5.640549432156827

* u9570 (U+9570): L&lt;&lt;497.0,486.0&gt;--&lt;497.0,517.0&gt;&gt;/L&lt;&lt;497.0,517.0&gt;--&lt;469.0,-69.0&gt;&gt; = 2.7356016991130856

* u9572 (U+9572): L&lt;&lt;149.0,479.0&gt;--&lt;158.0,479.0&gt;&gt;/L&lt;&lt;158.0,479.0&gt;--&lt;75.0,487.0&gt;&gt; = 5.505477857978337

* u9572 (U+9572): L&lt;&lt;707.0,579.0&gt;--&lt;870.0,579.0&gt;&gt;/L&lt;&lt;870.0,579.0&gt;--&lt;825.0,582.0&gt;&gt; = 3.8140748342903783

* u9573 (U+9573): L&lt;&lt;148.0,479.0&gt;--&lt;158.0,479.0&gt;&gt;/L&lt;&lt;158.0,479.0&gt;--&lt;75.0,487.0&gt;&gt; = 5.505477857978337

* u95A0 (U+95A0): L&lt;&lt;710.0,65.0&gt;--&lt;618.0,54.0&gt;&gt;/L&lt;&lt;618.0,54.0&gt;--&lt;740.0,54.0&gt;&gt; = 6.818214571651848

* u95AC (U+95AC): L&lt;&lt;710.0,168.0&gt;--&lt;688.0,168.0&gt;&gt;/L&lt;&lt;688.0,168.0&gt;--&lt;736.0,157.0&gt;&gt; = 12.907408671265848

* u95BB (U+95BB): L&lt;&lt;721.0,222.0&gt;--&lt;721.0,0.0&gt;&gt;/L&lt;&lt;721.0,0.0&gt;--&lt;727.0,24.0&gt;&gt; = 14.036243467926484

* u95D5 (U+95D5): L&lt;&lt;496.0,271.0&gt;--&lt;496.0,251.0&gt;&gt;/L&lt;&lt;496.0,251.0&gt;--&lt;540.0,454.0&gt;&gt; = 12.229615757557848

* u964B (U+964B): L&lt;&lt;593.0,561.0&gt;--&lt;595.0,268.0&gt;&gt;/L&lt;&lt;595.0,268.0&gt;--&lt;651.0,561.0&gt;&gt; = 11.211328277947995

* u968F (U+968F): L&lt;&lt;664.0,55.0&gt;--&lt;664.0,371.0&gt;&gt;/L&lt;&lt;664.0,371.0&gt;--&lt;639.0,151.0&gt;&gt; = 6.483073692897206

* u9744 (U+9744): L&lt;&lt;79.0,388.0&gt;--&lt;301.0,388.0&gt;&gt;/L&lt;&lt;301.0,388.0&gt;--&lt;123.0,415.0&gt;&gt; = 8.62518317817046

* u9749 (U+9749): L&lt;&lt;821.0,450.0&gt;--&lt;839.0,352.0&gt;&gt;/L&lt;&lt;839.0,352.0&gt;--&lt;845.0,497.0&gt;&gt; = 12.777219376745322

* u974D (U+974D): L&lt;&lt;760.0,89.0&gt;--&lt;798.0,97.0&gt;&gt;/L&lt;&lt;798.0,97.0&gt;--&lt;519.0,97.0&gt;&gt; = 11.888658039627968

* u9779 (U+9779): L&lt;&lt;597.0,600.0&gt;--&lt;597.0,219.0&gt;&gt;/L&lt;&lt;597.0,219.0&gt;--&lt;675.0,600.0&gt;&gt; = 11.569972047901999

* u979C (U+979C): L&lt;&lt;799.0,603.0&gt;--&lt;752.0,634.0&gt;&gt;/L&lt;&lt;752.0,634.0&gt;--&lt;936.0,462.0&gt;&gt; = 9.661587969124048

* u97A6 (U+97A6): L&lt;&lt;428.0,95.0&gt;--&lt;428.0,80.0&gt;&gt;/L&lt;&lt;428.0,80.0&gt;--&lt;508.0,402.0&gt;&gt; = 13.95247776808494

* u97A6 (U+97A6): L&lt;&lt;530.0,-52.0&gt;--&lt;530.0,195.0&gt;&gt;/L&lt;&lt;530.0,195.0&gt;--&lt;494.0,49.0&gt;&gt; = 13.851419013805002

* u97C8 (U+97C8): L&lt;&lt;638.0,357.0&gt;--&lt;696.0,371.0&gt;&gt;/L&lt;&lt;696.0,371.0&gt;--&lt;554.0,371.0&gt;&gt; = 13.570434385161475

* u9862 (U+9862): L&lt;&lt;405.0,332.0&gt;--&lt;452.0,63.0&gt;&gt;/L&lt;&lt;452.0,63.0&gt;--&lt;452.0,402.0&gt;&gt; = 9.910744800154664

* u988D (U+988D): L&lt;&lt;402.0,198.0&gt;--&lt;356.0,227.0&gt;&gt;/L&lt;&lt;356.0,227.0&gt;--&lt;540.0,40.0&gt;&gt; = 13.234540657243226

* u989E (U+989E): L&lt;&lt;693.0,655.0&gt;--&lt;693.0,644.0&gt;&gt;/L&lt;&lt;693.0,644.0&gt;--&lt;715.0,736.0&gt;&gt; = 13.448615051686527

* u98AE (U+98AE): L&lt;&lt;789.0,308.0&gt;--&lt;774.0,308.0&gt;&gt;/L&lt;&lt;774.0,308.0&gt;--&lt;812.0,301.0&gt;&gt; = 10.437475351118158

* u98D1 (U+98D1): L&lt;&lt;769.0,308.0&gt;--&lt;753.0,308.0&gt;&gt;/L&lt;&lt;753.0,308.0&gt;--&lt;794.0,301.0&gt;&gt; = 9.68878656036679

* u98FD (U+98FD): L&lt;&lt;494.0,486.0&gt;--&lt;494.0,379.0&gt;&gt;/L&lt;&lt;494.0,379.0&gt;--&lt;514.0,537.0&gt;&gt; = 7.214262039206713

* u9950 (U+9950): L&lt;&lt;677.0,25.0&gt;--&lt;661.0,24.0&gt;&gt;/L&lt;&lt;661.0,24.0&gt;--&lt;727.0,24.0&gt;&gt; = 3.576334374997269

* u9954 (U+9954): L&lt;&lt;307.0,12.0&gt;--&lt;450.0,22.0&gt;&gt;/L&lt;&lt;450.0,22.0&gt;--&lt;341.0,39.0&gt;&gt; = 12.864809148923896

* u9955 (U+9955): L&lt;&lt;307.0,9.0&gt;--&lt;467.0,21.0&gt;&gt;/L&lt;&lt;467.0,21.0&gt;--&lt;342.0,42.0&gt;&gt; = 13.825789087278434

* u9957 (U+9957): L&lt;&lt;891.0,42.0&gt;--&lt;730.0,34.0&gt;&gt;/L&lt;&lt;730.0,34.0&gt;--&lt;903.0,3.0&gt;&gt; = 13.003711600620223

* u995C (U+995C): L&lt;&lt;898.0,43.0&gt;--&lt;750.0,35.0&gt;&gt;/L&lt;&lt;750.0,35.0&gt;--&lt;909.0,7.0&gt;&gt; = 13.081479633930671

* u9962 (U+9962): L&lt;&lt;708.0,101.0&gt;--&lt;886.0,137.0&gt;&gt;/L&lt;&lt;886.0,137.0&gt;--&lt;663.0,137.0&gt;&gt; = 11.433681265426657

* u99A8 (U+99A8): L&lt;&lt;555.0,169.0&gt;--&lt;721.0,169.0&gt;&gt;/L&lt;&lt;721.0,169.0&gt;--&lt;555.0,211.0&gt;&gt; = 14.198554023863164

* u99A8 (U+99A8): L&lt;&lt;80.0,171.0&gt;--&lt;300.0,225.0&gt;&gt;/L&lt;&lt;300.0,225.0&gt;--&lt;58.0,225.0&gt;&gt; = 13.790866897360976

* u99C9 (U+99C9): L&lt;&lt;330.0,223.0&gt;--&lt;332.0,13.0&gt;&gt;/L&lt;&lt;332.0,13.0&gt;--&lt;332.0,14.0&gt;&gt; = 0.5456575934158381

* u99DF (U+99DF): L&lt;&lt;335.0,215.0&gt;--&lt;337.0,5.0&gt;&gt;/L&lt;&lt;337.0,5.0&gt;--&lt;337.0,6.0&gt;&gt; = 0.5456575934158381

* u99E2 (U+99E2): L&lt;&lt;331.0,219.0&gt;--&lt;333.0,5.0&gt;&gt;/L&lt;&lt;333.0,5.0&gt;--&lt;333.0,6.0&gt;&gt; = 0.5354589855643856

* u99F0 (U+99F0): L&lt;&lt;330.0,223.0&gt;--&lt;332.0,13.0&gt;&gt;/L&lt;&lt;332.0,13.0&gt;--&lt;332.0,14.0&gt;&gt; = 0.5456575934158381

* u99F2 (U+99F2): L&lt;&lt;317.0,215.0&gt;--&lt;319.0,0.0&gt;&gt;/L&lt;&lt;319.0,0.0&gt;--&lt;320.0,6.0&gt;&gt; = 9.995290830679862

* u99F2 (U+99F2): L&lt;&lt;849.0,602.0&gt;--&lt;850.0,580.0&gt;&gt;/L&lt;&lt;850.0,580.0&gt;--&lt;850.0,826.0&gt;&gt; = 2.6025622024998034

* u99FC (U+99FC): L&lt;&lt;330.0,223.0&gt;--&lt;332.0,13.0&gt;&gt;/L&lt;&lt;332.0,13.0&gt;--&lt;332.0,14.0&gt;&gt; = 0.5456575934158381

* u9A1E (U+9A1E): L&lt;&lt;335.0,223.0&gt;--&lt;337.0,13.0&gt;&gt;/L&lt;&lt;337.0,13.0&gt;--&lt;337.0,14.0&gt;&gt; = 0.5456575934158381

* u9A31 (U+9A31): L&lt;&lt;324.0,223.0&gt;--&lt;326.0,13.0&gt;&gt;/L&lt;&lt;326.0,13.0&gt;--&lt;326.0,14.0&gt;&gt; = 0.5456575934158381

* u9A45 (U+9A45): L&lt;&lt;325.0,228.0&gt;--&lt;328.0,8.0&gt;&gt;/L&lt;&lt;328.0,8.0&gt;--&lt;330.0,19.0&gt;&gt; = 11.086104130374654

* u9ACF (U+9ACF): L&lt;&lt;808.0,263.0&gt;--&lt;658.0,263.0&gt;&gt;/L&lt;&lt;658.0,263.0&gt;--&lt;679.0,259.0&gt;&gt; = 10.784297867562596

* u9AD1 (U+9AD1): L&lt;&lt;533.0,137.0&gt;--&lt;533.0,274.0&gt;&gt;/L&lt;&lt;533.0,274.0&gt;--&lt;517.0,199.0&gt;&gt; = 12.042575142884978

* u9AD4 (U+9AD4): L&lt;&lt;577.0,115.0&gt;--&lt;629.0,123.0&gt;&gt;/L&lt;&lt;629.0,123.0&gt;--&lt;577.0,123.0&gt;&gt; = 8.746162262555211

* u9AD4 (U+9AD4): L&lt;&lt;659.0,29.0&gt;--&lt;626.0,24.0&gt;&gt;/L&lt;&lt;626.0,24.0&gt;--&lt;707.0,24.0&gt;&gt; = 8.615648184164108

* u9AD4 (U+9AD4): L&lt;&lt;780.0,123.0&gt;--&lt;757.0,123.0&gt;&gt;/L&lt;&lt;757.0,123.0&gt;--&lt;780.0,118.0&gt;&gt; = 12.2647737278924

* u9AD4 (U+9AD4): L&lt;&lt;876.0,108.0&gt;--&lt;830.0,108.0&gt;&gt;/L&lt;&lt;830.0,108.0&gt;--&lt;835.0,107.0&gt;&gt; = 11.309932474020195

* u9AEB (U+9AEB): L&lt;&lt;160.0,163.0&gt;--&lt;140.0,159.0&gt;&gt;/L&lt;&lt;140.0,159.0&gt;--&lt;229.0,159.0&gt;&gt; = 11.309932474020195

* u9B18 (U+9B18): L&lt;&lt;426.0,49.0&gt;--&lt;642.0,87.0&gt;&gt;/L&lt;&lt;642.0,87.0&gt;--&lt;79.0,87.0&gt;&gt; = 9.97771262015058

* u9B1F (U+9B1F): L&lt;&lt;879.0,60.0&gt;--&lt;663.0,42.0&gt;&gt;/L&lt;&lt;663.0,42.0&gt;--&lt;925.0,-2.0&gt;&gt; = 14.29687448075618

* u9B22 (U+9B22): L&lt;&lt;770.0,271.0&gt;--&lt;479.0,238.0&gt;&gt;/L&lt;&lt;479.0,238.0&gt;--&lt;831.0,238.0&gt;&gt; = 6.469819985173205

* u9B23 (U+9B23): L&lt;&lt;363.0,237.0&gt;--&lt;594.0,237.0&gt;&gt;/L&lt;&lt;594.0,237.0&gt;--&lt;478.0,262.0&gt;&gt; = 12.16220351968183

* u9B23 (U+9B23): L&lt;&lt;478.0,262.0&gt;--&lt;363.0,237.0&gt;&gt;/L&lt;&lt;363.0,237.0&gt;--&lt;594.0,237.0&gt;&gt; = 12.2647737278924

* u9B23 (U+9B23): L&lt;&lt;478.0,298.0&gt;--&lt;602.0,325.0&gt;&gt;/L&lt;&lt;602.0,325.0&gt;--&lt;354.0,325.0&gt;&gt; = 12.283955441107178

* u9B23 (U+9B23): L&lt;&lt;602.0,325.0&gt;--&lt;354.0,325.0&gt;&gt;/L&lt;&lt;354.0,325.0&gt;--&lt;478.0,298.0&gt;&gt; = 12.283955441107178

* u9B23 (U+9B23): L&lt;&lt;716.0,181.0&gt;--&lt;772.0,187.0&gt;&gt;/L&lt;&lt;772.0,187.0&gt;--&lt;739.0,187.0&gt;&gt; = 6.115503566285384

* u9B6F (U+9B6F): L&lt;&lt;170.0,252.0&gt;--&lt;187.0,252.0&gt;&gt;/L&lt;&lt;187.0,252.0&gt;--&lt;97.0,270.0&gt;&gt; = 11.309932474020195

* u9B77 (U+9B77): L&lt;&lt;675.0,-24.0&gt;--&lt;675.0,260.0&gt;&gt;/B&lt;&lt;675.0,260.0&gt;-&lt;652.0,150.0&gt;-&lt;620.5,81.0&gt;&gt; = 11.809882957028252

* u9BAA (U+9BAA): L&lt;&lt;560.0,-52.0&gt;--&lt;560.0,209.0&gt;&gt;/L&lt;&lt;560.0,209.0&gt;--&lt;521.0,56.0&gt;&gt; = 14.300277449185575

* u9BB4 (U+9BB4): L&lt;&lt;832.0,57.0&gt;--&lt;769.0,332.0&gt;&gt;/L&lt;&lt;769.0,332.0&gt;--&lt;769.0,-43.0&gt;&gt; = 12.903284595874329

* u9BFB (U+9BFB): L&lt;&lt;499.0,271.0&gt;--&lt;499.0,263.0&gt;&gt;/L&lt;&lt;499.0,263.0&gt;--&lt;501.0,271.0&gt;&gt; = 14.036243467926484

* u9C0D (U+9C0D): L&lt;&lt;502.0,-52.0&gt;--&lt;502.0,180.0&gt;&gt;/L&lt;&lt;502.0,180.0&gt;--&lt;471.0,47.0&gt;&gt; = 13.120403152977243

* u9C27 (U+9C27): L&lt;&lt;540.0,505.0&gt;--&lt;504.0,438.0&gt;&gt;/L&lt;&lt;504.0,438.0&gt;--&lt;519.0,456.0&gt;&gt; = 11.555835597290931

* u9C35 (U+9C35): L&lt;&lt;199.0,725.0&gt;--&lt;187.0,689.0&gt;&gt;/L&lt;&lt;187.0,689.0&gt;--&lt;198.0,714.0&gt;&gt; = 5.3145456699448

* u9C37 (U+9C37): L&lt;&lt;467.0,-52.0&gt;--&lt;467.0,352.0&gt;&gt;/L&lt;&lt;467.0,352.0&gt;--&lt;461.0,326.0&gt;&gt; = 12.994616791916512

* u9C42 (U+9C42): L&lt;&lt;397.0,130.0&gt;--&lt;406.0,-27.0&gt;&gt;/L&lt;&lt;406.0,-27.0&gt;--&lt;440.0,306.0&gt;&gt; = 9.110698011690413

* u9C67 (U+9C67): L&lt;&lt;558.0,114.0&gt;--&lt;608.0,123.0&gt;&gt;/L&lt;&lt;608.0,123.0&gt;--&lt;558.0,123.0&gt;&gt; = 10.203973721731666

* u9C67 (U+9C67): L&lt;&lt;646.0,30.0&gt;--&lt;612.0,24.0&gt;&gt;/L&lt;&lt;612.0,24.0&gt;--&lt;706.0,24.0&gt;&gt; = 10.007979801441312

* u9C67 (U+9C67): L&lt;&lt;786.0,123.0&gt;--&lt;763.0,123.0&gt;&gt;/L&lt;&lt;763.0,123.0&gt;--&lt;786.0,118.0&gt;&gt; = 12.2647737278924

* u9C67 (U+9C67): L&lt;&lt;882.0,108.0&gt;--&lt;829.0,108.0&gt;&gt;/L&lt;&lt;829.0,108.0&gt;--&lt;838.0,106.0&gt;&gt; = 12.528807709151522

* u9C7F (U+9C7F): L&lt;&lt;650.0,-24.0&gt;--&lt;650.0,260.0&gt;&gt;/B&lt;&lt;650.0,260.0&gt;-&lt;625.0,150.0&gt;-&lt;590.5,81.0&gt;&gt; = 12.80426606528674

* u9CC5 (U+9CC5): L&lt;&lt;509.0,-52.0&gt;--&lt;509.0,180.0&gt;&gt;/L&lt;&lt;509.0,180.0&gt;--&lt;478.0,47.0&gt;&gt; = 13.120403152977243

* u9CD8 (U+9CD8): L&lt;&lt;199.0,725.0&gt;--&lt;187.0,689.0&gt;&gt;/L&lt;&lt;187.0,689.0&gt;--&lt;198.0,714.0&gt;&gt; = 5.3145456699448

* u9CE2 (U+9CE2): L&lt;&lt;566.0,114.0&gt;--&lt;616.0,123.0&gt;&gt;/L&lt;&lt;616.0,123.0&gt;--&lt;566.0,123.0&gt;&gt; = 10.203973721731666

* u9CE2 (U+9CE2): L&lt;&lt;654.0,30.0&gt;--&lt;620.0,24.0&gt;&gt;/L&lt;&lt;620.0,24.0&gt;--&lt;714.0,24.0&gt;&gt; = 10.007979801441312

* u9CE2 (U+9CE2): L&lt;&lt;794.0,123.0&gt;--&lt;771.0,123.0&gt;&gt;/L&lt;&lt;771.0,123.0&gt;--&lt;794.0,118.0&gt;&gt; = 12.2647737278924

* u9CE2 (U+9CE2): L&lt;&lt;890.0,108.0&gt;--&lt;837.0,108.0&gt;&gt;/L&lt;&lt;837.0,108.0&gt;--&lt;846.0,106.0&gt;&gt; = 12.528807709151522

* u9CE7 (U+9CE7): L&lt;&lt;583.0,375.0&gt;--&lt;663.0,391.0&gt;&gt;/L&lt;&lt;663.0,391.0&gt;--&lt;195.0,391.0&gt;&gt; = 11.309932474020195

* u9D1B (U+9D1B): L&lt;&lt;587.0,69.0&gt;--&lt;672.0,86.0&gt;&gt;/L&lt;&lt;672.0,86.0&gt;--&lt;199.0,86.0&gt;&gt; = 11.309932474020195

* u9D2A (U+9D2A): L&lt;&lt;793.0,162.0&gt;--&lt;809.0,-6.0&gt;&gt;/L&lt;&lt;809.0,-6.0&gt;--&lt;809.0,-5.0&gt;&gt; = 5.4403320310054815

* u9D2C (U+9D2C): L&lt;&lt;816.0,636.0&gt;--&lt;492.0,636.0&gt;&gt;/L&lt;&lt;492.0,636.0&gt;--&lt;558.0,621.0&gt;&gt; = 12.80426606528674

* u9D50 (U+9D50): L&lt;&lt;188.0,370.0&gt;--&lt;241.0,150.0&gt;&gt;/L&lt;&lt;241.0,150.0&gt;--&lt;241.0,684.0&gt;&gt; = 13.544973367945516

* u9D50 (U+9D50): L&lt;&lt;323.0,684.0&gt;--&lt;323.0,167.0&gt;&gt;/B&lt;&lt;323.0,167.0&gt;-&lt;347.0,269.0&gt;-&lt;358.5,371.0&gt;&gt; = 13.24051991518721

* u9D72 (U+9D72): L&lt;&lt;816.0,-2.0&gt;--&lt;794.0,-4.0&gt;&gt;/L&lt;&lt;794.0,-4.0&gt;--&lt;847.0,-7.0&gt;&gt; = 8.434129203836921

* u9DA0 (U+9DA0): L&lt;&lt;294.0,362.0&gt;--&lt;278.0,362.0&gt;&gt;/L&lt;&lt;278.0,362.0&gt;--&lt;351.0,346.0&gt;&gt; = 12.36249241571429

* u9DA4 (U+9DA4): L&lt;&lt;782.0,164.0&gt;--&lt;798.0,-5.0&gt;&gt;/L&lt;&lt;798.0,-5.0&gt;--&lt;798.0,-4.0&gt;&gt; = 5.408332157475356

* u9E40 (U+9E40): L&lt;&lt;191.0,393.0&gt;--&lt;245.0,171.0&gt;&gt;/L&lt;&lt;245.0,171.0&gt;--&lt;245.0,711.0&gt;&gt; = 13.67130713219584

* u9E40 (U+9E40): L&lt;&lt;329.0,711.0&gt;--&lt;329.0,188.0&gt;&gt;/B&lt;&lt;329.0,188.0&gt;-&lt;353.0,291.0&gt;-&lt;365.0,394.0&gt;&gt; = 13.11643612539148

* u9E88 (U+9E88): L&lt;&lt;253.0,194.0&gt;--&lt;602.0,194.0&gt;&gt;/L&lt;&lt;602.0,194.0&gt;--&lt;434.0,230.0&gt;&gt; = 12.094757077012089

* u9E8C (U+9E8C): L&lt;&lt;921.0,22.0&gt;--&lt;750.0,22.0&gt;&gt;/L&lt;&lt;750.0,22.0&gt;--&lt;890.0,-13.0&gt;&gt; = 14.036243467926484

* u9E9D (U+9E9D): L&lt;&lt;218.0,3.0&gt;--&lt;345.0,45.0&gt;&gt;/L&lt;&lt;345.0,45.0&gt;--&lt;213.0,33.0&gt;&gt; = 13.105069152125633

* u9EBB (U+9EBB): L&lt;&lt;851.0,-10.0&gt;--&lt;768.0,323.0&gt;&gt;/L&lt;&lt;768.0,323.0&gt;--&lt;768.0,-51.0&gt;&gt; = 13.995751757697208

* u9ECE (U+9ECE): L&lt;&lt;904.0,173.0&gt;--&lt;786.0,243.0&gt;&gt;/L&lt;&lt;786.0,243.0&gt;--&lt;789.0,240.0&gt;&gt; = 14.32271997820355

* u9EE5 (U+9EE5): L&lt;&lt;332.0,743.0&gt;--&lt;332.0,545.0&gt;&gt;/L&lt;&lt;332.0,545.0&gt;--&lt;366.0,694.0&gt;&gt; = 12.854117368988941

* u9EEF (U+9EEF): L&lt;&lt;324.0,743.0&gt;--&lt;324.0,557.0&gt;&gt;/L&lt;&lt;324.0,557.0&gt;--&lt;362.0,708.0&gt;&gt; = 14.12548915823142

* u9EEF (U+9EEF): L&lt;&lt;404.0,494.0&gt;--&lt;404.0,687.0&gt;&gt;/L&lt;&lt;404.0,687.0&gt;--&lt;363.0,524.0&gt;&gt; = 14.118921303056382

* u9F13 (U+9F13): L&lt;&lt;76.0,14.0&gt;--&lt;179.0,26.0&gt;&gt;/L&lt;&lt;179.0,26.0&gt;--&lt;156.0,25.0&gt;&gt; = 4.155725288275133

* u9F49 (U+9F49): L&lt;&lt;717.0,101.0&gt;--&lt;891.0,137.0&gt;&gt;/L&lt;&lt;891.0,137.0&gt;--&lt;677.0,137.0&gt;&gt; = 11.689369175439202

* u9F4E (U+9F4E): L&lt;&lt;243.0,6.0&gt;--&lt;358.0,35.0&gt;&gt;/L&lt;&lt;358.0,35.0&gt;--&lt;276.0,35.0&gt;&gt; = 14.15341258785141

* u9F4E (U+9F4E): L&lt;&lt;698.0,35.0&gt;--&lt;616.0,35.0&gt;&gt;/L&lt;&lt;616.0,35.0&gt;--&lt;737.0,6.0&gt;&gt; = 13.477822753241302

* u9F63 (U+9F63): L&lt;&lt;607.0,108.0&gt;--&lt;607.0,355.0&gt;&gt;/L&lt;&lt;607.0,355.0&gt;--&lt;604.0,298.0&gt;&gt; = 3.012787504183286

* u9F7C (U+9F7C): L&lt;&lt;872.0,425.0&gt;--&lt;853.0,505.0&gt;&gt;/L&lt;&lt;853.0,505.0&gt;--&lt;853.0,383.0&gt;&gt; = 13.360218444764461

* u9F95 (U+9F95): L&lt;&lt;255.0,695.0&gt;--&lt;757.0,695.0&gt;&gt;/L&lt;&lt;757.0,695.0&gt;--&lt;479.0,761.0&gt;&gt; = 13.355340962907436

* uFA11 (U+FA11): L&lt;&lt;631.0,434.0&gt;--&lt;751.0,434.0&gt;&gt;/L&lt;&lt;751.0,434.0&gt;--&lt;735.0,435.0&gt;&gt; = 3.576334374997269

* uFA28 (U+FA28): L&lt;&lt;694.0,334.0&gt;--&lt;646.0,332.0&gt;&gt;/L&lt;&lt;646.0,332.0&gt;--&lt;758.0,332.0&gt;&gt; = 2.3859440303887243
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* beta (U+03B2): L&lt;&lt;172.0,497.0&gt;--&lt;169.0,-200.0&gt;&gt;

* beta (U+03B2): L&lt;&lt;73.0,-200.0&gt;--&lt;76.0,497.0&gt;&gt;

* dotlessi (U+0131): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* dotlessi (U+0131): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* germandbls (U+00DF): L&lt;&lt;157.0,497.0&gt;--&lt;154.0,0.0&gt;&gt;

* germandbls (U+00DF): L&lt;&lt;58.0,0.0&gt;--&lt;61.0,497.0&gt;&gt;

* iacute (U+00ED): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* iacute (U+00ED): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* ibreve (U+012D): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* ibreve (U+012D): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* icircumflex (U+00EE): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* icircumflex (U+00EE): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* idieresis (U+00EF): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* idieresis (U+00EF): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* igrave (U+00EC): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* igrave (U+00EC): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* imacron (U+012B): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* imacron (U+012B): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* itilde (U+0129): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* itilde (U+0129): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* oneeighth (U+215B): L&lt;&lt;216.0,750.0&gt;--&lt;214.0,335.0&gt;&gt;

* onehalf (U+00BD): L&lt;&lt;327.0,750.0&gt;--&lt;325.0,335.0&gt;&gt;

* onequarter (U+00BC): L&lt;&lt;317.0,750.0&gt;--&lt;315.0,335.0&gt;&gt;

* onethird (U+2153): L&lt;&lt;216.0,750.0&gt;--&lt;214.0,335.0&gt;&gt;

* paragraph (U+00B6): L&lt;&lt;245.0,-89.0&gt;--&lt;244.0,695.0&gt;&gt;

* rho (U+03C1): L&lt;&lt;142.0,42.0&gt;--&lt;140.0,-200.0&gt;&gt;

* u00B9 (U+00B9): L&lt;&lt;216.0,750.0&gt;--&lt;214.0,335.0&gt;&gt;

* u01D0 (U+01D0): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* u01D0 (U+01D0): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* u0209 (U+0209): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* u0209 (U+0209): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* u020B (U+020B): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* u020B (U+020B): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* u03D0 (U+03D0): L&lt;&lt;59.0,257.0&gt;--&lt;61.0,494.0&gt;&gt;

* u0457 (U+0457): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* u0457 (U+0457): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* u1E2F (U+1E2F): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* u1E2F (U+1E2F): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* u1E9E (U+1E9E): L&lt;&lt;157.0,470.0&gt;--&lt;154.0,0.0&gt;&gt;

* u1E9E (U+1E9E): L&lt;&lt;58.0,0.0&gt;--&lt;61.0,470.0&gt;&gt;

* u1EC9 (U+1EC9): L&lt;&lt;111.0,0.0&gt;--&lt;112.0,510.0&gt;&gt;

* u1EC9 (U+1EC9): L&lt;&lt;204.0,510.0&gt;--&lt;203.0,0.0&gt;&gt;

* u2081 (U+2081): L&lt;&lt;216.0,365.0&gt;--&lt;214.0,-50.0&gt;&gt;

* u2150 (U+2150): L&lt;&lt;216.0,750.0&gt;--&lt;214.0,335.0&gt;&gt;

* u2151 (U+2151): L&lt;&lt;216.0,750.0&gt;--&lt;214.0,335.0&gt;&gt;

* u2152 (U+2152): L&lt;&lt;216.0,750.0&gt;--&lt;214.0,335.0&gt;&gt;

* u2152 (U+2152): L&lt;&lt;562.0,415.0&gt;--&lt;560.0,0.0&gt;&gt;

* u2155 (U+2155): L&lt;&lt;225.0,750.0&gt;--&lt;223.0,335.0&gt;&gt;

* u2159 (U+2159): L&lt;&lt;216.0,750.0&gt;--&lt;214.0,335.0&gt;&gt;

* u215F (U+215F): L&lt;&lt;216.0,750.0&gt;--&lt;214.0,335.0&gt;&gt;

* u2230 (U+2230): L&lt;&lt;463.0,483.0&gt;--&lt;308.0,482.0&gt;&gt;

* u25ED7 (U+25ED7): L&lt;&lt;169.0,754.0&gt;--&lt;170.0,420.0&gt;&gt;

* u25ED7 (U+25ED7): L&lt;&lt;95.0,420.0&gt;--&lt;94.0,754.0&gt;&gt;

* u29F8C (U+29F8C): L&lt;&lt;928.0,686.0&gt;--&lt;567.0,685.0&gt;&gt;

* u3051 (U+3051): L&lt;&lt;192.0,706.0&gt;--&lt;197.0,85.0&gt;&gt;

* u3051.vert: L&lt;&lt;282.0,795.0&gt;--&lt;287.0,174.0&gt;&gt;

* u3052 (U+3052): L&lt;&lt;192.0,706.0&gt;--&lt;197.0,85.0&gt;&gt;

* u3052.vert: L&lt;&lt;275.0,780.0&gt;--&lt;280.0,159.0&gt;&gt;

* u3096 (U+3096): L&lt;&lt;167.0,560.0&gt;--&lt;171.0,60.0&gt;&gt;

* u3096.vert: L&lt;&lt;420.0,787.0&gt;--&lt;424.0,287.0&gt;&gt;

* u30CC (U+30CC): L&lt;&lt;655.0,626.0&gt;--&lt;69.0,623.0&gt;&gt;

* u30CC (U+30CC): L&lt;&lt;69.0,671.0&gt;--&lt;791.0,676.0&gt;&gt;

* u30CC.vert: L&lt;&lt;151.0,749.0&gt;--&lt;873.0,754.0&gt;&gt;

* u30CC.vert: L&lt;&lt;737.0,704.0&gt;--&lt;151.0,701.0&gt;&gt;

* u3108 (U+3108): L&lt;&lt;149.0,-24.0&gt;--&lt;147.0,700.0&gt;&gt;

* u3108 (U+3108): L&lt;&lt;243.0,700.0&gt;--&lt;245.0,24.0&gt;&gt;

* u311D (U+311D): L&lt;&lt;245.0,579.0&gt;--&lt;244.0,784.0&gt;&gt;

* u311D (U+311D): L&lt;&lt;246.0,-24.0&gt;--&lt;245.0,531.0&gt;&gt;

* u311D (U+311D): L&lt;&lt;340.0,784.0&gt;--&lt;341.0,579.0&gt;&gt;

* u311D (U+311D): L&lt;&lt;341.0,531.0&gt;--&lt;342.0,24.0&gt;&gt;

* u3B0A (U+3B0A): L&lt;&lt;285.0,136.0&gt;--&lt;865.0,134.0&gt;&gt;

* u3B0A (U+3B0A): L&lt;&lt;650.0,92.0&gt;--&lt;257.0,93.0&gt;&gt;

* u3DB2 (U+3DB2): L&lt;&lt;523.0,736.0&gt;--&lt;522.0,518.0&gt;&gt;

* u4383 (U+4383): L&lt;&lt;227.0,474.0&gt;--&lt;226.0,654.0&gt;&gt;

* u4383 (U+4383): L&lt;&lt;308.0,654.0&gt;--&lt;309.0,474.0&gt;&gt;

* u44EA (U+44EA): L&lt;&lt;358.0,256.0&gt;--&lt;896.0,260.0&gt;&gt;

* u44EC (U+44EC): L&lt;&lt;449.0,442.0&gt;--&lt;450.0,625.0&gt;&gt;

* u4729 (U+4729): L&lt;&lt;604.0,532.0&gt;--&lt;727.0,533.0&gt;&gt;

* u4C3E (U+4C3E): L&lt;&lt;602.0,24.0&gt;--&lt;834.0,25.0&gt;&gt;

* u4C3E (U+4C3E): L&lt;&lt;929.0,-23.0&gt;--&lt;514.0,-24.0&gt;&gt;

* u4E82 (U+4E82): L&lt;&lt;463.0,254.0&gt;--&lt;462.0,417.0&gt;&gt;

* u4E82 (U+4E82): L&lt;&lt;464.0,26.0&gt;--&lt;463.0,240.0&gt;&gt;

* u4E82 (U+4E82): L&lt;&lt;551.0,465.0&gt;--&lt;553.0,-32.0&gt;&gt;

* u4F26 (U+4F26): L&lt;&lt;548.0,26.0&gt;--&lt;794.0,25.0&gt;&gt;

* u4F57 (U+4F57): L&lt;&lt;555.0,26.0&gt;--&lt;801.0,25.0&gt;&gt;

* u4F60 (U+4F60): L&lt;&lt;491.0,688.0&gt;--&lt;937.0,687.0&gt;&gt;

* u5115 (U+5115): L&lt;&lt;690.0,334.0&gt;--&lt;688.0,581.0&gt;&gt;

* u5189 (U+5189): L&lt;&lt;456.0,474.0&gt;--&lt;455.0,654.0&gt;&gt;

* u5189 (U+5189): L&lt;&lt;551.0,654.0&gt;--&lt;552.0,474.0&gt;&gt;

* u51E4 (U+51E4): L&lt;&lt;629.0,557.0&gt;--&lt;238.0,554.0&gt;&gt;

* u5284 (U+5284): L&lt;&lt;229.0,525.0&gt;--&lt;228.0,645.0&gt;&gt;

* u5284 (U+5284): L&lt;&lt;302.0,645.0&gt;--&lt;303.0,525.0&gt;&gt;

* u5338 (U+5338): L&lt;&lt;179.0,-24.0&gt;--&lt;177.0,700.0&gt;&gt;

* u5338 (U+5338): L&lt;&lt;273.0,700.0&gt;--&lt;275.0,24.0&gt;&gt;

* u53BE (U+53BE): L&lt;&lt;55.0,782.0&gt;--&lt;809.0,784.0&gt;&gt;

* u53BE (U+53BE): L&lt;&lt;715.0,736.0&gt;--&lt;55.0,734.0&gt;&gt;

* u53C6 (U+53C6): L&lt;&lt;757.0,153.0&gt;--&lt;590.0,154.0&gt;&gt;

* u5427 (U+5427): L&lt;&lt;523.0,24.0&gt;--&lt;797.0,25.0&gt;&gt;

* u5427 (U+5427): L&lt;&lt;893.0,-23.0&gt;--&lt;434.0,-24.0&gt;&gt;

* u556D (U+556D): L&lt;&lt;237.0,200.0&gt;--&lt;238.0,611.0&gt;&gt;

* u556D (U+556D): L&lt;&lt;317.0,659.0&gt;--&lt;315.0,113.0&gt;&gt;

* u556D (U+556D): L&lt;&lt;87.0,113.0&gt;--&lt;89.0,680.0&gt;&gt;

* u55CD (U+55CD): L&lt;&lt;237.0,200.0&gt;--&lt;238.0,611.0&gt;&gt;

* u55CD (U+55CD): L&lt;&lt;317.0,659.0&gt;--&lt;315.0,113.0&gt;&gt;

* u55CD (U+55CD): L&lt;&lt;87.0,113.0&gt;--&lt;89.0,680.0&gt;&gt;

* u55F2 (U+55F2): L&lt;&lt;635.0,460.0&gt;--&lt;868.0,462.0&gt;&gt;

* u55F3 (U+55F3): L&lt;&lt;733.0,153.0&gt;--&lt;538.0,154.0&gt;&gt;

* u5623 (U+5623): L&lt;&lt;767.0,480.0&gt;--&lt;766.0,357.0&gt;&gt;

* u5643 (U+5643): L&lt;&lt;614.0,511.0&gt;--&lt;613.0,706.0&gt;&gt;

* u5643 (U+5643): L&lt;&lt;704.0,715.0&gt;--&lt;705.0,511.0&gt;&gt;

* u569A (U+569A): L&lt;&lt;169.0,184.0&gt;--&lt;170.0,593.0&gt;&gt;

* u569A (U+569A): L&lt;&lt;265.0,584.0&gt;--&lt;838.0,583.0&gt;&gt;

* u56E4 (U+56E4): L&lt;&lt;456.0,331.0&gt;--&lt;457.0,557.0&gt;&gt;

* u56F1 (U+56F1): L&lt;&lt;488.0,440.0&gt;--&lt;715.0,439.0&gt;&gt;

* u57D4 (U+57D4): L&lt;&lt;607.0,667.0&gt;--&lt;606.0,814.0&gt;&gt;

* u57D4 (U+57D4): L&lt;&lt;609.0,356.0&gt;--&lt;608.0,484.0&gt;&gt;

* u57D4 (U+57D4): L&lt;&lt;610.0,185.0&gt;--&lt;609.0,308.0&gt;&gt;

* u57D4 (U+57D4): L&lt;&lt;611.0,-55.0&gt;--&lt;610.0,137.0&gt;&gt;

* u57D4 (U+57D4): L&lt;&lt;702.0,814.0&gt;--&lt;703.0,667.0&gt;&gt;

* u57D4 (U+57D4): L&lt;&lt;704.0,484.0&gt;--&lt;705.0,356.0&gt;&gt;

* u57D4 (U+57D4): L&lt;&lt;705.0,308.0&gt;--&lt;706.0,185.0&gt;&gt;

* u57D4 (U+57D4): L&lt;&lt;706.0,137.0&gt;--&lt;707.0,-55.0&gt;&gt;

* u580B (U+580B): L&lt;&lt;757.0,736.0&gt;--&lt;756.0,523.0&gt;&gt;

* u5A9B (U+5A9B): L&lt;&lt;548.0,202.0&gt;--&lt;918.0,199.0&gt;&gt;

* u5A9B (U+5A9B): L&lt;&lt;752.0,153.0&gt;--&lt;534.0,154.0&gt;&gt;

* u5AD2 (U+5AD2): L&lt;&lt;748.0,153.0&gt;--&lt;569.0,154.0&gt;&gt;

* u5C9A (U+5C9A): L&lt;&lt;205.0,518.0&gt;--&lt;830.0,519.0&gt;&gt;

* u5C9A (U+5C9A): L&lt;&lt;738.0,471.0&gt;--&lt;202.0,470.0&gt;&gt;

* u5C9C (U+5C9C): L&lt;&lt;233.0,24.0&gt;--&lt;790.0,25.0&gt;&gt;

* u5C9C (U+5C9C): L&lt;&lt;886.0,-23.0&gt;--&lt;137.0,-24.0&gt;&gt;

* u5D50 (U+5D50): L&lt;&lt;205.0,558.0&gt;--&lt;830.0,559.0&gt;&gt;

* u5D50 (U+5D50): L&lt;&lt;738.0,511.0&gt;--&lt;202.0,510.0&gt;&gt;

* u5D5C (U+5D5C): L&lt;&lt;568.0,17.0&gt;--&lt;762.0,16.0&gt;&gt;

* u5D5C (U+5D5C): L&lt;&lt;858.0,-32.0&gt;--&lt;568.0,-31.0&gt;&gt;

* u5D93 (U+5D93): L&lt;&lt;628.0,511.0&gt;--&lt;627.0,706.0&gt;&gt;

* u5D93 (U+5D93): L&lt;&lt;714.0,715.0&gt;--&lt;715.0,511.0&gt;&gt;

* u5DDE (U+5DDE): L&lt;&lt;389.0,308.0&gt;--&lt;388.0,576.0&gt;&gt;

* u5DDE (U+5DDE): L&lt;&lt;484.0,576.0&gt;--&lt;485.0,308.0&gt;&gt;

* u5DF4 (U+5DF4): L&lt;&lt;233.0,24.0&gt;--&lt;790.0,25.0&gt;&gt;

* u5DF4 (U+5DF4): L&lt;&lt;886.0,-23.0&gt;--&lt;137.0,-24.0&gt;&gt;

* u5EF1 (U+5EF1): L&lt;&lt;300.0,24.0&gt;--&lt;427.0,25.0&gt;&gt;

* u5EF1 (U+5EF1): L&lt;&lt;509.0,-23.0&gt;--&lt;232.0,-24.0&gt;&gt;

* u5F38 (U+5F38): L&lt;&lt;765.0,736.0&gt;--&lt;764.0,523.0&gt;&gt;

* u5F4E (U+5F4E): L&lt;&lt;478.0,3.0&gt;--&lt;751.0,1.0&gt;&gt;

* u5F4E (U+5F4E): L&lt;&lt;815.0,-47.0&gt;--&lt;478.0,-45.0&gt;&gt;

* u5F59 (U+5F59): L&lt;&lt;456.0,-51.0&gt;--&lt;457.0,66.0&gt;&gt;

* u60A8 (U+60A8): L&lt;&lt;498.0,742.0&gt;--&lt;942.0,741.0&gt;&gt;

* u60A9 (U+60A9): L&lt;&lt;620.0,464.0&gt;--&lt;618.0,810.0&gt;&gt;

* u60A9 (U+60A9): L&lt;&lt;714.0,810.0&gt;--&lt;716.0,464.0&gt;&gt;

* u60F3 (U+60F3): L&lt;&lt;830.0,-23.0&gt;--&lt;339.0,-26.0&gt;&gt;

* u628A (U+628A): L&lt;&lt;577.0,24.0&gt;--&lt;821.0,25.0&gt;&gt;

* u628A (U+628A): L&lt;&lt;917.0,-23.0&gt;--&lt;488.0,-24.0&gt;&gt;

* u62E5 (U+62E5): L&lt;&lt;516.0,736.0&gt;--&lt;515.0,518.0&gt;&gt;

* u63C9 (U+63C9): L&lt;&lt;188.0,522.0&gt;--&lt;55.0,523.0&gt;&gt;

* u63C9 (U+63C9): L&lt;&lt;57.0,571.0&gt;--&lt;188.0,570.0&gt;&gt;

* u63F4 (U+63F4): L&lt;&lt;549.0,202.0&gt;--&lt;926.0,199.0&gt;&gt;

* u63F4 (U+63F4): L&lt;&lt;752.0,153.0&gt;--&lt;535.0,154.0&gt;&gt;

* u6445 (U+6445): L&lt;&lt;684.0,259.0&gt;--&lt;685.0,42.0&gt;&gt;

* u64AD (U+64AD): L&lt;&lt;596.0,511.0&gt;--&lt;595.0,706.0&gt;&gt;

* u64AD (U+64AD): L&lt;&lt;691.0,715.0&gt;--&lt;692.0,511.0&gt;&gt;

* u64E1 (U+64E1): L&lt;&lt;588.0,200.0&gt;--&lt;759.0,201.0&gt;&gt;

* u6549 (U+6549): L&lt;&lt;105.0,420.0&gt;--&lt;103.0,754.0&gt;&gt;

* u6549 (U+6549): L&lt;&lt;185.0,754.0&gt;--&lt;187.0,420.0&gt;&gt;

* u655B (U+655B): L&lt;&lt;193.0,536.0&gt;--&lt;489.0,534.0&gt;&gt;

* u655B (U+655B): L&lt;&lt;489.0,486.0&gt;--&lt;189.0,488.0&gt;&gt;

* u6582 (U+6582): L&lt;&lt;192.0,536.0&gt;--&lt;488.0,534.0&gt;&gt;

* u6582 (U+6582): L&lt;&lt;488.0,486.0&gt;--&lt;188.0,488.0&gt;&gt;

* u6696 (U+6696): L&lt;&lt;529.0,202.0&gt;--&lt;899.0,199.0&gt;&gt;

* u6696 (U+6696): L&lt;&lt;733.0,153.0&gt;--&lt;515.0,154.0&gt;&gt;

* u66A7 (U+66A7): L&lt;&lt;733.0,153.0&gt;--&lt;538.0,154.0&gt;&gt;

* u6777 (U+6777): L&lt;&lt;567.0,24.0&gt;--&lt;827.0,25.0&gt;&gt;

* u6777 (U+6777): L&lt;&lt;923.0,-23.0&gt;--&lt;478.0,-24.0&gt;&gt;

* u67AB (U+67AB): L&lt;&lt;473.0,782.0&gt;--&lt;876.0,784.0&gt;&gt;

* u67AB (U+67AB): L&lt;&lt;796.0,736.0&gt;--&lt;472.0,734.0&gt;&gt;

* u685C (U+685C): L&lt;&lt;632.0,464.0&gt;--&lt;630.0,810.0&gt;&gt;

* u685C (U+685C): L&lt;&lt;726.0,810.0&gt;--&lt;728.0,464.0&gt;&gt;

* u68DA (U+68DA): L&lt;&lt;768.0,736.0&gt;--&lt;767.0,523.0&gt;&gt;

* u6953 (U+6953): L&lt;&lt;473.0,782.0&gt;--&lt;876.0,784.0&gt;&gt;

* u6953 (U+6953): L&lt;&lt;796.0,736.0&gt;--&lt;472.0,734.0&gt;&gt;

* u6AAF (U+6AAF): L&lt;&lt;588.0,200.0&gt;--&lt;759.0,201.0&gt;&gt;

* u6ADB (U+6ADB): L&lt;&lt;515.0,495.0&gt;--&lt;514.0,645.0&gt;&gt;

* u6ADB (U+6ADB): L&lt;&lt;596.0,645.0&gt;--&lt;597.0,495.0&gt;&gt;

* u6CA6 (U+6CA6): L&lt;&lt;510.0,26.0&gt;--&lt;756.0,25.0&gt;&gt;

* u6CA8 (U+6CA8): L&lt;&lt;444.0,782.0&gt;--&lt;871.0,784.0&gt;&gt;

* u6CA8 (U+6CA8): L&lt;&lt;785.0,736.0&gt;--&lt;443.0,734.0&gt;&gt;

* u6D32 (U+6D32): L&lt;&lt;528.0,308.0&gt;--&lt;527.0,576.0&gt;&gt;

* u6D32 (U+6D32): L&lt;&lt;588.0,576.0&gt;--&lt;589.0,308.0&gt;&gt;

* u6D5F (U+6D5F): L&lt;&lt;419.0,628.0&gt;--&lt;421.0,-51.0&gt;&gt;

* u6D89 (U+6D89): L&lt;&lt;569.0,191.0&gt;--&lt;567.0,442.0&gt;&gt;

* u6D89 (U+6D89): L&lt;&lt;663.0,442.0&gt;--&lt;665.0,191.0&gt;&gt;

* u6DDC (U+6DDC): L&lt;&lt;738.0,736.0&gt;--&lt;737.0,523.0&gt;&gt;

* u6E09 (U+6E09): L&lt;&lt;569.0,157.0&gt;--&lt;567.0,442.0&gt;&gt;

* u6E09 (U+6E09): L&lt;&lt;663.0,442.0&gt;--&lt;665.0,141.0&gt;&gt;

* u6E22 (U+6E22): L&lt;&lt;439.0,782.0&gt;--&lt;869.0,784.0&gt;&gt;

* u6E22 (U+6E22): L&lt;&lt;788.0,736.0&gt;--&lt;438.0,734.0&gt;&gt;

* u6E56 (U+6E56): L&lt;&lt;734.0,736.0&gt;--&lt;732.0,506.0&gt;&gt;

* u6E68 (U+6E68): L&lt;&lt;385.0,312.0&gt;--&lt;386.0,763.0&gt;&gt;

* u6E68 (U+6E68): L&lt;&lt;386.0,763.0&gt;--&lt;882.0,762.0&gt;&gt;

* u6E72 (U+6E72): L&lt;&lt;463.0,202.0&gt;--&lt;868.0,199.0&gt;&gt;

* u6E72 (U+6E72): L&lt;&lt;724.0,153.0&gt;--&lt;447.0,154.0&gt;&gt;

* u6ED7 (U+6ED7): L&lt;&lt;500.0,495.0&gt;--&lt;499.0,645.0&gt;&gt;

* u6ED7 (U+6ED7): L&lt;&lt;578.0,645.0&gt;--&lt;579.0,495.0&gt;&gt;

* u6F4B (U+6F4B): L&lt;&lt;595.0,486.0&gt;--&lt;365.0,488.0&gt;&gt;

* u6F58 (U+6F58): L&lt;&lt;554.0,511.0&gt;--&lt;553.0,722.0&gt;&gt;

* u6F58 (U+6F58): L&lt;&lt;649.0,736.0&gt;--&lt;650.0,511.0&gt;&gt;

* u7032 (U+7032): L&lt;&lt;595.0,486.0&gt;--&lt;365.0,488.0&gt;&gt;

* u7051 (U+7051): L&lt;&lt;909.0,408.0&gt;--&lt;910.0,211.0&gt;&gt;

* u7156 (U+7156): L&lt;&lt;752.0,153.0&gt;--&lt;571.0,154.0&gt;&gt;

* u722C (U+722C): L&lt;&lt;621.0,188.0&gt;--&lt;834.0,189.0&gt;&gt;

* u722C (U+722C): L&lt;&lt;916.0,141.0&gt;--&lt;540.0,140.0&gt;&gt;

* u7230 (U+7230): L&lt;&lt;280.0,202.0&gt;--&lt;866.0,199.0&gt;&gt;

* u7230 (U+7230): L&lt;&lt;681.0,153.0&gt;--&lt;258.0,154.0&gt;&gt;

* u7231 (U+7231): L&lt;&lt;308.0,222.0&gt;--&lt;866.0,219.0&gt;&gt;

* u7231 (U+7231): L&lt;&lt;701.0,173.0&gt;--&lt;283.0,174.0&gt;&gt;

* u7238 (U+7238): L&lt;&lt;235.0,24.0&gt;--&lt;792.0,25.0&gt;&gt;

* u7238 (U+7238): L&lt;&lt;888.0,-23.0&gt;--&lt;139.0,-24.0&gt;&gt;

* u7315 (U+7315): L&lt;&lt;704.0,688.0&gt;--&lt;941.0,687.0&gt;&gt;

* u731F (U+731F): L&lt;&lt;517.0,461.0&gt;--&lt;874.0,462.0&gt;&gt;

* u731F (U+731F): L&lt;&lt;620.0,484.0&gt;--&lt;618.0,810.0&gt;&gt;

* u731F (U+731F): L&lt;&lt;714.0,810.0&gt;--&lt;716.0,484.0&gt;&gt;

* u73F1 (U+73F1): L&lt;&lt;612.0,464.0&gt;--&lt;610.0,810.0&gt;&gt;

* u73F1 (U+73F1): L&lt;&lt;706.0,810.0&gt;--&lt;708.0,464.0&gt;&gt;

* u7457 (U+7457): L&lt;&lt;529.0,202.0&gt;--&lt;899.0,199.0&gt;&gt;

* u7457 (U+7457): L&lt;&lt;733.0,153.0&gt;--&lt;515.0,154.0&gt;&gt;

* u7477 (U+7477): L&lt;&lt;733.0,153.0&gt;--&lt;538.0,154.0&gt;&gt;

* u74A0 (U+74A0): L&lt;&lt;596.0,511.0&gt;--&lt;595.0,706.0&gt;&gt;

* u74A0 (U+74A0): L&lt;&lt;691.0,715.0&gt;--&lt;692.0,511.0&gt;&gt;

* u7505 (U+7505): L&lt;&lt;243.0,658.0&gt;--&lt;458.0,657.0&gt;&gt;

* u7505 (U+7505): L&lt;&lt;369.0,609.0&gt;--&lt;240.0,610.0&gt;&gt;

* u75A4 (U+75A4): L&lt;&lt;482.0,18.0&gt;--&lt;852.0,19.0&gt;&gt;

* u75A4 (U+75A4): L&lt;&lt;939.0,-27.0&gt;--&lt;395.0,-28.0&gt;&gt;

* u75AF (U+75AF): L&lt;&lt;424.0,622.0&gt;--&lt;885.0,624.0&gt;&gt;

* u75AF (U+75AF): L&lt;&lt;796.0,579.0&gt;--&lt;423.0,578.0&gt;&gt;

* u760B (U+760B): L&lt;&lt;404.0,659.0&gt;--&lt;874.0,661.0&gt;&gt;

* u760B (U+760B): L&lt;&lt;794.0,613.0&gt;--&lt;402.0,611.0&gt;&gt;

* u7664 (U+7664): L&lt;&lt;476.0,419.0&gt;--&lt;475.0,549.0&gt;&gt;

* u7664 (U+7664): L&lt;&lt;559.0,549.0&gt;--&lt;560.0,419.0&gt;&gt;

* u7670 (U+7670): L&lt;&lt;578.0,-23.0&gt;--&lt;325.0,-24.0&gt;&gt;

* u76A4 (U+76A4): L&lt;&lt;614.0,511.0&gt;--&lt;613.0,706.0&gt;&gt;

* u76A4 (U+76A4): L&lt;&lt;704.0,715.0&gt;--&lt;705.0,511.0&gt;&gt;

* u781C (U+781C): L&lt;&lt;504.0,782.0&gt;--&lt;881.0,784.0&gt;&gt;

* u781C (U+781C): L&lt;&lt;806.0,736.0&gt;--&lt;503.0,734.0&gt;&gt;

* u78B8 (U+78B8): L&lt;&lt;502.0,782.0&gt;--&lt;912.0,784.0&gt;&gt;

* u78B8 (U+78B8): L&lt;&lt;839.0,736.0&gt;--&lt;501.0,734.0&gt;&gt;

* u78FB (U+78FB): L&lt;&lt;632.0,511.0&gt;--&lt;631.0,706.0&gt;&gt;

* u78FB (U+78FB): L&lt;&lt;717.0,715.0&gt;--&lt;718.0,511.0&gt;&gt;

* u7A97 (U+7A97): L&lt;&lt;503.0,330.0&gt;--&lt;730.0,329.0&gt;&gt;

* u7A97 (U+7A97): L&lt;&lt;594.0,281.0&gt;--&lt;465.0,282.0&gt;&gt;

* u7AD2 (U+7AD2): L&lt;&lt;568.0,17.0&gt;--&lt;762.0,16.0&gt;&gt;

* u7AD2 (U+7AD2): L&lt;&lt;858.0,-32.0&gt;--&lt;568.0,-31.0&gt;&gt;

* u7C09 (U+7C09): L&lt;&lt;491.0,466.0&gt;--&lt;607.0,467.0&gt;&gt;

* u7C09 (U+7C09): L&lt;&lt;607.0,420.0&gt;--&lt;481.0,419.0&gt;&gt;

* u7C50 (U+7C50): L&lt;&lt;626.0,106.0&gt;--&lt;627.0,308.0&gt;&gt;

* u7C50 (U+7C50): L&lt;&lt;723.0,308.0&gt;--&lt;722.0,99.0&gt;&gt;

* u7C78 (U+7C78): L&lt;&lt;152.0,754.0&gt;--&lt;154.0,450.0&gt;&gt;

* u7C78 (U+7C78): L&lt;&lt;79.0,450.0&gt;--&lt;77.0,754.0&gt;&gt;

* u7C7C (U+7C7C): L&lt;&lt;172.0,754.0&gt;--&lt;173.0,420.0&gt;&gt;

* u7C7C (U+7C7C): L&lt;&lt;98.0,420.0&gt;--&lt;97.0,754.0&gt;&gt;

* u7C7E (U+7C7E): L&lt;&lt;183.0,754.0&gt;--&lt;185.0,420.0&gt;&gt;

* u7C7E (U+7C7E): L&lt;&lt;96.0,420.0&gt;--&lt;94.0,754.0&gt;&gt;

* u7C81 (U+7C81): L&lt;&lt;110.0,420.0&gt;--&lt;108.0,754.0&gt;&gt;

* u7C81 (U+7C81): L&lt;&lt;204.0,754.0&gt;--&lt;206.0,420.0&gt;&gt;

* u7C83 (U+7C83): L&lt;&lt;166.0,754.0&gt;--&lt;167.0,420.0&gt;&gt;

* u7C83 (U+7C83): L&lt;&lt;99.0,420.0&gt;--&lt;98.0,754.0&gt;&gt;

* u7C89 (U+7C89): L&lt;&lt;101.0,420.0&gt;--&lt;99.0,754.0&gt;&gt;

* u7C89 (U+7C89): L&lt;&lt;195.0,754.0&gt;--&lt;197.0,420.0&gt;&gt;

* u7C8D (U+7C8D): L&lt;&lt;102.0,420.0&gt;--&lt;100.0,754.0&gt;&gt;

* u7C8D (U+7C8D): L&lt;&lt;189.0,754.0&gt;--&lt;191.0,420.0&gt;&gt;

* u7C90 (U+7C90): L&lt;&lt;105.0,420.0&gt;--&lt;103.0,754.0&gt;&gt;

* u7C90 (U+7C90): L&lt;&lt;185.0,754.0&gt;--&lt;187.0,420.0&gt;&gt;

* u7C91 (U+7C91): L&lt;&lt;172.0,754.0&gt;--&lt;173.0,420.0&gt;&gt;

* u7C91 (U+7C91): L&lt;&lt;577.0,24.0&gt;--&lt;821.0,25.0&gt;&gt;

* u7C91 (U+7C91): L&lt;&lt;917.0,-23.0&gt;--&lt;488.0,-24.0&gt;&gt;

* u7C91 (U+7C91): L&lt;&lt;98.0,420.0&gt;--&lt;97.0,754.0&gt;&gt;

* u7C92 (U+7C92): L&lt;&lt;113.0,420.0&gt;--&lt;111.0,754.0&gt;&gt;

* u7C92 (U+7C92): L&lt;&lt;200.0,754.0&gt;--&lt;202.0,420.0&gt;&gt;

* u7C97 (U+7C97): L&lt;&lt;100.0,418.0&gt;--&lt;98.0,742.0&gt;&gt;

* u7C97 (U+7C97): L&lt;&lt;180.0,742.0&gt;--&lt;182.0,418.0&gt;&gt;

* u7C98 (U+7C98): L&lt;&lt;101.0,420.0&gt;--&lt;99.0,754.0&gt;&gt;

* u7C98 (U+7C98): L&lt;&lt;188.0,754.0&gt;--&lt;190.0,420.0&gt;&gt;

* u7C9D (U+7C9D): L&lt;&lt;167.0,754.0&gt;--&lt;168.0,430.0&gt;&gt;

* u7C9D (U+7C9D): L&lt;&lt;83.0,430.0&gt;--&lt;82.0,754.0&gt;&gt;

* u7CA1 (U+7CA1): L&lt;&lt;105.0,420.0&gt;--&lt;104.0,754.0&gt;&gt;

* u7CA1 (U+7CA1): L&lt;&lt;179.0,754.0&gt;--&lt;180.0,420.0&gt;&gt;

* u7CA5 (U+7CA5): L&lt;&lt;347.0,420.0&gt;--&lt;346.0,754.0&gt;&gt;

* u7CA5 (U+7CA5): L&lt;&lt;421.0,754.0&gt;--&lt;422.0,420.0&gt;&gt;

* u7CA7 (U+7CA7): L&lt;&lt;166.0,754.0&gt;--&lt;168.0,420.0&gt;&gt;

* u7CA7 (U+7CA7): L&lt;&lt;93.0,420.0&gt;--&lt;91.0,754.0&gt;&gt;

* u7CA8 (U+7CA8): L&lt;&lt;172.0,754.0&gt;--&lt;173.0,420.0&gt;&gt;

* u7CA8 (U+7CA8): L&lt;&lt;98.0,420.0&gt;--&lt;97.0,754.0&gt;&gt;

* u7CAB (U+7CAB): L&lt;&lt;102.0,420.0&gt;--&lt;101.0,754.0&gt;&gt;

* u7CAB (U+7CAB): L&lt;&lt;183.0,754.0&gt;--&lt;184.0,420.0&gt;&gt;

* u7CB9 (U+7CB9): L&lt;&lt;158.0,754.0&gt;--&lt;159.0,420.0&gt;&gt;

* u7CB9 (U+7CB9): L&lt;&lt;77.0,420.0&gt;--&lt;76.0,754.0&gt;&gt;

* u7CBA (U+7CBA): L&lt;&lt;161.0,754.0&gt;--&lt;162.0,420.0&gt;&gt;

* u7CBA (U+7CBA): L&lt;&lt;87.0,420.0&gt;--&lt;86.0,754.0&gt;&gt;

* u7CBD (U+7CBD): L&lt;&lt;168.0,754.0&gt;--&lt;170.0,420.0&gt;&gt;

* u7CBD (U+7CBD): L&lt;&lt;95.0,420.0&gt;--&lt;93.0,754.0&gt;&gt;

* u7CBE (U+7CBE): L&lt;&lt;107.0,420.0&gt;--&lt;105.0,754.0&gt;&gt;

* u7CBE (U+7CBE): L&lt;&lt;194.0,754.0&gt;--&lt;196.0,420.0&gt;&gt;

* u7CBF (U+7CBF): L&lt;&lt;152.0,754.0&gt;--&lt;154.0,420.0&gt;&gt;

* u7CBF (U+7CBF): L&lt;&lt;79.0,420.0&gt;--&lt;77.0,754.0&gt;&gt;

* u7CC1 (U+7CC1): L&lt;&lt;152.0,754.0&gt;--&lt;154.0,450.0&gt;&gt;

* u7CC1 (U+7CC1): L&lt;&lt;79.0,450.0&gt;--&lt;77.0,754.0&gt;&gt;

* u7CC2 (U+7CC2): L&lt;&lt;171.0,754.0&gt;--&lt;173.0,420.0&gt;&gt;

* u7CC2 (U+7CC2): L&lt;&lt;91.0,420.0&gt;--&lt;89.0,754.0&gt;&gt;

* u7CC5 (U+7CC5): L&lt;&lt;152.0,754.0&gt;--&lt;154.0,420.0&gt;&gt;

* u7CC5 (U+7CC5): L&lt;&lt;79.0,420.0&gt;--&lt;77.0,754.0&gt;&gt;

* u7CC9 (U+7CC9): L&lt;&lt;166.0,754.0&gt;--&lt;168.0,420.0&gt;&gt;

* u7CC9 (U+7CC9): L&lt;&lt;93.0,420.0&gt;--&lt;91.0,754.0&gt;&gt;

* u7CCA (U+7CCA): L&lt;&lt;166.0,754.0&gt;--&lt;167.0,420.0&gt;&gt;

* u7CCA (U+7CCA): L&lt;&lt;99.0,420.0&gt;--&lt;98.0,754.0&gt;&gt;

* u7CCD (U+7CCD): L&lt;&lt;164.0,754.0&gt;--&lt;165.0,430.0&gt;&gt;

* u7CCD (U+7CCD): L&lt;&lt;82.0,430.0&gt;--&lt;81.0,754.0&gt;&gt;

* u7CCE (U+7CCE): L&lt;&lt;161.0,754.0&gt;--&lt;162.0,420.0&gt;&gt;

* u7CCE (U+7CCE): L&lt;&lt;87.0,420.0&gt;--&lt;86.0,754.0&gt;&gt;

* u7CD2 (U+7CD2): L&lt;&lt;141.0,754.0&gt;--&lt;143.0,420.0&gt;&gt;

* u7CD2 (U+7CD2): L&lt;&lt;75.0,420.0&gt;--&lt;73.0,754.0&gt;&gt;

* u7CD7 (U+7CD7): L&lt;&lt;164.0,754.0&gt;--&lt;166.0,420.0&gt;&gt;

* u7CD7 (U+7CD7): L&lt;&lt;85.0,420.0&gt;--&lt;84.0,754.0&gt;&gt;

* u7CD8 (U+7CD8): L&lt;&lt;166.0,754.0&gt;--&lt;168.0,420.0&gt;&gt;

* u7CD8 (U+7CD8): L&lt;&lt;93.0,420.0&gt;--&lt;91.0,754.0&gt;&gt;

* u7CDD (U+7CDD): L&lt;&lt;152.0,754.0&gt;--&lt;154.0,450.0&gt;&gt;

* u7CDD (U+7CDD): L&lt;&lt;79.0,450.0&gt;--&lt;77.0,754.0&gt;&gt;

* u7CDF (U+7CDF): L&lt;&lt;160.0,754.0&gt;--&lt;161.0,420.0&gt;&gt;

* u7CDF (U+7CDF): L&lt;&lt;86.0,420.0&gt;--&lt;85.0,754.0&gt;&gt;

* u7CE0 (U+7CE0): L&lt;&lt;148.0,754.0&gt;--&lt;150.0,420.0&gt;&gt;

* u7CE0 (U+7CE0): L&lt;&lt;75.0,420.0&gt;--&lt;73.0,754.0&gt;&gt;

* u7CE2 (U+7CE2): L&lt;&lt;166.0,754.0&gt;--&lt;168.0,420.0&gt;&gt;

* u7CE2 (U+7CE2): L&lt;&lt;86.0,420.0&gt;--&lt;84.0,754.0&gt;&gt;

* u7CE7 (U+7CE7): L&lt;&lt;169.0,754.0&gt;--&lt;170.0,420.0&gt;&gt;

* u7CE7 (U+7CE7): L&lt;&lt;95.0,420.0&gt;--&lt;94.0,754.0&gt;&gt;

* u7CE8 (U+7CE8): L&lt;&lt;141.0,754.0&gt;--&lt;143.0,420.0&gt;&gt;

* u7CE8 (U+7CE8): L&lt;&lt;75.0,420.0&gt;--&lt;73.0,754.0&gt;&gt;

* u7CEC (U+7CEC): L&lt;&lt;160.0,754.0&gt;--&lt;161.0,420.0&gt;&gt;

* u7CEC (U+7CEC): L&lt;&lt;86.0,420.0&gt;--&lt;85.0,754.0&gt;&gt;

* u7CEF (U+7CEF): L&lt;&lt;102.0,420.0&gt;--&lt;100.0,754.0&gt;&gt;

* u7CEF (U+7CEF): L&lt;&lt;168.0,754.0&gt;--&lt;170.0,420.0&gt;&gt;

* u7CF0 (U+7CF0): L&lt;&lt;148.0,754.0&gt;--&lt;150.0,420.0&gt;&gt;

* u7CF0 (U+7CF0): L&lt;&lt;75.0,420.0&gt;--&lt;73.0,754.0&gt;&gt;

* u7CF2 (U+7CF2): L&lt;&lt;161.0,754.0&gt;--&lt;162.0,430.0&gt;&gt;

* u7CF2 (U+7CF2): L&lt;&lt;87.0,430.0&gt;--&lt;86.0,754.0&gt;&gt;

* u7CF6 (U+7CF6): L&lt;&lt;101.0,192.0&gt;--&lt;100.0,367.0&gt;&gt;

* u7CF6 (U+7CF6): L&lt;&lt;168.0,367.0&gt;--&lt;169.0,192.0&gt;&gt;

* u7DE9 (U+7DE9): L&lt;&lt;571.0,202.0&gt;--&lt;921.0,199.0&gt;&gt;

* u7DE9 (U+7DE9): L&lt;&lt;761.0,153.0&gt;--&lt;558.0,154.0&gt;&gt;

* u7E43 (U+7E43): L&lt;&lt;774.0,480.0&gt;--&lt;773.0,357.0&gt;&gt;

* u7E83 (U+7E83): L&lt;&lt;725.0,332.0&gt;--&lt;723.0,580.0&gt;&gt;

* u7EB6 (U+7EB6): L&lt;&lt;537.0,26.0&gt;--&lt;783.0,25.0&gt;&gt;

* u7F13 (U+7F13): L&lt;&lt;579.0,202.0&gt;--&lt;929.0,199.0&gt;&gt;

* u7F13 (U+7F13): L&lt;&lt;769.0,153.0&gt;--&lt;566.0,154.0&gt;&gt;

* u7F69 (U+7F69): L&lt;&lt;449.0,422.0&gt;--&lt;450.0,575.0&gt;&gt;

* u7F81 (U+7F81): L&lt;&lt;645.0,219.0&gt;--&lt;768.0,220.0&gt;&gt;

* u7F93 (U+7F93): L&lt;&lt;577.0,24.0&gt;--&lt;821.0,25.0&gt;&gt;

* u7F93 (U+7F93): L&lt;&lt;917.0,-23.0&gt;--&lt;488.0,-24.0&gt;&gt;

* u800B (U+800B): L&lt;&lt;352.0,240.0&gt;--&lt;687.0,242.0&gt;&gt;

* u800B (U+800B): L&lt;&lt;462.0,192.0&gt;--&lt;161.0,190.0&gt;&gt;

* u8019 (U+8019): L&lt;&lt;561.0,24.0&gt;--&lt;798.0,25.0&gt;&gt;

* u8019 (U+8019): L&lt;&lt;894.0,-23.0&gt;--&lt;465.0,-24.0&gt;&gt;

* u8030 (U+8030): L&lt;&lt;929.0,438.0&gt;--&lt;928.0,314.0&gt;&gt;

* u8043 (U+8043): L&lt;&lt;635.0,474.0&gt;--&lt;634.0,654.0&gt;&gt;

* u8043 (U+8043): L&lt;&lt;722.0,654.0&gt;--&lt;723.0,474.0&gt;&gt;

* u8133 (U+8133): L&lt;&lt;637.0,464.0&gt;--&lt;636.0,810.0&gt;&gt;

* u8133 (U+8133): L&lt;&lt;732.0,810.0&gt;--&lt;733.0,464.0&gt;&gt;

* u817E (U+817E): L&lt;&lt;562.0,219.0&gt;--&lt;695.0,220.0&gt;&gt;

* u817E (U+817E): L&lt;&lt;801.0,177.0&gt;--&lt;562.0,175.0&gt;&gt;

* u819A (U+819A): L&lt;&lt;661.0,1.0&gt;--&lt;780.0,0.0&gt;&gt;

* u81FA (U+81FA): L&lt;&lt;374.0,200.0&gt;--&lt;681.0,201.0&gt;&gt;

* u8278 (U+8278): L&lt;&lt;235.0,666.0&gt;--&lt;234.0,809.0&gt;&gt;

* u8278 (U+8278): L&lt;&lt;324.0,667.0&gt;--&lt;325.0,546.0&gt;&gt;

* u82D2 (U+82D2): L&lt;&lt;451.0,352.0&gt;--&lt;450.0,475.0&gt;&gt;

* u82D2 (U+82D2): L&lt;&lt;452.0,185.0&gt;--&lt;451.0,304.0&gt;&gt;

* u82D2 (U+82D2): L&lt;&lt;546.0,475.0&gt;--&lt;547.0,352.0&gt;&gt;

* u82D2 (U+82D2): L&lt;&lt;547.0,304.0&gt;--&lt;548.0,185.0&gt;&gt;

* u846C (U+846C): L&lt;&lt;266.0,491.0&gt;--&lt;497.0,492.0&gt;&gt;

* u846C (U+846C): L&lt;&lt;381.0,444.0&gt;--&lt;243.0,443.0&gt;&gt;

* u84AF (U+84AF): L&lt;&lt;468.0,501.0&gt;--&lt;467.0,364.0&gt;&gt;

* u8525 (U+8525): L&lt;&lt;510.0,530.0&gt;--&lt;736.0,529.0&gt;&gt;

* u8525 (U+8525): L&lt;&lt;588.0,481.0&gt;--&lt;464.0,482.0&gt;&gt;

* u8539 (U+8539): L&lt;&lt;202.0,367.0&gt;--&lt;482.0,365.0&gt;&gt;

* u8539 (U+8539): L&lt;&lt;489.0,317.0&gt;--&lt;189.0,319.0&gt;&gt;

* u85B9 (U+85B9): L&lt;&lt;366.0,166.0&gt;--&lt;679.0,167.0&gt;&gt;

* u861E (U+861E): L&lt;&lt;304.0,383.0&gt;--&lt;489.0,382.0&gt;&gt;

* u861E (U+861E): L&lt;&lt;496.0,335.0&gt;--&lt;304.0,336.0&gt;&gt;

* u8671 (U+8671): L&lt;&lt;55.0,782.0&gt;--&lt;809.0,784.0&gt;&gt;

* u8671 (U+8671): L&lt;&lt;715.0,736.0&gt;--&lt;55.0,734.0&gt;&gt;

* u8686 (U+8686): L&lt;&lt;588.0,24.0&gt;--&lt;836.0,25.0&gt;&gt;

* u8686 (U+8686): L&lt;&lt;927.0,-23.0&gt;--&lt;504.0,-24.0&gt;&gt;

* u8695 (U+8695): L&lt;&lt;446.0,146.0&gt;--&lt;447.0,269.0&gt;&gt;

* u8695 (U+8695): L&lt;&lt;543.0,269.0&gt;--&lt;542.0,146.0&gt;&gt;

* u86BA (U+86BA): L&lt;&lt;635.0,474.0&gt;--&lt;634.0,654.0&gt;&gt;

* u86BA (U+86BA): L&lt;&lt;722.0,654.0&gt;--&lt;723.0,474.0&gt;&gt;

* u8729 (U+8729): L&lt;&lt;637.0,593.0&gt;--&lt;638.0,712.0&gt;&gt;

* u8729 (U+8729): L&lt;&lt;720.0,712.0&gt;--&lt;719.0,593.0&gt;&gt;

* u874B (U+874B): L&lt;&lt;570.0,461.0&gt;--&lt;861.0,462.0&gt;&gt;

* u874B (U+874B): L&lt;&lt;633.0,490.0&gt;--&lt;632.0,810.0&gt;&gt;

* u874B (U+874B): L&lt;&lt;721.0,810.0&gt;--&lt;722.0,490.0&gt;&gt;

* u8768 (U+8768): L&lt;&lt;318.0,297.0&gt;--&lt;458.0,298.0&gt;&gt;

* u8768 (U+8768): L&lt;&lt;741.0,297.0&gt;--&lt;881.0,298.0&gt;&gt;

* u87A3 (U+87A3): L&lt;&lt;745.0,317.0&gt;--&lt;905.0,318.0&gt;&gt;

* u87BD (U+87BD): L&lt;&lt;332.0,297.0&gt;--&lt;472.0,298.0&gt;&gt;

* u87BD (U+87BD): L&lt;&lt;755.0,297.0&gt;--&lt;895.0,298.0&gt;&gt;

* u87CA (U+87CA): L&lt;&lt;332.0,287.0&gt;--&lt;472.0,288.0&gt;&gt;

* u87CA (U+87CA): L&lt;&lt;755.0,287.0&gt;--&lt;895.0,288.0&gt;&gt;

* u87F2 (U+87F2): L&lt;&lt;334.0,325.0&gt;--&lt;474.0,326.0&gt;&gt;

* u87F2 (U+87F2): L&lt;&lt;757.0,325.0&gt;--&lt;897.0,326.0&gt;&gt;

* u8821 (U+8821): L&lt;&lt;333.0,235.0&gt;--&lt;473.0,236.0&gt;&gt;

* u8821 (U+8821): L&lt;&lt;756.0,235.0&gt;--&lt;896.0,236.0&gt;&gt;

* u8822 (U+8822): L&lt;&lt;332.0,183.0&gt;--&lt;472.0,184.0&gt;&gt;

* u8822 (U+8822): L&lt;&lt;748.0,183.0&gt;--&lt;895.0,184.0&gt;&gt;

* u8827 (U+8827): L&lt;&lt;335.0,244.0&gt;--&lt;475.0,245.0&gt;&gt;

* u8827 (U+8827): L&lt;&lt;758.0,244.0&gt;--&lt;898.0,245.0&gt;&gt;

* u8836 (U+8836): L&lt;&lt;336.0,217.0&gt;--&lt;476.0,218.0&gt;&gt;

* u8836 (U+8836): L&lt;&lt;759.0,217.0&gt;--&lt;899.0,218.0&gt;&gt;

* u8839 (U+8839): L&lt;&lt;335.0,169.0&gt;--&lt;475.0,170.0&gt;&gt;

* u8839 (U+8839): L&lt;&lt;758.0,169.0&gt;--&lt;898.0,170.0&gt;&gt;

* u88DB (U+88DB): L&lt;&lt;243.0,255.0&gt;--&lt;820.0,256.0&gt;&gt;

* u88DB (U+88DB): L&lt;&lt;916.0,209.0&gt;--&lt;445.0,208.0&gt;&gt;

* u898A (U+898A): L&lt;&lt;847.0,148.0&gt;--&lt;635.0,147.0&gt;&gt;

* u8ADB (U+8ADB): L&lt;&lt;431.0,581.0&gt;--&lt;95.0,583.0&gt;&gt;

* u8ADB (U+8ADB): L&lt;&lt;95.0,631.0&gt;--&lt;431.0,629.0&gt;&gt;

* u8AF7 (U+8AF7): L&lt;&lt;468.0,782.0&gt;--&lt;878.0,784.0&gt;&gt;

* u8AF7 (U+8AF7): L&lt;&lt;805.0,736.0&gt;--&lt;467.0,734.0&gt;&gt;

* u8AFC (U+8AFC): L&lt;&lt;571.0,202.0&gt;--&lt;921.0,199.0&gt;&gt;

* u8AFC (U+8AFC): L&lt;&lt;761.0,153.0&gt;--&lt;558.0,154.0&gt;&gt;

* u8B04 (U+8B04): L&lt;&lt;594.0,550.0&gt;--&lt;730.0,551.0&gt;&gt;

* u8B4C (U+8B4C): L&lt;&lt;463.0,233.0&gt;--&lt;790.0,232.0&gt;&gt;

* u8B66 (U+8B66): L&lt;&lt;287.0,464.0&gt;--&lt;409.0,463.0&gt;&gt;

* u8BBD (U+8BBD): L&lt;&lt;483.0,782.0&gt;--&lt;883.0,784.0&gt;&gt;

* u8BBD (U+8BBD): L&lt;&lt;800.0,736.0&gt;--&lt;482.0,734.0&gt;&gt;

* u8C16 (U+8C16): L&lt;&lt;534.0,202.0&gt;--&lt;927.0,199.0&gt;&gt;

* u8C16 (U+8C16): L&lt;&lt;748.0,153.0&gt;--&lt;519.0,154.0&gt;&gt;

* u8C5A (U+8C5A): L&lt;&lt;160.0,202.0&gt;--&lt;158.0,-49.0&gt;&gt;

* u8C5A (U+8C5A): L&lt;&lt;163.0,737.0&gt;--&lt;162.0,506.0&gt;&gt;

* u8C5A (U+8C5A): L&lt;&lt;62.0,-49.0&gt;--&lt;68.0,810.0&gt;&gt;

* u8CD9 (U+8CD9): L&lt;&lt;640.0,593.0&gt;--&lt;641.0,712.0&gt;&gt;

* u8CD9 (U+8CD9): L&lt;&lt;731.0,712.0&gt;--&lt;730.0,593.0&gt;&gt;

* u8E1F (U+8E1F): L&lt;&lt;322.0,205.0&gt;--&lt;323.0,72.0&gt;&gt;

* u8E2A (U+8E2A): L&lt;&lt;250.0,51.0&gt;--&lt;248.0,382.0&gt;&gt;

* u8E2A (U+8E2A): L&lt;&lt;345.0,205.0&gt;--&lt;346.0,71.0&gt;&gt;

* u8E66 (U+8E66): L&lt;&lt;790.0,480.0&gt;--&lt;789.0,357.0&gt;&gt;

* u8E6F (U+8E6F): L&lt;&lt;628.0,511.0&gt;--&lt;627.0,706.0&gt;&gt;

* u8E6F (U+8E6F): L&lt;&lt;714.0,715.0&gt;--&lt;715.0,511.0&gt;&gt;

* u8E70 (U+8E70): L&lt;&lt;302.0,205.0&gt;--&lt;303.0,72.0&gt;&gt;

* u8E95 (U+8E95): L&lt;&lt;302.0,205.0&gt;--&lt;303.0,72.0&gt;&gt;

* u8F2C (U+8F2C): L&lt;&lt;677.0,13.0&gt;--&lt;678.0,298.0&gt;&gt;

* u8F2C (U+8F2C): L&lt;&lt;774.0,298.0&gt;--&lt;773.0,-45.0&gt;&gt;

* u8F40 (U+8F40): L&lt;&lt;829.0,458.0&gt;--&lt;830.0,718.0&gt;&gt;

* u8FAD (U+8FAD): L&lt;&lt;450.0,26.0&gt;--&lt;448.0,417.0&gt;&gt;

* u8FAD (U+8FAD): L&lt;&lt;530.0,465.0&gt;--&lt;532.0,-32.0&gt;&gt;

* u906F (U+906F): L&lt;&lt;301.0,44.0&gt;--&lt;306.0,803.0&gt;&gt;

* u906F (U+906F): L&lt;&lt;384.0,263.0&gt;--&lt;383.0,44.0&gt;&gt;

* u906F (U+906F): L&lt;&lt;386.0,489.0&gt;--&lt;385.0,311.0&gt;&gt;

* u9090 (U+9090): L&lt;&lt;911.0,458.0&gt;--&lt;912.0,285.0&gt;&gt;

* u9091 (U+9091): L&lt;&lt;233.0,24.0&gt;--&lt;790.0,25.0&gt;&gt;

* u9091 (U+9091): L&lt;&lt;886.0,-23.0&gt;--&lt;137.0,-24.0&gt;&gt;

* u9095 (U+9095): L&lt;&lt;223.0,24.0&gt;--&lt;800.0,25.0&gt;&gt;

* u9095 (U+9095): L&lt;&lt;896.0,-23.0&gt;--&lt;127.0,-24.0&gt;&gt;

* u911C (U+911C): L&lt;&lt;481.0,363.0&gt;--&lt;480.0,504.0&gt;&gt;

* u911C (U+911C): L&lt;&lt;555.0,552.0&gt;--&lt;556.0,297.0&gt;&gt;

* u9131 (U+9131): L&lt;&lt;382.0,715.0&gt;--&lt;383.0,511.0&gt;&gt;

* u916C (U+916C): L&lt;&lt;640.0,308.0&gt;--&lt;639.0,576.0&gt;&gt;

* u916C (U+916C): L&lt;&lt;686.0,576.0&gt;--&lt;687.0,308.0&gt;&gt;

* u9229 (U+9229): L&lt;&lt;131.0,308.0&gt;--&lt;283.0,309.0&gt;&gt;

* u9229 (U+9229): L&lt;&lt;283.0,261.0&gt;--&lt;131.0,260.0&gt;&gt;

* u9229 (U+9229): L&lt;&lt;365.0,309.0&gt;--&lt;516.0,310.0&gt;&gt;

* u9229 (U+9229): L&lt;&lt;516.0,262.0&gt;--&lt;365.0,261.0&gt;&gt;

* u9344 (U+9344): L&lt;&lt;677.0,13.0&gt;--&lt;678.0,298.0&gt;&gt;

* u9344 (U+9344): L&lt;&lt;774.0,298.0&gt;--&lt;773.0,-45.0&gt;&gt;

* u9370 (U+9370): L&lt;&lt;666.0,201.0&gt;--&lt;929.0,199.0&gt;&gt;

* u9370 (U+9370): L&lt;&lt;791.0,153.0&gt;--&lt;653.0,154.0&gt;&gt;

* u93F0 (U+93F0): L&lt;&lt;778.0,480.0&gt;--&lt;777.0,357.0&gt;&gt;

* u94AF (U+94AF): L&lt;&lt;569.0,24.0&gt;--&lt;800.0,25.0&gt;&gt;

* u94AF (U+94AF): L&lt;&lt;894.0,-23.0&gt;--&lt;475.0,-24.0&gt;&gt;

* u94D7 (U+94D7): L&lt;&lt;643.0,662.0&gt;--&lt;644.0,814.0&gt;&gt;

* u953E (U+953E): L&lt;&lt;570.0,202.0&gt;--&lt;920.0,199.0&gt;&gt;

* u953E (U+953E): L&lt;&lt;760.0,153.0&gt;--&lt;557.0,154.0&gt;&gt;

* u955A (U+955A): L&lt;&lt;764.0,480.0&gt;--&lt;763.0,357.0&gt;&gt;

* u95A9 (U+95A9): L&lt;&lt;552.0,357.0&gt;--&lt;718.0,358.0&gt;&gt;

* u95EF (U+95EF): L&lt;&lt;409.0,309.0&gt;--&lt;552.0,310.0&gt;&gt;

* u95EF (U+95EF): L&lt;&lt;638.0,267.0&gt;--&lt;313.0,265.0&gt;&gt;

* u964B (U+964B): L&lt;&lt;522.0,46.0&gt;--&lt;517.0,634.0&gt;&gt;

* u964B (U+964B): L&lt;&lt;593.0,561.0&gt;--&lt;595.0,268.0&gt;&gt;

* u964B (U+964B): L&lt;&lt;596.0,219.0&gt;--&lt;597.0,46.0&gt;&gt;

* u97C2 (U+97C2): L&lt;&lt;222.0,46.0&gt;--&lt;62.0,47.0&gt;&gt;

* u97C2 (U+97C2): L&lt;&lt;294.0,93.0&gt;--&lt;453.0,92.0&gt;&gt;

* u97C2 (U+97C2): L&lt;&lt;453.0,44.0&gt;--&lt;294.0,45.0&gt;&gt;

* u97C2 (U+97C2): L&lt;&lt;62.0,95.0&gt;--&lt;222.0,94.0&gt;&gt;

* u97C8 (U+97C8): L&lt;&lt;228.0,46.0&gt;--&lt;62.0,47.0&gt;&gt;

* u97C8 (U+97C8): L&lt;&lt;303.0,93.0&gt;--&lt;468.0,92.0&gt;&gt;

* u97C8 (U+97C8): L&lt;&lt;468.0,44.0&gt;--&lt;303.0,45.0&gt;&gt;

* u97C8 (U+97C8): L&lt;&lt;62.0,95.0&gt;--&lt;228.0,94.0&gt;&gt;

* u97DE (U+97DE): L&lt;&lt;797.0,476.0&gt;--&lt;798.0,736.0&gt;&gt;

* u98A8 (U+98A8): L&lt;&lt;204.0,782.0&gt;--&lt;830.0,784.0&gt;&gt;

* u98A8 (U+98A8): L&lt;&lt;736.0,736.0&gt;--&lt;202.0,734.0&gt;&gt;

* u98AA (U+98AA): L&lt;&lt;224.0,566.0&gt;--&lt;849.0,567.0&gt;&gt;

* u98AA (U+98AA): L&lt;&lt;757.0,519.0&gt;--&lt;221.0,518.0&gt;&gt;

* u98AD (U+98AD): L&lt;&lt;165.0,782.0&gt;--&lt;540.0,784.0&gt;&gt;

* u98AD (U+98AD): L&lt;&lt;465.0,736.0&gt;--&lt;164.0,734.0&gt;&gt;

* u98AE (U+98AE): L&lt;&lt;165.0,782.0&gt;--&lt;540.0,784.0&gt;&gt;

* u98AE (U+98AE): L&lt;&lt;465.0,736.0&gt;--&lt;164.0,734.0&gt;&gt;

* u98AF (U+98AF): L&lt;&lt;461.0,782.0&gt;--&lt;871.0,784.0&gt;&gt;

* u98AF (U+98AF): L&lt;&lt;798.0,736.0&gt;--&lt;460.0,734.0&gt;&gt;

* u98B1 (U+98B1): L&lt;&lt;162.0,782.0&gt;--&lt;537.0,784.0&gt;&gt;

* u98B1 (U+98B1): L&lt;&lt;462.0,736.0&gt;--&lt;161.0,734.0&gt;&gt;

* u98B3 (U+98B3): L&lt;&lt;162.0,782.0&gt;--&lt;537.0,784.0&gt;&gt;

* u98B3 (U+98B3): L&lt;&lt;462.0,736.0&gt;--&lt;161.0,734.0&gt;&gt;

* u98B6 (U+98B6): L&lt;&lt;166.0,782.0&gt;--&lt;523.0,784.0&gt;&gt;

* u98B6 (U+98B6): L&lt;&lt;441.0,736.0&gt;--&lt;165.0,734.0&gt;&gt;

* u98B8 (U+98B8): L&lt;&lt;164.0,782.0&gt;--&lt;515.0,784.0&gt;&gt;

* u98B8 (U+98B8): L&lt;&lt;445.0,736.0&gt;--&lt;163.0,734.0&gt;&gt;

* u98B8 (U+98B8): L&lt;&lt;649.0,94.0&gt;--&lt;647.0,377.0&gt;&gt;

* u98BA (U+98BA): L&lt;&lt;165.0,782.0&gt;--&lt;540.0,784.0&gt;&gt;

* u98BA (U+98BA): L&lt;&lt;465.0,736.0&gt;--&lt;164.0,734.0&gt;&gt;

* u98BC (U+98BC): L&lt;&lt;165.0,782.0&gt;--&lt;540.0,784.0&gt;&gt;

* u98BC (U+98BC): L&lt;&lt;465.0,736.0&gt;--&lt;164.0,734.0&gt;&gt;

* u98C0 (U+98C0): L&lt;&lt;164.0,782.0&gt;--&lt;515.0,784.0&gt;&gt;

* u98C0 (U+98C0): L&lt;&lt;445.0,736.0&gt;--&lt;163.0,734.0&gt;&gt;

* u98C3 (U+98C3): L&lt;&lt;165.0,782.0&gt;--&lt;540.0,784.0&gt;&gt;

* u98C3 (U+98C3): L&lt;&lt;465.0,736.0&gt;--&lt;164.0,734.0&gt;&gt;

* u98C4 (U+98C4): L&lt;&lt;521.0,782.0&gt;--&lt;893.0,784.0&gt;&gt;

* u98C4 (U+98C4): L&lt;&lt;820.0,736.0&gt;--&lt;520.0,734.0&gt;&gt;

* u98C6 (U+98C6): L&lt;&lt;542.0,782.0&gt;--&lt;887.0,784.0&gt;&gt;

* u98C6 (U+98C6): L&lt;&lt;821.0,736.0&gt;--&lt;541.0,734.0&gt;&gt;

* u98C7 (U+98C7): L&lt;&lt;164.0,782.0&gt;--&lt;515.0,784.0&gt;&gt;

* u98C7 (U+98C7): L&lt;&lt;445.0,736.0&gt;--&lt;163.0,734.0&gt;&gt;

* u98C8 (U+98C8): L&lt;&lt;164.0,782.0&gt;--&lt;515.0,784.0&gt;&gt;

* u98C8 (U+98C8): L&lt;&lt;445.0,736.0&gt;--&lt;163.0,734.0&gt;&gt;

* u98CE (U+98CE): L&lt;&lt;204.0,782.0&gt;--&lt;830.0,784.0&gt;&gt;

* u98CE (U+98CE): L&lt;&lt;736.0,736.0&gt;--&lt;202.0,734.0&gt;&gt;

* u98CF (U+98CF): L&lt;&lt;166.0,782.0&gt;--&lt;523.0,784.0&gt;&gt;

* u98CF (U+98CF): L&lt;&lt;441.0,736.0&gt;--&lt;165.0,734.0&gt;&gt;

* u98D0 (U+98D0): L&lt;&lt;186.0,782.0&gt;--&lt;533.0,784.0&gt;&gt;

* u98D0 (U+98D0): L&lt;&lt;451.0,736.0&gt;--&lt;185.0,734.0&gt;&gt;

* u98D1 (U+98D1): L&lt;&lt;166.0,782.0&gt;--&lt;513.0,784.0&gt;&gt;

* u98D1 (U+98D1): L&lt;&lt;431.0,736.0&gt;--&lt;165.0,734.0&gt;&gt;

* u98D2 (U+98D2): L&lt;&lt;461.0,782.0&gt;--&lt;871.0,784.0&gt;&gt;

* u98D2 (U+98D2): L&lt;&lt;798.0,736.0&gt;--&lt;460.0,734.0&gt;&gt;

* u98D3 (U+98D3): L&lt;&lt;166.0,782.0&gt;--&lt;523.0,784.0&gt;&gt;

* u98D3 (U+98D3): L&lt;&lt;441.0,736.0&gt;--&lt;165.0,734.0&gt;&gt;

* u98D4 (U+98D4): L&lt;&lt;166.0,782.0&gt;--&lt;476.0,784.0&gt;&gt;

* u98D4 (U+98D4): L&lt;&lt;629.0,101.0&gt;--&lt;627.0,381.0&gt;&gt;

* u98D5 (U+98D5): L&lt;&lt;166.0,782.0&gt;--&lt;503.0,784.0&gt;&gt;

* u98D5 (U+98D5): L&lt;&lt;421.0,736.0&gt;--&lt;165.0,734.0&gt;&gt;

* u98D7 (U+98D7): L&lt;&lt;166.0,782.0&gt;--&lt;476.0,784.0&gt;&gt;

* u98D8 (U+98D8): L&lt;&lt;521.0,782.0&gt;--&lt;893.0,784.0&gt;&gt;

* u98D8 (U+98D8): L&lt;&lt;820.0,736.0&gt;--&lt;520.0,734.0&gt;&gt;

* u98D9 (U+98D9): L&lt;&lt;542.0,782.0&gt;--&lt;887.0,784.0&gt;&gt;

* u98D9 (U+98D9): L&lt;&lt;821.0,736.0&gt;--&lt;541.0,734.0&gt;&gt;

* u98DA (U+98DA): L&lt;&lt;166.0,782.0&gt;--&lt;476.0,784.0&gt;&gt;

* u994B (U+994B): L&lt;&lt;214.0,47.0&gt;--&lt;420.0,46.0&gt;&gt;

* u994B (U+994B): L&lt;&lt;420.0,-2.0&gt;--&lt;214.0,-1.0&gt;&gt;

* u99B3 (U+99B3): L&lt;&lt;125.0,228.0&gt;--&lt;124.0,723.0&gt;&gt;

* u99BC (U+99BC): L&lt;&lt;160.0,-35.0&gt;--&lt;158.0,195.0&gt;&gt;

* u99C9 (U+99C9): L&lt;&lt;164.0,-27.0&gt;--&lt;162.0,203.0&gt;&gt;

* u99C9 (U+99C9): L&lt;&lt;207.0,205.0&gt;--&lt;209.0,-25.0&gt;&gt;

* u99C9 (U+99C9): L&lt;&lt;269.0,213.0&gt;--&lt;271.0,-17.0&gt;&gt;

* u99D2 (U+99D2): L&lt;&lt;108.0,239.0&gt;--&lt;106.0,723.0&gt;&gt;

* u99D2 (U+99D2): L&lt;&lt;202.0,723.0&gt;--&lt;203.0,602.0&gt;&gt;

* u99D2 (U+99D2): L&lt;&lt;555.0,696.0&gt;--&lt;914.0,694.0&gt;&gt;

* u99D2 (U+99D2): L&lt;&lt;817.0,646.0&gt;--&lt;551.0,648.0&gt;&gt;

* u99D4 (U+99D4): L&lt;&lt;113.0,228.0&gt;--&lt;111.0,723.0&gt;&gt;

* u99D4 (U+99D4): L&lt;&lt;203.0,723.0&gt;--&lt;204.0,598.0&gt;&gt;

* u99DD (U+99DD): L&lt;&lt;185.0,723.0&gt;--&lt;186.0,598.0&gt;&gt;

* u99DD (U+99DD): L&lt;&lt;91.0,228.0&gt;--&lt;89.0,723.0&gt;&gt;

* u99DF (U+99DF): L&lt;&lt;209.0,197.0&gt;--&lt;211.0,-33.0&gt;&gt;

* u99DF (U+99DF): L&lt;&lt;273.0,205.0&gt;--&lt;275.0,-25.0&gt;&gt;

* u99E2 (U+99E2): L&lt;&lt;200.0,201.0&gt;--&lt;202.0,-33.0&gt;&gt;

* u99E2 (U+99E2): L&lt;&lt;222.0,-27.0&gt;--&lt;220.0,207.0&gt;&gt;

* u99EA (U+99EA): L&lt;&lt;208.0,201.0&gt;--&lt;210.0,-33.0&gt;&gt;

* u99ED (U+99ED): L&lt;&lt;157.0,-35.0&gt;--&lt;155.0,195.0&gt;&gt;

* u99ED (U+99ED): L&lt;&lt;204.0,197.0&gt;--&lt;206.0,-33.0&gt;&gt;

* u99EE (U+99EE): L&lt;&lt;210.0,201.0&gt;--&lt;212.0,-33.0&gt;&gt;

* u99F0 (U+99F0): L&lt;&lt;164.0,-27.0&gt;--&lt;162.0,203.0&gt;&gt;

* u99F0 (U+99F0): L&lt;&lt;207.0,205.0&gt;--&lt;209.0,-25.0&gt;&gt;

* u99F0 (U+99F0): L&lt;&lt;269.0,213.0&gt;--&lt;271.0,-17.0&gt;&gt;

* u99F1 (U+99F1): L&lt;&lt;164.0,-35.0&gt;--&lt;162.0,195.0&gt;&gt;

* u99F1 (U+99F1): L&lt;&lt;209.0,197.0&gt;--&lt;211.0,-33.0&gt;&gt;

* u99F2 (U+99F2): L&lt;&lt;146.0,-35.0&gt;--&lt;144.0,195.0&gt;&gt;

* u99FC (U+99FC): L&lt;&lt;164.0,-27.0&gt;--&lt;162.0,203.0&gt;&gt;

* u99FC (U+99FC): L&lt;&lt;207.0,205.0&gt;--&lt;209.0,-25.0&gt;&gt;

* u99FC (U+99FC): L&lt;&lt;269.0,213.0&gt;--&lt;271.0,-17.0&gt;&gt;

* u9A02 (U+9A02): L&lt;&lt;166.0,-35.0&gt;--&lt;164.0,195.0&gt;&gt;

* u9A04 (U+9A04): L&lt;&lt;165.0,-35.0&gt;--&lt;163.0,195.0&gt;&gt;

* u9A05 (U+9A05): L&lt;&lt;152.0,-35.0&gt;--&lt;150.0,195.0&gt;&gt;

* u9A0A (U+9A0A): L&lt;&lt;93.0,788.0&gt;--&lt;430.0,787.0&gt;&gt;

* u9A0F (U+9A0F): L&lt;&lt;210.0,204.0&gt;--&lt;212.0,-26.0&gt;&gt;

* u9A11 (U+9A11): L&lt;&lt;143.0,-35.0&gt;--&lt;141.0,199.0&gt;&gt;

* u9A11 (U+9A11): L&lt;&lt;187.0,201.0&gt;--&lt;189.0,-33.0&gt;&gt;

* u9A1E (U+9A1E): L&lt;&lt;169.0,-27.0&gt;--&lt;167.0,203.0&gt;&gt;

* u9A1E (U+9A1E): L&lt;&lt;212.0,205.0&gt;--&lt;214.0,-25.0&gt;&gt;

* u9A1E (U+9A1E): L&lt;&lt;274.0,213.0&gt;--&lt;276.0,-17.0&gt;&gt;

* u9A20 (U+9A20): L&lt;&lt;161.0,-25.0&gt;--&lt;159.0,209.0&gt;&gt;

* u9A20 (U+9A20): L&lt;&lt;205.0,211.0&gt;--&lt;207.0,-23.0&gt;&gt;

* u9A24 (U+9A24): L&lt;&lt;93.0,779.0&gt;--&lt;430.0,778.0&gt;&gt;

* u9A2B (U+9A2B): L&lt;&lt;298.0,142.0&gt;--&lt;487.0,141.0&gt;&gt;

* u9A2B (U+9A2B): L&lt;&lt;583.0,141.0&gt;--&lt;917.0,140.0&gt;&gt;

* u9A2B (U+9A2B): L&lt;&lt;817.0,92.0&gt;--&lt;298.0,94.0&gt;&gt;

* u9A2E (U+9A2E): L&lt;&lt;153.0,-22.0&gt;--&lt;151.0,208.0&gt;&gt;

* u9A2E (U+9A2E): L&lt;&lt;197.0,210.0&gt;--&lt;199.0,-20.0&gt;&gt;

* u9A2F (U+9A2F): L&lt;&lt;155.0,-35.0&gt;--&lt;153.0,195.0&gt;&gt;

* u9A31 (U+9A31): L&lt;&lt;204.0,205.0&gt;--&lt;206.0,-25.0&gt;&gt;

* u9A31 (U+9A31): L&lt;&lt;265.0,213.0&gt;--&lt;267.0,-17.0&gt;&gt;

* u9A35 (U+9A35): L&lt;&lt;156.0,-22.0&gt;--&lt;154.0,208.0&gt;&gt;

* u9A36 (U+9A36): L&lt;&lt;170.0,-35.0&gt;--&lt;168.0,195.0&gt;&gt;

* u9A36 (U+9A36): L&lt;&lt;213.0,197.0&gt;--&lt;215.0,-33.0&gt;&gt;

* u9A36 (U+9A36): L&lt;&lt;281.0,205.0&gt;--&lt;283.0,-25.0&gt;&gt;

* u9A42 (U+9A42): L&lt;&lt;143.0,-35.0&gt;--&lt;141.0,199.0&gt;&gt;

* u9A42 (U+9A42): L&lt;&lt;187.0,201.0&gt;--&lt;189.0,-33.0&gt;&gt;

* u9A43 (U+9A43): L&lt;&lt;155.0,-35.0&gt;--&lt;153.0,195.0&gt;&gt;

* u9A45 (U+9A45): L&lt;&lt;201.0,210.0&gt;--&lt;203.0,-20.0&gt;&gt;

* u9A4A (U+9A4A): L&lt;&lt;213.0,197.0&gt;--&lt;215.0,-33.0&gt;&gt;

* u9A4A (U+9A4A): L&lt;&lt;281.0,205.0&gt;--&lt;283.0,-25.0&gt;&gt;

* u9A4C (U+9A4C): L&lt;&lt;152.0,-35.0&gt;--&lt;150.0,195.0&gt;&gt;

* u9A4C (U+9A4C): L&lt;&lt;198.0,197.0&gt;--&lt;200.0,-33.0&gt;&gt;

* u9A4C (U+9A4C): L&lt;&lt;267.0,205.0&gt;--&lt;269.0,-25.0&gt;&gt;

* u9A4D (U+9A4D): L&lt;&lt;161.0,-35.0&gt;--&lt;159.0,195.0&gt;&gt;

* u9A4D (U+9A4D): L&lt;&lt;207.0,197.0&gt;--&lt;209.0,-33.0&gt;&gt;

* u9A57 (U+9A57): L&lt;&lt;153.0,-22.0&gt;--&lt;151.0,208.0&gt;&gt;

* u9A57 (U+9A57): L&lt;&lt;197.0,210.0&gt;--&lt;199.0,-20.0&gt;&gt;

* u9A5B (U+9A5B): L&lt;&lt;190.0,197.0&gt;--&lt;192.0,-33.0&gt;&gt;

* u9A5B (U+9A5B): L&lt;&lt;258.0,205.0&gt;--&lt;260.0,-25.0&gt;&gt;

* u9A5F (U+9A5F): L&lt;&lt;72.0,771.0&gt;--&lt;420.0,770.0&gt;&gt;

* u9A62 (U+9A62): L&lt;&lt;154.0,-35.0&gt;--&lt;152.0,195.0&gt;&gt;

* u9A62 (U+9A62): L&lt;&lt;197.0,197.0&gt;--&lt;199.0,-33.0&gt;&gt;

* u9A64 (U+9A64): L&lt;&lt;152.0,-35.0&gt;--&lt;150.0,195.0&gt;&gt;

* u9A64 (U+9A64): L&lt;&lt;198.0,197.0&gt;--&lt;200.0,-33.0&gt;&gt;

* u9A64 (U+9A64): L&lt;&lt;267.0,205.0&gt;--&lt;269.0,-25.0&gt;&gt;

* u9A65 (U+9A65): L&lt;&lt;155.0,-35.0&gt;--&lt;153.0,195.0&gt;&gt;

* u9A66 (U+9A66): L&lt;&lt;143.0,-31.0&gt;--&lt;141.0,199.0&gt;&gt;

* u9A66 (U+9A66): L&lt;&lt;182.0,201.0&gt;--&lt;183.0,-29.0&gt;&gt;

* u9A66 (U+9A66): L&lt;&lt;244.0,209.0&gt;--&lt;246.0,-21.0&gt;&gt;

* u9A69 (U+9A69): L&lt;&lt;156.0,-35.0&gt;--&lt;154.0,195.0&gt;&gt;

* u9A69 (U+9A69): L&lt;&lt;199.0,197.0&gt;--&lt;201.0,-33.0&gt;&gt;

* u9A69 (U+9A69): L&lt;&lt;267.0,205.0&gt;--&lt;269.0,-25.0&gt;&gt;

* u9AD1 (U+9AD1): L&lt;&lt;356.0,736.0&gt;--&lt;215.0,735.0&gt;&gt;

* u9AD2 (U+9AD2): L&lt;&lt;356.0,735.0&gt;--&lt;215.0,736.0&gt;&gt;

* u9AD2 (U+9AD2): L&lt;&lt;582.0,491.0&gt;--&lt;710.0,492.0&gt;&gt;

* u9AD3 (U+9AD3): L&lt;&lt;469.0,468.0&gt;--&lt;468.0,339.0&gt;&gt;

* u9AEA (U+9AEA): L&lt;&lt;327.0,174.0&gt;--&lt;840.0,171.0&gt;&gt;

* u9AEA (U+9AEA): L&lt;&lt;650.0,125.0&gt;--&lt;290.0,126.0&gt;&gt;

* u9B3B (U+9B3B): L&lt;&lt;357.0,674.0&gt;--&lt;356.0,796.0&gt;&gt;

* u9B3B (U+9B3B): L&lt;&lt;424.0,796.0&gt;--&lt;425.0,674.0&gt;&gt;

* u9BF4 (U+9BF4): L&lt;&lt;472.0,782.0&gt;--&lt;876.0,784.0&gt;&gt;

* u9BF4 (U+9BF4): L&lt;&lt;796.0,736.0&gt;--&lt;472.0,734.0&gt;&gt;

* u9C00 (U+9C00): L&lt;&lt;666.0,201.0&gt;--&lt;913.0,199.0&gt;&gt;

* u9C00 (U+9C00): L&lt;&lt;775.0,153.0&gt;--&lt;656.0,154.0&gt;&gt;

* u9C2E (U+9C2E): L&lt;&lt;792.0,476.0&gt;--&lt;793.0,736.0&gt;&gt;

* u9C47 (U+9C47): L&lt;&lt;928.0,686.0&gt;--&lt;567.0,685.0&gt;&gt;

* u9C83 (U+9C83): L&lt;&lt;602.0,24.0&gt;--&lt;837.0,25.0&gt;&gt;

* u9C83 (U+9C83): L&lt;&lt;929.0,-23.0&gt;--&lt;517.0,-24.0&gt;&gt;

* u9CBA (U+9CBA): L&lt;&lt;472.0,782.0&gt;--&lt;876.0,784.0&gt;&gt;

* u9CBA (U+9CBA): L&lt;&lt;796.0,736.0&gt;--&lt;472.0,734.0&gt;&gt;

* u9CF3 (U+9CF3): L&lt;&lt;268.0,157.0&gt;--&lt;269.0,596.0&gt;&gt;

* u9D15 (U+9D15): L&lt;&lt;95.0,220.0&gt;--&lt;97.0,719.0&gt;&gt;

* u9D52 (U+9D52): L&lt;&lt;507.0,207.0&gt;--&lt;509.0,747.0&gt;&gt;

* u9D59 (U+9D59): L&lt;&lt;489.0,207.0&gt;--&lt;491.0,747.0&gt;&gt;

* u9DC2 (U+9DC2): L&lt;&lt;499.0,228.0&gt;--&lt;502.0,760.0&gt;&gt;

* u9DC8 (U+9DC8): L&lt;&lt;84.0,211.0&gt;--&lt;86.0,710.0&gt;&gt;

* u9DD7 (U+9DD7): L&lt;&lt;528.0,183.0&gt;--&lt;529.0,729.0&gt;&gt;

* u9DF8 (U+9DF8): L&lt;&lt;514.0,183.0&gt;--&lt;515.0,729.0&gt;&gt;

* u9E0C (U+9E0C): L&lt;&lt;97.0,220.0&gt;--&lt;99.0,719.0&gt;&gt;

* u9E92 (U+9E92): L&lt;&lt;476.0,363.0&gt;--&lt;475.0,504.0&gt;&gt;

* u9E92 (U+9E92): L&lt;&lt;550.0,552.0&gt;--&lt;551.0,297.0&gt;&gt;

* u9EAD (U+9EAD): L&lt;&lt;246.0,296.0&gt;--&lt;479.0,297.0&gt;&gt;

* u9EAD (U+9EAD): L&lt;&lt;345.0,249.0&gt;--&lt;221.0,248.0&gt;&gt;

* u9EAF (U+9EAF): L&lt;&lt;246.0,296.0&gt;--&lt;479.0,297.0&gt;&gt;

* u9EAF (U+9EAF): L&lt;&lt;345.0,249.0&gt;--&lt;221.0,248.0&gt;&gt;

* u9EB4 (U+9EB4): L&lt;&lt;223.0,296.0&gt;--&lt;456.0,297.0&gt;&gt;

* u9EB4 (U+9EB4): L&lt;&lt;322.0,249.0&gt;--&lt;198.0,248.0&gt;&gt;

* u9EB5 (U+9EB5): L&lt;&lt;246.0,296.0&gt;--&lt;479.0,297.0&gt;&gt;

* u9EB5 (U+9EB5): L&lt;&lt;345.0,249.0&gt;--&lt;221.0,248.0&gt;&gt;

* u9F21 (U+9F21): L&lt;&lt;204.0,575.0&gt;--&lt;779.0,576.0&gt;&gt;

* u9F34 (U+9F34): L&lt;&lt;482.0,25.0&gt;--&lt;856.0,24.0&gt;&gt;

* uFA1D (U+FA1D): L&lt;&lt;164.0,754.0&gt;--&lt;166.0,420.0&gt;&gt;

* uFA1D (U+FA1D): L&lt;&lt;91.0,420.0&gt;--&lt;89.0,754.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table set to optimize rendering? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-gasp">googlefonts/gasp</a></summary>
    <div>









* ⚠️ **WARN** <p>The gasp range 0xFFFF value 0x0A should be set to 0x0F.</p>
 [code: unset-flags]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 1 | 0 | 4 | 21 | 109 | 6 | 95 | 0 | 
| 0% | 0% | 2% | 9% | 46% | 3% | 40% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
