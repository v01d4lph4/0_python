# 1. string manipulation
name = "v01d4lph4"  # declaration       // OUTPUT ↓
# -------------------------------------------------- #
name[0]             # first char        // v     
name[-1]            # last char         // 4     
name[::-1]          # reverse           // 4hpl4d10v
name[4:9]           # slice             // 4lph4
name + "?!"         # concatenation     // v01d4lph4?!
name.upper()        # upper case        // V01D4LPH4
name.islower()      # check if lower    // True
name.count("4")     # count pattern     // 2
name.find("h")      # find char index   // 7
len(name)           # length            // 9
"v01d" in name      # inline search     // true
