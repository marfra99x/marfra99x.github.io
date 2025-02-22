import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def fetch(session, url):
    """Fetch page content asynchronously."""
    async with session.get(url) as response:
        return await response.text()

async def get_ancestors(session, person_id, result, ancestors=None):


    """Recursively fetch advisors only (not students)."""
    if ancestors is None:
        ancestors = []

    url = f"https://www.mathgenealogy.org/id.php?id={person_id}"
    html = await fetch(session, url)
    soup = BeautifulSoup(html, "html.parser")

    # Extract name
    name_tag = soup.find("h2")
    name = name_tag.text.strip() if name_tag else f"ID {person_id}"

    # If already visited, stop recursion
    if (person_id, name) in ancestors:
        return ancestors

    ancestors.append((person_id, name))

    # Locate the advisor(s)
    advisors = []
    for p_tag in soup.find_all("p"):
        if any(keyword in p_tag.text for keyword in ["Advisor:", "Advisor 1:", "Advisor 2:", "Advisor 3:"]):
            if "Advisor: Unknown" in p_tag.text:
                print("UNKNOWN ADVISOR")
                continue
            advisor_links = p_tag.find_all("a", href=True)
            for advisor_link in advisor_links:
                if advisor_link and "id.php?id=" in advisor_link["href"]:
                    advisor_id = advisor_link["href"].split("=")[-1]
                    advisors.append((advisor_id, advisor_link.text.strip()))
                    print(f"{name} -> {advisor_link.text.strip()}\n")
                    result.append(f"{name} -> {advisor_link.text.strip()}\n")

    # Process advisors recursively
    for advisor_id, advisor_name in advisors:
        await get_ancestors(session=session, person_id=advisor_id, ancestors=ancestors, result=result)

    return ancestors

async def main():
    """Fetch genealogy data and save as a Markdown file."""
    person_id = "XXXX" 

    result = []
    
    async with aiohttp.ClientSession() as session:
        ancestors = await get_ancestors(session=session, person_id=person_id, result=result)

    # Generate Markdown content
    md_content = "# My Mathematical Genealogy\n\n"
    md_content += "A list of my academic ancestors from the [Mathematics Genealogy Project](https://www.mathgenealogy.org):\n\n"

    for ancestor in reversed(ancestors):  # Reverse order: oldest to newest
        md_content += f"- **{ancestor[1]}** [(Math Genealogy)](https://www.mathgenealogy.org/id.php?id={ancestor[0]})\n"

    # Save to a Markdown file

    print(len(result))

    with open("my_genealogy.txt", "w", encoding="utf-8") as f:
        for r in result:
            f.write(r)



    print("Genealogy list saved as 'my_genealogy.md'.")

# Run the script
asyncio.run(main())
