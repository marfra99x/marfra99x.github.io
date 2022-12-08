import Vue from 'vue'
import VueI18n from 'vue-i18n'
import { i18n_en } from '@/i18n/en'
import { i18n_it } from '@/i18n/it'
import { i18n_fr } from '@/i18n/fr'

Vue.use(VueI18n)

const messages = {
    it: i18n_it,
    en: i18n_en,
    fr: i18n_fr,
}
export const i18n = new VueI18n({
    locale: 'en',
    messages,
})
