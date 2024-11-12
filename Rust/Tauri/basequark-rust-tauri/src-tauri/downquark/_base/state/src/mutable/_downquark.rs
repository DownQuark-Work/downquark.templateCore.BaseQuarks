use std::sync::Mutex;
use particle_flows::particles::symbols::structs::_downquark::SetupState;

pub fn get_setup_state() -> Mutex<SetupState> {
    Mutex::new(SetupState {
        frontend_task: false,
        backend_task: false,
    })
}
