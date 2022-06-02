/// <reference types="cypress" />
/// <reference types="cypress-downloadfile"/>
Cypress.config().waitForAnimations = true;


// Testowanie aplikacji internetowego sklepu.
import { parametersContacttManager } from "../../fixtures/parametrsWebApp";

const homePage = parametersContacttManager.formURL + "index.php"
const contactPage = parametersContacttManager.formURL + "index.php?controller=contact"
// nazwa pliku randomowo sciągniętego i zapisanego do "fixture" 
const fileName = 'image.jpg';


// sprawdzi adres strony na której jesteśmy
const confirmURL = (url) => {
    cy.location().should(($loc=>{
            expect($loc.href).to.eq(url);
        })
    )}

describe("form veryfication tests", ()=>{
    it("should open app",()=>{
        cy.visit(parametersContacttManager.formURL);
    })
    // 1. Kliknij „Contact us”
    // oraz sprawdza czy przycisk "Contact us" istnieje i czy URL jest poprawny
    it('Should open Contact us page and confirm URL',()=>{
        confirmURL(homePage);
        cy.clickButton(parametersContacttManager.buttonConatactUs);
        confirmURL(contactPage);
    })
    // 2. Wybierz rodzaj zapytania
    it("contakt us",()=>{
        cy.contacUs(parametersContacttManager.selectChoose);
    })
    // 3. Wpisz e-mail
    it('enter email',()=>{
        cy.enterEmail(parametersContacttManager.email);
    })
    // 4. Wpisz numer referencyjny zamówienia
    it('enter order and confirm',()=>{
        cy.enterOrder(parametersContacttManager.order);
    })
    // 5. załącz plik np. jpg
    it('save and upload random jpg file',()=>{
        cy.uploadFile(parametersContacttManager.randomFile,
            parametersContacttManager.fileName);
    })
    // 6. Wpisz wiadomośc np. "Correctly sent message"
    it('enter message to customer service',()=>{
        cy.message(parametersContacttManager.messageToService);
    })
    // 7. Kliknij przycisk "Send" + assertion
    it('should send message "pass"',()=>{
        cy.sendSuccessfully(parametersContacttManager.submitButton,
            parametersContacttManager.alertSuccessfully);
    })
    // 8. Kliknij przycisk "Send" + assertion
    it('should send message "not pass"',()=>{
        cy.sendDanger(parametersContacttManager.submitButton,
            parametersContacttManager.alertDanger);
    })
})

// Oczekiwany rezultat:
// 1. użytkownik otrzymuje komunikat:
// Your message has been successfully sent to our team.

// Warunki końcowe:
// 1. Wiadomość zostaje wysłana

// Not pass: 
// Otrzymujemy komunikat "An error occurred while sending the message.", choć wszystkie kroki przeszły pomyślnie.