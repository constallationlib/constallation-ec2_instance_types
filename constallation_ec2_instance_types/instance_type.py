class InstanceType:
    def __init__(self,
                 instance_family: str = None,
                 instance_size: str = None,
                 free_tier_eligible: bool = None,
                 bare_metal: bool = None,
                 hypervisor: str = None,
                 vcpus: int = None,
                 architecture: str = None,
                 cores: int = None,
                 valid_cores: int = None,
                 threads_per_core: int = None,
                 valid_threads_per_core: int = None,
                 sustained_clock_speed: float = None,
                 memory_gb: float = None,
                 storage_gb: float = None,
                 storage_type: str = None,
                 network_performance: str = None,
                 instance_storage_gb: float = None,
                 gpu: bool = None,
                 gpu_count: int = None,
                 gpu_memory_gb: float = None,
                 eni: int = None,
                 ipv6_support: bool = None):
        self._instance_family = instance_family
        self._instance_size = instance_size
        self._free_tier_eligible = free_tier_eligible
        self._bare_metal = bare_metal
        self._hypervisor = hypervisor
        self._vcpus = vcpus
        self._architecture = architecture
        self._cores = cores
        self._valid_cores = valid_cores
        self._threads_per_core = threads_per_core
        self._valid_threads_per_core = valid_threads_per_core
        self._sustained_clock_speed = sustained_clock_speed
        self._memory_gb = memory_gb
        self._storage_gb = storage_gb
        self._storage_type = storage_type
        self._network_performance = network_performance
        self._instance_storage_gb = instance_storage_gb
        self._gpu = gpu
        self._gpu_count = gpu_count
        self._gpu_memory_gb = gpu_memory_gb
        self._eni = eni
        self._ipv6_support = ipv6_support

    @property
    def instance_type(self):
        return f"{self._instance_family}.{self._instance_size}"

    @property
    def instance_family(self):
        return self._instance_family

    @property
    def instance_size(self):
        return self._instance_size

    @property
    def free_tier_eligible(self):
        return self._free_tier_eligible

    @property
    def bare_metal(self):
        return self._bare_metal

    @property
    def hypervisor(self):
        return self._hypervisor

    @property
    def vcpus(self):
        return self._vcpus

    @property
    def architecture(self):
        return self._architecture

    @property
    def cores(self):
        return self._cores

    @property
    def valid_cores(self):
        return self._valid_cores

    @property
    def threads_per_core(self):
        return self._threads_per_core

    @property
    def valid_threads_per_core(self):
        return self._valid_threads_per_core

    @property
    def sustained_clock_speed(self):
        return self._sustained_clock_speed

    @property
    def memory_gb(self):
        return self._memory_gb

    @property
    def storage_gb(self):
        return self._storage_gb

    @property
    def storage_type(self):
        return self._storage_type

    @property
    def network_performance(self):
        return self._network_performance

    @property
    def instance_storage_gb(self):
        return self._instance_storage_gb

    @property
    def gpu(self):
        return self._gpu

    @property
    def gpu_count(self):
        return self._gpu_count

    @property
    def gpu_memory_gb(self):
        return self._gpu_memory_gb

    @property
    def eni(self):
        return self._eni

    @property
    def ipv6_support(self):
        return self._ipv6_support

    def __repr__(self):
        return (f"InstanceType(instance_family={self._instance_family!r}, "
                f"instance_size={self._instance_size!r}, "
                f"free_tier_eligible={self._free_tier_eligible!r}, "
                f"bare_metal={self._bare_metal!r}, "
                f"hypervisor={self._hypervisor!r}, "
                f"vcpus={self._vcpus!r}, "
                f"architecture={self._architecture!r}, "
                f"cores={self._cores!r}, "
                f"valid_cores={self._valid_cores!r}, "
                f"threads_per_core={self._threads_per_core!r}, "
                f"valid_threads_per_core={self._valid_threads_per_core!r}, "
                f"sustained_clock_speed={self._sustained_clock_speed!r}, "
                f"memory_gb={self._memory_gb!r}, "
                f"storage_gb={self._storage_gb!r}, "
                f"storage_type={self._storage_type!r}, "
                f"network_performance={self._network_performance!r}, "
                f"instance_storage_gb={self._instance_storage_gb!r}, "
                f"gpu={self._gpu!r}, "
                f"gpu_count={self._gpu_count!r}, "
                f"gpu_memory_gb={self._gpu_memory_gb!r}, "
                f"eni={self._eni!r}, "
                f"ipv6_support={self._ipv6_support!r})")