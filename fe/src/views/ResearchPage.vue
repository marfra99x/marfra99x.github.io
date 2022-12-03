<template>
    <div>
        <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <v-flex xs10 sm10 md10 lg8 xl8 class="mt-4 pt-4 pr-4 mr-4">
                <div>
                    Since 2020 I published {{ number_of_articles }} articles in International Journals and
                    Conferences especially in the field of Sampled String Matching.
                    <br>
                    My research interest are mainly focused on: text and strings processing algorithms, exact and
                    approximate pattern matching, multiple string matching, offline string matching, pattern matching on
                    compressed texts and sort algorithms.
                </div>
            </v-flex>
            <v-flex justify-end align-end xs10 sm10 md10 lg3 xl3 class="mt-4 pt-2">
                <v-card class="d-flex flex-column" max-width="300">
                    <v-card-text>
                        <div class="text-center display-1 primary--text">
                            Summary
                        </div>
                        <span class="primary--text">Publications:</span>
                        <span class=""> {{ number_of_articles }}</span>
                        <br>
                        <span class="primary--text">Citation:</span>
                        <span class=""> {{ number_of_citations }}</span>
                        <br>
                        <span class="primary--text">H-index:</span>
                        <span class=""> {{ h_index }}</span>
                        <br>
                        <span class="primary--text">Co-authored:</span>
                        <span class=""> 4</span>
                        <br>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
        <v-layout row justify-start align-center wrap class="mt-4 pt-2">
            <v-flex xs10 sm10 md10 lg8 xl8 class="mt-4 pt-4 pr-4 mr-4">
                <div class="headline text-center primary--text">List of published papers:</div>
            </v-flex>
        </v-layout>
        <v-layout row justify-center align-center wrap class="mt-4 pt-2">
            <v-flex xs10 sm10 md10 lg8 xl8 class="mt-4 pt-4">
                <div v-for="item of papers" :key="item.title">
                    <span class="primary--text">
                        {{ item['year'] }}.
                    </span>
                    <span>
                        <a :href="item['href']" target='_blank'>{{ item['title'] }}</a>
                    </span>
                    <br>
                    <div>
                        {{ item['authors'] }}
                        <br>
                        {{ item['publisher'] }}, {{ item["year"] }}
                    </div>
                    <br>
                    <!-- <a style="text-decoration: none" :href="item['href']" target='_blank'>{{ item['title'] }}</a> -->
                </div>
            </v-flex>
            <v-flex xs12 sm12 md12 lg3 xl3 class="mt-4 pt-4">

            </v-flex>
        </v-layout>
    </div>
</template>

<script>

export default {
    data() {
        document.title = "Research | Francesco Marino"
        return {
            papers: [
                {
                    title: "Reducing Time and Space in Indexed String Matching by Characters Distance Text Sampling.",
                    publisher: "Stringology",
                    href: "http://www.stringology.org/event/2020/p13.html",
                    year: "2020",
                    authors: "Simone Faro and Francesco Pio Marino"
                },
                {
                    title: "Fast-Insertion-Sort: a New Family of Efficient Variants of the Insertion-Sort Algorithm.",
                    publisher: "SOFSEM (Doctoral Student Research Forum)",
                    href: "https://ceur-ws.org/Vol-2568/paper4.pdf",
                    year: "2020",
                    authors: "Simone Faro, Francesco Pio Marino and Stefano Scafiti"
                },
                {
                    title: "Efficient Online String Matching Based on Characters Distance Text Sampling.",
                    publisher: "Algorithmica 82(11): 3390-3412",
                    href: "https://link.springer.com/article/10.1007/s00453-020-00732-4",
                    year: "2020",
                    authors: "Simone Faro, Francesco Pio Marino and Arianna Pavone"
                },
                {
                    title: "Towards an Efficient Text Sampling Approach for Exact and Approximate Matching.",
                    publisher: "Stringology",
                    href: "http://www.stringology.org/event/2021/p07.html",
                    year: "2021",
                    authors: "	Simone Faro, Francesco Pio Marino, Arianna Pavone and Antonio Scardace"
                },
                {
                    title: "Enhancing Characters Distance Text Sampling by Condensed Alphabets. ",
                    publisher: " Italian Conference on Theoretical Computer Science",
                    href: "https://ceur-ws.org/Vol-3072/paper1.pdf",
                    year: "2021",
                    authors: "Simone Faro, Francesco Pio Marino and Arianna Pavone"
                },
            ],
            number_of_articles: 6,
            number_of_citations: 10,
            h_index: 2,
        }
    },
}

</script>
