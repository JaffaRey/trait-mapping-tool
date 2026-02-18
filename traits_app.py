import streamlit as st

TRAITS = [
    "Driver",
    "Navigator",
    "Harmoniser",
    "Guardian",
    "Connector",
    "Analyst",
    "Catalyst"
]


TRAIT_DESCRIPTIONS = {
    "Driver": "Action-oriented, decisive, forward-moving.",
    "Navigator": "Strategic, structured, clarity-seeking.",
    "Harmoniser": "Emotionally attuned, peace-focused, relational.",
    "Guardian": "Protective, stabilising, dependable.",
    "Connector": "Community-minded, social, bridge-builder.",
    "Analyst": "Logical, detail-driven, pattern-focused.",
    "Catalyst": "Creative, energising, change-igniting."
}


def compare_two_traits(mine, theirs):
    if mine == theirs:
        return f"You both share {mine}, meaning your core rhythms align naturally."
    else:
        return (
            f"A {mine} interacting with a {theirs} creates a dynamic contrast. "
            "This can be complementary or challenging depending on context."
        )

def build_copilot_prompt(
    my_primary, my_secondary, my_background,
    other_primary, other_secondary, other_background
):
    return f"""
Using the Seven Traits model from The Age of Disconnection, analyse the relationship dynamics between two people.

Person A:
- Primary: {my_primary}
- Secondary: {my_secondary}
- Background: {my_background}

Person B:
- Primary: {other_primary}
- Secondary: {other_secondary}
- Background: {other_background}

Please explain:
1. Core alignment or friction between their primary traits.
2. How their secondary traits influence collaboration, communication, and emotional rhythm.
3. How background traits shape long-term patterns.
4. Potential strengths, blind spots, and growth opportunities.
5. The overall 6-5 rhythm between them.

Write the response in a warm, psychologically insightful tone.
"""

st.title("Trait Comparison Tool — The Age of Disconnection")

st.subheader("Your Traits")

# YOUR PRIMARY
my_primary = st.selectbox("Your Primary Trait", TRAITS, key="my_primary")

# YOUR SECONDARY (remove primary)
my_secondary_options = [t for t in TRAITS if t != my_primary]
my_secondary = st.selectbox("Your Secondary Trait", my_secondary_options, key="my_secondary")

# YOUR BACKGROUND (remove primary + secondary)
my_background_options = [t for t in TRAITS if t not in [my_primary, my_secondary]]
my_background = st.selectbox("Your Background Trait", my_background_options, key="my_background")


st.subheader("Their Traits")

# THEIR PRIMARY
other_primary = st.selectbox("Their Primary Trait", TRAITS, key="other_primary")

# THEIR SECONDARY (remove their primary)
other_secondary_options = [t for t in TRAITS if t != other_primary]
other_secondary = st.selectbox("Their Secondary Trait", other_secondary_options, key="other_secondary")

# THEIR BACKGROUND (remove their primary + secondary)
other_background_options = [t for t in TRAITS if t not in [other_primary, other_secondary]]
other_background = st.selectbox("Their Background Trait", other_background_options, key="other_background")


st.markdown("---")

if st.button("Compare Traits"):
    st.header("Trait Comparison Summary")

    st.write("### Primary Trait Interaction")
    st.write(compare_two_traits(my_primary, other_primary))

    st.write("### Secondary Trait Interaction")
    st.write(compare_two_traits(my_secondary, other_secondary))

    st.write("### Background Trait Interaction")
    st.write(compare_two_traits(my_background, other_background))

    st.markdown("---")
    st.header("Copilot Prompt (Copy & Paste)")
    prompt = build_copilot_prompt(
        my_primary, my_secondary, my_background,
        other_primary, other_secondary, other_background
    )
    st.code(prompt, language="markdown")

st.markdown("---")
st.caption("Built for The Age of Disconnection — Trait Mapping Tool")

