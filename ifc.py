from seleniumbase import SB

with SB(uc=True, test=True, locale="en") as sb:
    url = "https://ifcameroun.extranet-aec.com/students/login#/"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.type('input[name="matricule"]',"salleidriss60@gmail.com")
    sb.type('input[name="password"]',"wo?!%BON3")
    sb.click('button[type="submit"]')
    sb.click('button[type="submit"]')
    sb.click('[href*="/examinations/view/all"]')
    sb.click('[href*="/carts/view#/addExamination"]')
    sb.click('input[role="combobox"][autocomplete="off"]')
    sb.sleep(40)