# Allowable Ranges for 2 Series Numeric Formats

Percent (Unsigned, 16b): 0.000% to 100%. (3 decimal places of precision).

Legal for INTEGER_PARAMETER, LONG_INTEGER_PARAMETER

Percent (Signed, 16b): -50% to 49.999% (3 decimal places of precision).

Legal for SIGNED_INTEGER_PARAMETER, SIGNED_LONG_INTEGER_PARAMETER

Decimal (Unsigned, 16b): 0d to 65535d

Legal for INTEGER_PARAMETER, LONG_INTEGER_PARAMETER

Decimal (Signed, 16b): -32768d to 32767d

Legal for SIGNED_INTEGER_PARAMETER, SIGNED_LONG_INTEGER_PARAMETER

Decimal (Unsigned, 32b): 0d to 4294967295d

Legal for LONG_INTEGER_PARAMETER

Decimal (Signed, 32b): -2147483648d to 2147483647d

Legal for SIGNED_LONG_INTEGER_PARAMETER

Ticks (Unsigned, 16b): 0t to 65535t

Legal for INTEGER_PARAMETER, LONG_INTEGER_PARAMETER

Ticks (Signed, 16b): SIGNED TIME NOT LEGAL (i.e. can't allow -5t)

Ticks (Unsigned, 32b): 0t to 4294967295t

Legal for LONG_INTEGER_PARAMETER

Ticks (Signed, 32b): SIGNED TIME NOT LEGAL (i.e. can't allow -5t)

Hex (Unsigned, 16b): 0h to FFFFh

Legal for INTEGER_PARAMETER, LONG_INTEGER_PARAMETER

Hex (Signed, 16b): -8000h to 7FFFh

Legal for SIGNED_INTEGER_PARAMETER, SIGNED_LONG_INTEGER_PARAMETER

Hex (Unsigned, 32b): 0h to FFFFFFFFh

Legal for LONG_INTEGER_PARAMETER

Hex (Signed, 32b): -80000000h to 7FFFFFFFh

Legal for SIGNED_LONG_INTEGER_PARAMETER

Time (Unsigned, 16b): 0s to 655.35s

Legal for INTEGER_PARAMETER, LONG_INTEGER_PARAMETER

Time (Signed, 16b): SIGNED TIME NOT LEGAL (i.e. can't allow -5s)

Time (Unsigned, 32b): 0s to 4294967295s

Legal for LONG_INTEGER_PARAMETER

Time (Signed, 32b): SIGNED TIME NOT LEGAL (i.e. can't allow -5s)

Character (Unsigned, 16b): any single typeable character between '', i.e. 'a'.

Legal for INTEGER_PARAMETER, LONG_INTEGER_PARAMETER

Character (Signed, 16b): NOT LEGAL (i.e. can't allow -'a')

Character (Unsigned, 32b): NOT LEGAL

Character (Signed, 32): NOT LEGAL

Note for time, the following formats are valid:

HH.MM.SS.HS

MM.SS.HS

SS.HS

SS

.HS

Note that any of the above values don't need to be padded with leading 0's, so that

02.03.04.5s = 2.3.4.5s

Padding HS with leading 0's makes it a different # since it's a fraction!

For example,

2.25.36.08s (HH.MM.SS.HS)

145.36.08s (MM.SS.HS)

8736.08s (SS.HS)

---
*Source: https://help.crestron.com/simpl_plus/Content/Allowable_Ranges_for_2_Series_Numeric_Formats.htm*
